#!/usr/bin/env python3
"""
reminiscence — Seep Logos 長期記憶システム (Phase 1)
SQLite + FTS5 によるキーワード検索ベースの記憶管理CLI
"""

import sqlite3
import argparse
import datetime
import glob
import json
import os
import sys

try:
    from janome.tokenizer import Tokenizer as JanomeTokenizer
    _janome = JanomeTokenizer()
    def tokenize_ja(text):
        """日本語テキストを形態素解析して名詞・動詞・形容詞のみ返す"""
        tokens = []
        for token in _janome.tokenize(text):
            pos = token.part_of_speech.split(',')[0]
            if pos in ('名詞', '動詞', '形容詞'):
                surface = token.surface
                if len(surface) >= 2:
                    tokens.append(surface)
        return tokens
except ImportError:
    def tokenize_ja(text):
        return []

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory.db")
PROJECT_CLAUDE_DIR = os.path.expanduser(
    "~/.claude/projects/-Users-matsuura-hisashi-com-Seep-Logos-agents"
)
MIN_CHUNK_LENGTH = 30  # これより短いQ&Aは保存しない


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS memories (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            content    TEXT    NOT NULL,
            tags       TEXT    DEFAULT '',
            type       TEXT    DEFAULT 'general',
            created_at TEXT    NOT NULL,
            updated_at TEXT    NOT NULL
        );

        CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts
        USING fts5(content, tags, type, content='memories', content_rowid='id');

        CREATE TRIGGER IF NOT EXISTS memories_ai AFTER INSERT ON memories BEGIN
            INSERT INTO memories_fts(rowid, content, tags, type)
            VALUES (new.id, new.content, new.tags, new.type);
        END;

        CREATE TRIGGER IF NOT EXISTS memories_ad AFTER DELETE ON memories BEGIN
            INSERT INTO memories_fts(memories_fts, rowid, content, tags, type)
            VALUES ('delete', old.id, old.content, old.tags, old.type);
        END;

        CREATE TRIGGER IF NOT EXISTS memories_au AFTER UPDATE ON memories BEGIN
            INSERT INTO memories_fts(memories_fts, rowid, content, tags, type)
            VALUES ('delete', old.id, old.content, old.tags, old.type);
            INSERT INTO memories_fts(rowid, content, tags, type)
            VALUES (new.id, new.content, new.tags, new.type);
        END;

        CREATE TABLE IF NOT EXISTS processed_sessions (
            session_file TEXT PRIMARY KEY,
            processed_at TEXT NOT NULL
        );
    """)
    conn.commit()


def extract_text(content):
    """contentフィールドからテキストを抽出（配列・文字列どちらにも対応）"""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", "").strip())
        return " ".join(parts).strip()
    return ""


def load_session_messages(filepath):
    """jsonlからuser/assistantメッセージを順番に取り出す"""
    messages = []
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("type") not in ("user", "assistant"):
                continue
            msg = obj.get("message", {})
            role = msg.get("role", "")
            text = extract_text(msg.get("content", ""))
            if role and text:
                messages.append({
                    "role": role,
                    "text": text,
                    "timestamp": obj.get("timestamp", ""),
                })
    return messages


def build_chunks(messages):
    """userとassistantのペアをQ&Aチャンクに変換"""
    chunks = []
    i = 0
    while i < len(messages):
        if messages[i]["role"] == "user":
            user = messages[i]
            assistant = None
            if i + 1 < len(messages) and messages[i + 1]["role"] == "assistant":
                assistant = messages[i + 1]
                i += 2
            else:
                i += 1

            q = user["text"][:300]
            a = assistant["text"][:800] if assistant else ""
            chunk = f"Q: {q}\nA: {a}" if a else f"Q: {q}"

            if len(chunk) >= MIN_CHUNK_LENGTH:
                chunks.append({
                    "content": chunk,
                    "timestamp": user["timestamp"],
                })
        else:
            i += 1
    return chunks


def cmd_process_session(args, conn):
    """未処理・更新済みセッションをすべて読み込んでQ&Aチャンクとして自動保存"""
    project_dir = args.project_dir or PROJECT_CLAUDE_DIR

    # トップレベルの .jsonl のみ対象（サブエージェントのものは除外）
    files = [
        f for f in glob.glob(os.path.join(project_dir, "*.jsonl"))
        if os.path.isfile(f)
    ]
    if not files:
        print("[reminiscence] セッションファイルが見つかりません。")
        return

    total_saved = 0
    for filepath in files:
        basename = os.path.basename(filepath)
        current_size = os.path.getsize(filepath)

        # 処理済みかどうか確認
        row = conn.execute(
            "SELECT file_size FROM processed_sessions WHERE session_file = ?", (basename,)
        ).fetchone()

        if row is not None:
            last_size = row[0] or 0
            if current_size <= last_size:
                # サイズ変化なし → スキップ
                continue
            # ファイルが増えている → 差分を再処理
            is_update = True
        else:
            is_update = False

        messages = load_session_messages(filepath)
        chunks = build_chunks(messages)

        if not chunks:
            pass
        else:
            now = datetime.datetime.now().isoformat(timespec="seconds")
            for chunk in chunks:
                ts = chunk["timestamp"][:19].replace("T", " ") if chunk["timestamp"] else now
                # 重複チェック：同じcontentが既にあればスキップ
                exists = conn.execute(
                    "SELECT 1 FROM memories WHERE content = ?", (chunk["content"],)
                ).fetchone()
                if exists:
                    continue
                tokens = tokenize_ja(chunk["content"])
                if tokens:
                    unique_tokens = list(dict.fromkeys(tokens[:20]))
                    tags_str = "session,auto," + ",".join(unique_tokens)
                else:
                    tags_str = "session,auto"
                conn.execute(
                    "INSERT INTO memories (content, tags, type, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                    (chunk["content"], tags_str, "session", ts, now),
                )
                total_saved += 1
            conn.commit()

        # 処理済み記録を更新（INSERT OR REPLACE）
        conn.execute(
            "INSERT OR REPLACE INTO processed_sessions (session_file, processed_at, file_size) VALUES (?, ?, ?)",
            (basename, datetime.datetime.now().isoformat(timespec="seconds"), current_size),
        )
        conn.commit()

    if total_saved > 0:
        print(f"[reminiscence] 合計{total_saved}件保存しました。")
    else:
        print("[reminiscence] 新規保存なし（すべて処理済みまたは重複）")


def cmd_save(args, conn):
    now = datetime.datetime.now().isoformat(timespec="seconds")
    conn.execute(
        "INSERT INTO memories (content, tags, type, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
        (args.content, args.tags or "", args.type or "general", now, now),
    )
    conn.commit()
    print(f"[reminiscence] 保存しました（{now}）")


def cmd_search(args, conn):
    rows = conn.execute("""
        SELECT m.id, m.content, m.tags, m.type, m.created_at
        FROM memories_fts f
        JOIN memories m ON m.id = f.rowid
        WHERE memories_fts MATCH ?
        ORDER BY rank
        LIMIT ?
    """, (args.query, args.limit or 10)).fetchall()

    if not rows:
        print("[reminiscence] 該当する記憶が見つかりませんでした。")
        return

    print(f"[reminiscence] {len(rows)}件ヒット\n")
    for row in rows:
        print(f"── #{row['id']} [{row['type']}] {row['created_at']}")
        if row["tags"]:
            print(f"   タグ: {row['tags']}")
        print(f"   {row['content']}")
        print()


def cmd_list(args, conn):
    rows = conn.execute("""
        SELECT id, content, tags, type, created_at
        FROM memories
        ORDER BY created_at DESC
        LIMIT ?
    """, (args.limit or 20,)).fetchall()

    if not rows:
        print("[reminiscence] 記憶がまだありません。")
        return

    print(f"[reminiscence] 最新{len(rows)}件\n")
    for row in rows:
        print(f"── #{row['id']} [{row['type']}] {row['created_at']}")
        if row["tags"]:
            print(f"   タグ: {row['tags']}")
        print(f"   {row['content'][:120]}{'...' if len(row['content']) > 120 else ''}")
        print()


def cmd_delete(args, conn):
    conn.execute("DELETE FROM memories WHERE id = ?", (args.id,))
    conn.commit()
    print(f"[reminiscence] #{args.id} を削除しました。")


def cmd_retokenize(args, conn):
    """既存レコードの tags に Janome トークンを追加する（一回限りの遡及処理）"""
    rows = conn.execute(
        "SELECT id, content FROM memories WHERE tags = 'session,auto' OR tags = ''"
    ).fetchall()

    if not rows:
        print("[reminiscence] 遡及処理の対象レコードがありません。")
        return

    updated = 0
    now = datetime.datetime.now().isoformat(timespec="seconds")
    for row in rows:
        tokens = tokenize_ja(row["content"])
        if not tokens:
            continue
        unique_tokens = list(dict.fromkeys(tokens[:20]))
        new_tags = "session,auto," + ",".join(unique_tokens)
        conn.execute(
            "UPDATE memories SET tags = ?, updated_at = ? WHERE id = ?",
            (new_tags, now, row["id"])
        )
        updated += 1

    conn.commit()
    print(f"[reminiscence] {updated}件のレコードを遡及更新しました（対象: {len(rows)}件）。")


def cmd_digest(args, conn):
    """reminiscence DBからdocs/digest/に週次ダイジェストMarkdownを生成する"""
    import collections

    PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    DIGEST_DIR = os.path.join(PROJECT_ROOT, "docs", "digest")
    os.makedirs(DIGEST_DIR, exist_ok=True)

    days = getattr(args, 'days', 90)
    cutoff = (datetime.datetime.now() - datetime.timedelta(days=days)).isoformat(timespec="seconds")

    rows = conn.execute("""
        SELECT id, content, tags, created_at
        FROM memories
        WHERE created_at >= ?
        ORDER BY created_at ASC
    """, (cutoff,)).fetchall()

    if not rows:
        print("[digest] 対象レコードがありません。")
        return

    # ISO週でグループ化（例: 2026-W15）
    weeks = collections.defaultdict(list)
    for row in rows:
        try:
            dt = datetime.datetime.fromisoformat(row['created_at'])
            week_key = dt.strftime("%Y-W%W")
        except Exception:
            week_key = "unknown"
        weeks[week_key].append(row)

    generated = []
    for week_key in sorted(weeks.keys()):
        records = weeks[week_key]

        # 週の日付範囲
        dates = []
        for r in records:
            try:
                dates.append(datetime.datetime.fromisoformat(r['created_at']))
            except Exception:
                pass
        if dates:
            range_str = f"{min(dates).strftime('%Y-%m-%d')} 〜 {max(dates).strftime('%Y-%m-%d')}"
        else:
            range_str = week_key

        # 頻出トークン（上位10）— 記号・助動詞・超頻出語を除外
        STOPWORDS = {
            'する', 'いる', 'ある', 'なる', 'れる', 'られる', 'させる',
            'なっ', 'し', 'でき', 'くれ', 'もら', 'おり', 'いっ',
            'こと', 'もの', 'ため', 'よう', 'とき', 'あなた', 'これ', 'それ',
            'session', 'auto',
        }
        token_counter = collections.Counter()
        for r in records:
            for tag in (r['tags'] or '').split(','):
                tag = tag.strip()
                # ASCII記号・数字のみのトークンを除外、ストップワード除外
                if (tag
                        and tag not in STOPWORDS
                        and len(tag) >= 2
                        and not all(c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0123456789' for c in tag)):
                    token_counter[tag] += 1
        top_tokens = [t for t, _ in token_counter.most_common(10)]

        # 日別グループ
        day_groups = collections.defaultdict(list)
        for r in records:
            try:
                day_key = datetime.datetime.fromisoformat(r['created_at']).strftime("%Y-%m-%d")
            except Exception:
                day_key = "unknown"
            day_groups[day_key].append(r)

        lines = [
            f"# Digest: {week_key} ({range_str})",
            "",
            f"**レコード数:** {len(records)}件",
        ]
        if top_tokens:
            lines.append(f"**頻出キーワード:** {', '.join(top_tokens)}")
        lines += ["", "---", ""]

        for day_key in sorted(day_groups.keys()):
            lines.append(f"## {day_key}")
            lines.append("")
            for r in day_groups[day_key]:
                ts = r['created_at'][:16]
                lines.append(f"[{ts}]")
                lines.append(r['content'])
                lines.append("")

        filepath = os.path.join(DIGEST_DIR, f"{week_key}.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        generated.append(week_key)

    # _index.md 更新
    index_lines = [
        "# docs/digest インデックス",
        "",
        "reminiscence DB から自動生成された週次ダイジェスト。エージェントの知識参照先。",
        "",
    ]
    for week_key in sorted(generated, reverse=True):
        index_lines.append(f"- [{week_key}]({week_key}.md)")

    with open(os.path.join(DIGEST_DIR, "_index.md"), 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_lines))

    print(f"[digest] {len(generated)}週分のダイジェストを生成しました → docs/digest/")


def cmd_inject(args, conn):
    """UserPromptSubmit フック用: stdinからhookイベントを読み、関連記憶をadditionalContextとして返す"""
    LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inject.log")

    try:
        event = json.loads(sys.stdin.read())
    except Exception:
        print("{}")
        return

    prompt = event.get("prompt", "")
    if not prompt or len(prompt.strip()) < 5:
        print("{}")
        return

    # 形態素解析でキーワード抽出、なければ先頭100文字をそのまま使用
    raw_query = prompt.strip()[:200]
    tokens = tokenize_ja(raw_query)
    if tokens:
        # FTS5 の OR 検索で複数キーワードをマッチ
        query = " OR ".join(f'"{t}"' for t in tokens[:10])
    else:
        query = raw_query[:100]

    cutoff = (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat(timespec="seconds")
    search_all = getattr(args, 'all', False)

    try:
        if search_all:
            rows = conn.execute("""
                SELECT m.id, m.content, m.created_at
                FROM memories_fts f
                JOIN memories m ON m.id = f.rowid
                WHERE memories_fts MATCH ?
                ORDER BY rank
                LIMIT ?
            """, (query, args.limit or 5)).fetchall()
        else:
            rows = conn.execute("""
                SELECT m.id, m.content, m.created_at
                FROM memories_fts f
                JOIN memories m ON m.id = f.rowid
                WHERE memories_fts MATCH ?
                  AND m.created_at >= ?
                ORDER BY rank
                LIMIT ?
            """, (query, cutoff, args.limit or 5)).fetchall()
    except Exception:
        rows = []

    # 7日以内にヒットなし → 古いデータにあるか確認
    old_count = 0
    if not rows and not search_all:
        try:
            old_count = conn.execute("""
                SELECT COUNT(*) FROM memories_fts f
                JOIN memories m ON m.id = f.rowid
                WHERE memories_fts MATCH ?
                  AND m.created_at < ?
            """, (query, cutoff)).fetchone()[0]
        except Exception:
            old_count = 0

    # ログ記録
    now = datetime.datetime.now().isoformat(timespec="seconds")
    total_chars = sum(len(r["content"]) for r in rows)
    with open(LOG_PATH, "a", encoding="utf-8") as lf:
        lf.write(f"{now} | hits={len(rows)} | old={old_count} | chars={total_chars} | query={query[:50]}\n")

    if not rows and old_count == 0:
        print("{}")
        return

    if not rows and old_count > 0:
        context = (
            f"📦 [reminiscence] 7日以内の関連記憶はありません。"
            f"古いデータに{old_count}件の関連記憶があります。"
            f"参照が必要であれば明示してください。"
        )
    else:
        lines = ["## reminiscence: 関連する過去の記憶（7日以内）\n"]
        for row in rows:
            lines.append(f"[{row['created_at']}]\n{row['content']}\n")
        context = "\n".join(lines)

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context
        }
    }
    print(json.dumps(output, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="reminiscence — Seep Logos 長期記憶システム")
    sub = parser.add_subparsers(dest="command")

    # process-session（自動保存）
    p_ps = sub.add_parser("process-session", help="最新セッションを自動でQ&Aチャンク保存する")
    p_ps.add_argument("--project-dir", help="対象のClaudeプロジェクトディレクトリ（省略時はデフォルト）")

    # save（手動保存）
    p_save = sub.add_parser("save", help="記憶を手動保存する")
    p_save.add_argument("content", help="保存する内容")
    p_save.add_argument("--tags", help="タグ（カンマ区切り）例: feedback,sns")
    p_save.add_argument("--type", help="種別: feedback / project / user / reference / general", default="general")

    # search
    p_search = sub.add_parser("search", help="記憶を検索する")
    p_search.add_argument("query", help="検索キーワード")
    p_search.add_argument("--limit", type=int, default=10, help="最大取得件数")

    # list
    p_list = sub.add_parser("list", help="最近の記憶を一覧表示する")
    p_list.add_argument("--limit", type=int, default=20, help="最大取得件数")

    # delete
    p_delete = sub.add_parser("delete", help="記憶をIDで削除する")
    p_delete.add_argument("id", type=int, help="削除するメモリID")

    # retokenize（一回限りの遡及処理）
    sub.add_parser("retokenize", help="既存レコードのtagsにJanomeトークンを追加する（一回限りの遡及処理）")

    # digest（docs/digest/へのMarkdown生成）
    p_digest = sub.add_parser("digest", help="DBからdocs/digest/に週次ダイジェストを生成する")
    p_digest.add_argument("--days", type=int, default=90, help="対象期間（日数、デフォルト90日）")

    # inject（UserPromptSubmitフック用）
    p_inject = sub.add_parser("inject", help="UserPromptSubmitフック: 関連記憶をadditionalContextとして返す")
    p_inject.add_argument("--limit", type=int, default=5, help="最大取得件数")
    p_inject.add_argument("--all", action="store_true", help="7日以上前の記憶も含めて検索する")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    conn = get_connection()
    init_db(conn)

    if args.command == "process-session":
        cmd_process_session(args, conn)
    elif args.command == "save":
        cmd_save(args, conn)
    elif args.command == "search":
        cmd_search(args, conn)
    elif args.command == "list":
        cmd_list(args, conn)
    elif args.command == "delete":
        cmd_delete(args, conn)
    elif args.command == "retokenize":
        cmd_retokenize(args, conn)
    elif args.command == "digest":
        cmd_digest(args, conn)
    elif args.command == "inject":
        cmd_inject(args, conn)

    conn.close()


if __name__ == "__main__":
    main()
