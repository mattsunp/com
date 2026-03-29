# 自動ルーティングルール

```
ユーザーからの指示 → 単体 or 複数エージェント？ → エージェント起動
```

**単体エージェントで完結するタスク：** 該当エージェントを直接起動する。
**複数エージェントの連携が必要なタスク：** orchestrator（指揮者）を起動し、編成・進行を委ねる。

## orchestratorを起動する目安

- 2つ以上の専門領域をまたぐ成果物が必要なとき
- 相互批評・段階的精緻化（複数ラウンド）が必要なとき
- どのエージェントを呼ぶか自分で判断したくないとき

## 複合タスク例（orchestrator経由）

- 新規ゲームIP立案 → orchestrator → chief-producer × game-director × worldbuilding-creator × scenario-writer × planning-developer
- 新IP発表のプレスリリース → orchestrator → pr-communications × press-release-writer × sns-manager
- 海外ローカライズ → orchestrator → localization-director × localization-specialist × cultural-adaptation
- 外部クライアント提案 → orchestrator → sales-director × project-manager

## 優先度ルール

1. 外部公開コンテンツは必ずブランドルールチェック（→ `docs/brand-rules.md`）
2. 未発表情報を含む場合は機密フラグを立てて出力に注記
3. orchestratorが編成した場合、orchestratorが統合・進行責任を持つ
