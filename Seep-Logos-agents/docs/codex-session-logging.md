# Codex Session Logging

> 対象: Codex / ChatGPT セッションの全文保全
> 保存先: `.reminiscence-cod/`
> 最終更新: 2026-04-12

---

## 1. この文書の目的

この文書は、Codex との会話セッションを**要約ではなく全文**で保存し続けるための運用ルールを定める。

Seep Logos では、長期継続性を AI の内部記憶だけに依存させない。
そのため、Codex 側の会話もリポジトリ内に外部記憶として保持する。

---

## 2. 位置づけ

`.reminiscence-cod/` は、Codex 系セッションの全文記録の原本置き場である。

役割分担は以下とする。

- `.reminiscence/`: Claude 系の全文記憶の原本
- `.reminiscence-cod/`: Codex 系の全文記録の原本
- `docs/digest/`: AI が高速参照する状態整理レイヤー
- `minutes/`: 人間向けの議事録レイヤー

Codex の作業内容は、必要に応じて `.reminiscence-cod/` から `docs/digest/` と `minutes/` に接続する。

---

## 3. 保存単位

全文記録は **1セッション1ファイル** を原則とする。

形式は YAML とし、以下を同一ファイル内に保持する。

- セッション識別子
- 開始・終了時刻
- 議題
- メッセージ全文
- 作成・更新した成果物
- handoff 情報

追記のしやすさより、**再読性と保全性**を優先する。

---

## 4. ファイル命名規則

保存先:

```text
.reminiscence-cod/sessions/YYYY-MM-DD_HH-MM_[topic].yaml
```

例:

```text
.reminiscence-cod/sessions/2026-04-12_19-11_codex-session-logging.yaml
```

ルール:

- 日付と時刻はセッション開始時刻を使う
- `[topic]` は英数字とハイフン中心で短く付ける
- 同一トピックでも開始時刻が違えば別ファイルとする

---

## 5. 必須項目

各 YAML には最低限以下を含める。

- `session_id`
- `agent`
- `project`
- `started_at`
- `topic`
- `messages`

推奨項目:

- `ended_at`
- `tags`
- `artifacts`
- `handoff`
- `notes`

---

## 6. messages のルール

`messages` には、セッション内の会話を時系列順に**全文そのまま**保持する。

各メッセージは以下のキーを持つ。

- `role`: `user` / `assistant`
- `ts`: タイムスタンプ
- `content`: 発話全文

必要なら補助キーとして以下を追加してよい。

- `kind`: `message` / `summary` / `system-note`
- `attachments`

ただし、正本はあくまで会話の全文である。
後処理用の要約が必要でも、全文を置き換えてはならない。

---

## 7. artifacts のルール

ファイル作成・更新・レビューなど、セッションで扱った成果物は `artifacts` に記録する。

例:

- `path`
- `kind`
- `status`

これにより、後から「どの会話でどの成果物が生まれたか」を辿りやすくする。

---

## 8. handoff のルール

セッション終了時に `Claude Code` へ戻す必要がある場合、`handoff` セクションを記録する。

最低限の推奨項目:

- `needed`
- `target`
- `summary`

必要に応じて `docs/handoff-protocol.md` の構造をそのまま転記してよい。

---

## 9. 運用原則

- YAML は人間と AI の両方が読めることを重視する
- 会話の全文は削らない
- 要約は補助情報として追加してよいが、原文の代替にしない
- `.reminiscence-cod/` は正本なので、後から整形目的で内容を書き換えすぎない
- 意思決定や運用変更が発生した場合は、必要に応じて `docs/digest/` や `minutes/` にも反映する

---

## 10. 実務上の使い分け

使い分けの目安は以下とする。

- 会話全文を保存したい: `.reminiscence-cod/`
- AI が今の状態を速く読みたい: `docs/digest/`
- 人間が経緯や理由を読みたい: `minutes/`

`.reminiscence-cod/` は「読むための最短距離」ではなく、
**失われない原本を保つための場所**
として扱う。
