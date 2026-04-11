#!/usr/bin/env python3
"""
context-watch — セッションコンテキスト長さ監視フック
UserPromptSubmit 時にセッションファイルのサイズを確認し、
長くなってきたら警告を additionalContext として返す。
"""

import json
import os
import sys

PROJECT_CLAUDE_DIR = os.path.expanduser(
    "~/.claude/projects/-Users-matsuura-hisashi-com-Seep-Logos-agents"
)

# ユーザー発言ターン数の警告閾値
WARN_THRESHOLD = 35   # 注意（そろそろ長い）
ALERT_THRESHOLD = 55  # 強い警告（分断リスク高）

# 警告済み状態を記録するファイル
WARNED_STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".context-watch-state")


def count_user_turns(session_file):
    count = 0
    try:
        with open(session_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    if obj.get("type") == "user":
                        count += 1
                except json.JSONDecodeError:
                    continue
    except OSError:
        pass
    return count


def load_warned_state(session_id):
    """セッションごとの警告済みレベルを読み込む"""
    try:
        with open(WARNED_STATE_FILE, encoding="utf-8") as f:
            state = json.load(f)
        return state.get(session_id, 0)
    except Exception:
        return 0


def save_warned_state(session_id, level):
    """セッションごとの警告済みレベルを保存する"""
    try:
        try:
            with open(WARNED_STATE_FILE, encoding="utf-8") as f:
                state = json.load(f)
        except Exception:
            state = {}
        state[session_id] = level
        with open(WARNED_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False)
    except Exception:
        pass


def main():
    try:
        event = json.loads(sys.stdin.read())
    except Exception:
        print("{}")
        return

    session_id = event.get("session_id", "")
    if not session_id:
        print("{}")
        return

    session_file = os.path.join(PROJECT_CLAUDE_DIR, f"{session_id}.jsonl")
    if not os.path.exists(session_file):
        print("{}")
        return

    turns = count_user_turns(session_file)
    warned_level = load_warned_state(session_id)

    if turns >= ALERT_THRESHOLD and warned_level < 2:
        message = (
            f"⚠️ [context-watch] 会話が{turns}ターンに達しています。"
            "コンテキスト圧縮による分断リスクが高い状態です。"
            "現在のトピックの決定事項を書記（recorder）に記録することを強く推奨します。"
        )
        save_warned_state(session_id, 2)
    elif turns >= WARN_THRESHOLD and warned_level < 1:
        message = (
            f"📝 [context-watch] 会話が{turns}ターンになっています。"
            "節目のトピックが完了していれば、書記（recorder）に記録しておくと安全です。"
        )
        save_warned_state(session_id, 1)
    else:
        print("{}")
        return

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": message,
        }
    }
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
