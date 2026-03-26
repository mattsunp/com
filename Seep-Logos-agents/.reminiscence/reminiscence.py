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
    """最新セッションを読み込んでQ&Aチャンクとして自動保存"""
    project_dir = args.project_dir or PROJECT_CLAUDE_DIR

    # トップレベルの .jsonl のみ対象（サブエージェントのものは除外）
    files = [
        f for f in glob.glob(os.path.join(project_dir, "*.jsonl"))
        if os.path.isfile(f)
    ]
    if not files:
        print("[reminiscence] セッションファイルが見つかりません。")
        return

    latest = max(files, key=os.path.getmtime)
    basename = os.path.basename(latest)

    # 既処理チェック
    already = conn.execute(
        "SELECT 1 FROM processed_sessions WHERE session_file = ?", (basename,)
    ).fetchone()
    if already:
        print(f"[reminiscence] 既処理: {basename}")
        return

    messages = load_session_messages(latest)
    chunks = build_chunks(messages)

    if not chunks:
        print(f"[reminiscence] 保存対象なし: {basename}")
    else:
        now = datetime.datetime.now().isoformat(timespec="seconds")
        for chunk in chunks:
            ts = chunk["timestamp"][:19].replace("T", " ") if chunk["timestamp"] else now
            conn.execute(
                "INSERT INTO memories (content, tags, type, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                (chunk["content"], "session,auto", "session", ts, now),
            )
        conn.commit()
        print(f"[reminiscence] {len(chunks)}件保存しました: {basename}")

    # 処理済みとして記録
    conn.execute(
        "INSERT INTO processed_sessions (session_file, processed_at) VALUES (?, ?)",
        (basename, datetime.datetime.now().isoformat(timespec="seconds")),
    )
    conn.commit()


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

    conn.close()


if __name__ == "__main__":
    main()
