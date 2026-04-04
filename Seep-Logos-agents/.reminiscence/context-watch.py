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
WARN_THRESHOLD = 20   # 注意（そろそろ長い）
ALERT_THRESHOLD = 35  # 強い警告（分断リスク高）


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

    if turns >= ALERT_THRESHOLD:
        message = (
            f"⚠️ [context-watch] 会話が{turns}ターンに達しています。"
            "コンテキスト圧縮による分断リスクが高い状態です。"
            "現在のトピックの決定事項を書記（recorder）に記録することを強く推奨します。"
        )
    elif turns >= WARN_THRESHOLD:
        message = (
            f"📝 [context-watch] 会話が{turns}ターンになっています。"
            "節目のトピックが完了していれば、書記（recorder）に記録しておくと安全です。"
        )
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
