# Claude Codeへの引き継ぎ：Seep-Logos-agents × ECC移行作業

## あなたへのお願い

このファイルを読んだら、以下の作業を順番通りに進めてください。
判断が必要な箇所には `【要確認】` と書いてあります。その都度ユーザーに聞いてください。

---

## 現状の把握

```
com/
└── Seep-Logos-agents/        ← 仮想一企業として運用中のリポジトリ
    ├── CLAUDE.md             ← 会社コンテキスト・ミッション・ルール記述あり
    └── agents/               ← 専門分野別のカスタムエージェント複数あり
```

- 個人運用（自分だけが使う）
- それなりに作り込んであるが、バックアップすれば中身は入れ替えてよい
- 「Seep-Logos-agents」という名前・器はそのまま使い続けたい

---

## 移行方針

**ECCをプラグインとして導入し、Seep-Logos-agentsを作り直す。**

- ECC（everything-claude-code）はリポジトリ内にファイルを置かず、プラグインとして外から読み込む
- Seep-Logosの独自資産（会社コンテキスト・一部エージェント）は選別して戻す
- 結果として「Seep-Logosというアイデンティティを持ちつつ、ECCの28エージェント+119スキルを使える会社」になる

---

## 作業手順

### Step 0: バックアップ

```bash
cd com
cp -r Seep-Logos-agents Seep-Logos-agents-backup-$(date +%Y%m%d)
```

バックアップが作成されたことを確認してから次へ。

---

### Step 1: Seep-Logos-agentsを空にする

以下を削除（バックアップ済みなので安全）：

```bash
cd com/Seep-Logos-agents
rm -rf agents/
rm -f CLAUDE.md
# .gitは残す。他に独自ファイルがあれば【要確認】
```

【要確認】削除前に `ls -la` でディレクトリ構造を確認し、上記以外に残すべきファイルがないかユーザーに聞く。

---

### Step 2: ECCをインストール

Seep-Logos-agentsディレクトリでClaude Codeを起動した状態で：

```
/plugin marketplace add affaan-m/everything-claude-code
/plugin install everything-claude-code@everything-claude-code
```

インストール後、`.claude/settings.json` にトークン最適化設定を追加：

```json
{
  "model": "sonnet",
  "env": {
    "MAX_THINKING_TOKENS": "10000",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
  }
}
```

---

### Step 3: ECCのrulesをコピー

```bash
git clone https://github.com/affaan-m/everything-claude-code.git /tmp/ecc
mkdir -p com/Seep-Logos-agents/.claude/rules
cp -r /tmp/ecc/rules/common/* com/Seep-Logos-agents/.claude/rules/
```

【要確認】使用言語を確認し、該当するものも追加する。
例：TypeScriptなら `cp -r /tmp/ecc/rules/typescript/* com/Seep-Logos-agents/.claude/rules/`

---

### Step 4: CLAUDE.mdを先に復元する（重要）

**この手順は agents/ より先にやること。**
会社コンテキストのない状態でClaude Codeを使い始めないようにするため。

バックアップから旧CLAUDE.mdを参照し、以下の要素を新CLAUDE.mdとして書き直す：

**残すもの（バックアップから持ってくる）：**
- 会社名・ミッション・ビジョン
- Seep-Logos固有のコンテキスト・背景
- 独自のルール・制約

**追加するもの（新規）：**

```markdown
## エージェント運用方針
このリポジトリではECCプラグインのエージェントを活用する。
- 計画立案 → `/plan`
- コードレビュー → `code-reviewer` エージェント
- セキュリティ確認 → `security-reviewer` エージェント
- ビルドエラー修正 → `build-error-resolver` エージェント

## Seep-Logos独自エージェント
（Step 5で復元したエージェントをここに記載する）
```

【要確認】旧CLAUDE.mdの内容をユーザーと一緒に確認し、残す・捨てる・書き直すを判断する。

---

### Step 5: agents/を仕分けして戻す

バックアップの `agents/` を一覧表示し、以下の基準で仕分けする：

| 判断 | 基準 |
|---|---|
| **削除**（ECCに任せる） | ECCに同等のエージェントが既にある |
| **残す** | Seep-Logos固有の文脈・知識・世界観を持つ |
| **削除**（整理） | 役割が曖昧、またはほぼ使っていない |

ECCに含まれる主なエージェント（これらと重複するものは削除候補）：
`planner`, `architect`, `code-reviewer`, `security-reviewer`, `tdd-guide`,
`build-error-resolver`, `e2e-runner`, `refactor-cleaner`, `doc-updater`

【要確認】各エージェントファイルの内容をユーザーに見せながら、残す・削除を一つずつ確認する。

残すと判断したものだけをコピー：

```bash
cp com/Seep-Logos-agents-backup-YYYYMMDD/agents/残すもの.md \
   com/Seep-Logos-agents/agents/
```

---

### Step 6: 動作確認

```
/plugin list everything-claude-code@everything-claude-code
```

ECCのエージェント・コマンド・スキルが一覧表示されれば完了。

試しに以下を実行してみる：
```
/plan "Seep-Logosの最初のタスク"
```

---

## 完了後の構成イメージ

```
com/
├── Seep-Logos-agents-backup-YYYYMMDD/   ← 旧データ（しばらく残しておく）
└── Seep-Logos-agents/
    ├── CLAUDE.md                         ← Seep-Logos独自コンテキスト
    ├── .claude/
    │   ├── settings.json                 ← ECCプラグイン有効化 + トークン最適化
    │   └── rules/                        ← ECC commonルール + 独自ルール
    └── agents/                           ← 仕分け済みの独自エージェントのみ
    # ECCの28エージェント・119スキル・60コマンドはプラグインで自動ロード
```

---

## 注意事項

- バックアップは移行完了後も**1〜2週間は削除しないこと**
- ECCのアップデートは `/plugin update everything-claude-code@everything-claude-code` で行う
- 困ったときは `npx ecc-agentshield scan` でセキュリティ・設定の問題を確認できる
