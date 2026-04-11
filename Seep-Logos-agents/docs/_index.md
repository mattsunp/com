# docs/ インデックス

> Seep Logos エージェント司令塔の詳細ドキュメント一覧。
> 各ファイルは必要に応じて参照する。最終更新: 2026-04-04

---

| ファイル | 内容 |
|---|---|
| `docs/brand-rules.md` | ブランドルール・SNS分離原則・世界観扱い方 |
| `docs/output-format.md` | 出力フォーマット標準・recorder仕様 |
| `docs/copyright-policy.md` | 著作物利用ポリシー |
| `docs/orchestration-spec.md` | オーケストレーション実験仕様・実験履歴 |
| `docs/visual-style-guide.md` | Web ビジュアルスタイルガイド（16パターン、パターン選定ガイド） |
| `docs/web-designer-manual.md` | Webデザイナー業務マニュアル（DESIGN.md 作成・ワークフロー・チェックリスト） |
| `docs/agent-genius-design.md` | エージェント天才化設計マニュアル・進捗管理 |
| `docs/glossary.md` | 用語集・辞書（定義・調査済みの言葉を随時蓄積） |
| `docs/orchestration-queue-schema.md` | オーケストレーションキュースキーマ定義 |

## ダイジェスト・状態管理

| ファイル | 内容 |
|---|---|
| `docs/digest/_index.md` | 週次ダイジェスト一覧（Stop フックで自動生成） |
| `docs/digest/_system-state.md` | 確認済みの設定・稼働状態の宣言 |
| `docs/digest/YYYY-Www.md` | 各週の構造化ダイジェスト（過去の決定事項・設定変更） |

---

## 記録・記憶システムの役割分担

```
【生ソース層】.reminiscence/memory.db
  全セッションの Q&A を全文・自動蓄積（変更不可）
  UserPromptSubmit フックで自動取込（process-session）
  関連記憶をセッション開始時に自動注入（inject）
        ↓ セッション終了時（Stop フック）
【ダイジェスト層】docs/digest/YYYY-Www.md
  週次で決定事項・設定変更・固有名詞を抽出
  エージェントの高速参照先
  _system-state.md に「今の状態」を宣言
        ↓ 手動トリガー or context-watch 警告時
【議事録層】minutes/YYYY-MM-DD_*.md
  人間向け構造化アーカイブ
  決定事項・未解決課題・文脈の理由を保持
  Claude が能動的に参照する補完資料
```

| レイヤー | 場所 | 稼働 | 読者 |
|---|---|---|---|
| 生ソース | `.reminiscence/memory.db` | 全自動 | Claude（inject 経由） |
| ダイジェスト | `docs/digest/` | Stop 時自動 | Claude（参照）・人間 |
| 議事録 | `minutes/` | 手動 | 人間・Claude（補完） |

---

## エージェント・スキル定義

| 場所 | 内容 |
|---|---|
| `.claude/agents/` | 各エージェントの愛称・性格・口調・指針 |
| `.claude/skills/` | 各スキルの実行マニュアル（例：`web-production.md`） |
