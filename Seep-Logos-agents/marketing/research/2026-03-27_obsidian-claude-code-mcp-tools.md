# Obsidian × Claude Code MCP統合ツール 調査レポート

## 調査概要

- **調査目的**: Obsidian と Claude Code CLI を統合する主要ツール4種の機能・安定性・互換性の把握
- **調査対象**:
  1. obsidian-claude-code-mcp（iansinnott）
  2. MCPVault（@bitbonsai/mcpvault）
  3. Claudian（YishenTu）
  4. Claude Desktop + MCP サーバー経由のObsidian連携
- **調査日**: 2026-03-27
- **情報ソース**: 各GitHubリポジトリ、Obsidian Forum、npm、DeepWiki、XDA Developers、ユーザーレビュー記事
- **注記**: 一部データ（スター数等）は調査時点のスナップショット。最新情報は各リポジトリを直接参照のこと。

---

## ツール別詳細分析

---

### ツール 1: obsidian-claude-code-mcp（iansinnott）

**リポジトリ**: https://github.com/iansinnott/obsidian-claude-code-mcp

#### 基本指標

| 項目 | 値 |
|---|---|
| GitHub スター数 | 206 |
| フォーク数 | 25 |
| 最新バージョン | 1.1.8 |
| 最終リリース日 | 2025年6月23日 |
| ライセンス | 記載なし（TypeScript製） |
| オープンissue数 | 6件 |

#### 位置づけ

Obsidianプラグインとして動作するMCPサーバー実装。Claude Code CLIとの接続を**主目的として設計された唯一のツール**。デュアルトランスポート（WebSocket + HTTP/SSE）で、Claude Code CLIとClaude Desktopの両方に対応する。

#### Claude Code CLI との互換性

**対応: 明示的にサポート**

接続手順は以下の通り：
1. Obsidianにプラグインをインストール（Community Plugins経由）
2. 設定でMCPサーバーを有効化（デフォルトポート: 22360）
3. ターミナルで `claude` を起動
4. Claude Code内で `/ide` コマンドを実行
5. リストから "Obsidian" を選択 → WebSocket経由で自動接続

WebSocketトランスポートがClaude Code CLI専用に設計されており、HTTPトランスポート（Claude Desktop向け）と並走する。ロックファイル（`~/.config/claude/ide/[port].lock`）を使った自動ディスカバリー機能により、手動設定なしで接続が確立する。

#### 導入手順

```
1. Obsidian → Settings → Community Plugins → Browse
2. "Claude Code MCP" を検索・インストール
3. プラグイン設定でサーバー起動を確認（Status: Running）
4. ターミナル: claude → /ide → Obsidian を選択
```

Claude Desktop向けに別途 `mcp-remote` ブリッジが必要（`claude_desktop_config.json` に設定）。

#### できること

- Vaultファイルの読み取り・書き込み（MCP経由）
- 現在アクティブなファイルのコンテキスト取得（`get_current_file`）
- ワークスペース構造の参照
- Claude Code と Claude Desktop の同時接続（マルチクライアント）
- 複数Vault運用（ポートを変えて並走）

#### できないこと / 既知の制限

- Windows環境で埋め込みターミナル入力が機能しない（Issue #10 未解決）
- IDE固有ツール（diff表示、タブ管理等）はスタブ実装のみ（動作しない）
- 最新MCPプロトコル（Streamable HTTP、2025-03-26仕様）は未対応。旧仕様（2024-11-05）を意図的に使用
- Vault外ディレクトリへのアクセス制限あり（Issue #3）
- WebSocket/HTTPサーバーが任意originからの接続を受け付けるCORSセキュリティ問題あり（Issue #12、2026年3月報告・未解決）

#### トークン消費への影響

公式ドキュメントに明示なし。ツールアーキテクチャ上、Vault全体をコンテキストに入れるのではなく**ファイル単位のリクエスト応答型**。ただし大規模Vault（4,000ノート超）での性能劣化はユーザーから報告あり。

#### 安定性評価

メンテナンス状況: 最終リリースが2025年6月で約9ヶ月更新なし（2026年3月時点）。オープンissueへのレスポンスは限定的。セキュリティ問題（Issue #12）が未対処である点は留意が必要。

---

### ツール 2: MCPVault（@bitbonsai/mcpvault）

**リポジトリ**: https://github.com/bitbonsai/mcpvault
**npm**: `@bitbonsai/mcpvault`

#### 基本指標

| 項目 | 値 |
|---|---|
| GitHub スター数 | 971 |
| フォーク数 | 71 |
| 最新バージョン | 0.11.0 |
| 最終リリース日 | 2026年3月22日 |
| コミット数 | 197 |
| オープンissue | 確認中 |

#### 位置づけ

Obsidianプラグインではなく、**スタンドアロンのMCPサーバー**（Node.jsプロセス）。Obsidianアプリは不要で、Vaultディレクトリに直接アクセスする。Claude Code CLI、Claude Desktop、Cursor、Gemini CLI等あらゆるMCPクライアントに対応する「ユニバーサル型」設計。

#### Claude Code CLI との互換性

**対応: 明示的にサポート（設定例あり）**

Claude Code CLIへの追加コマンド（公式ドキュメント記載）:
```bash
claude mcp add obsidian --scope user npx @bitbonsai/mcpvault /path/to/vault
```

または `~/.claude.json` に直接記述:
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["@bitbonsai/mcpvault@latest", "/path/to/your/vault"]
    }
  }
}
```

#### 導入手順

```bash
# 即時起動（インストール不要）
npx @bitbonsai/mcpvault@latest /path/to/vault

# Claude Code CLIへの永続登録
claude mcp add obsidian --scope user npx @bitbonsai/mcpvault /path/to/vault
```

Node.js v20以上が必要（v18はEOLにより2026年3月版よりサポート外）。

#### できること

- ノートの読み取り・書き込み・パッチ適用・削除・移動
- ディレクトリ構造の探索
- BM25関連度再ランキングによる全文検索
- YAMLフロントマターの安全な読み取り・更新（フロントマター破損防止機能あり）
- バッチ処理（複数ノートの一括操作）
- タグの追加・削除・一覧（`list_all_tags` ツール：v0.11.0で追加）
- 書き込みモード3種（上書き・追記・先頭挿入）
- Vault統計情報の取得
- `.base`、`.canvas`等のObsidian独自形式対応（v0.8.2以降）

#### できないこと / 既知の制限

- Vault外ディレクトリへのアクセス不可（パストラバーサル対策）
- `.obsidian/` システムディレクトリは自動除外
- Obsidianアプリ自体との連携なし（プラグインではないため、アクティブファイルの取得等は不可）
- 削除操作には明示的な確認が必要

#### トークン消費への影響

**積極的に最適化されている点が差別化要素**。v0.6.3以降、フィールド名の短縮とコンパクトJSON形式により「レスポンスサイズを40〜60%削減」とドキュメントに明記。Vault全体をコンテキストに入れるのではなく**検索・リクエストベースのアクセス**。デバッグ時は `prettyPrint: true` で可読形式に切り替え可能。

#### 安定性評価

4つの中で**最も活発なメンテナンス状況**。2026年3月だけでv0.9.0〜v0.11.0の複数バージョンをリリース。Obsidianからの要請でパッケージ名変更（`mcpvault` → `@bitbonsai/mcpvault`）に対応済み。セキュリティ強化（シンボリックリンク脱出防止、TOCTOU対策）も継続的に実施。

---

### ツール 3: Claudian（YishenTu）

**リポジトリ**: https://github.com/YishenTu/claudian

#### 基本指標

| 項目 | 値 |
|---|---|
| GitHub スター数 | 5,300以上（「4,500スター」報告後さらに増加） |
| 最新バージョン | 1.3.72 |
| 最終リリース日 | 2026年3月26日 |
| コミット数 | 527（mainブランチ） |
| ライセンス | MIT |
| オープンissue | 多数（400番台のissueが存在） |

#### 位置づけ

前述3つとは根本的に異なるアプローチ。**ObsidianプラグインがClaude Code CLIプロセスをObsidian内に直接ホスト**する設計。MCPサーバーではなく、Claude Code CLIのサブプロセスをObsidianのサイドバーに埋め込む。「VaultをClaude Codeの作業ディレクトリにする」という思想。

#### Claude Code CLI との互換性

**Claude Code CLIが必須前提**（これ自体がCLIのラッパー）

Claudianは以下を前提とする:
- Claude Code CLIがローカルインストール済み（`claude` コマンドが使える状態）
- Obsidian v1.8.9以上
- macOS / Linux / Windows（デスクトップのみ、モバイル不可）

CLIをターミナルで使う場合との違いは「Obsidianのサイドバー内で動作する」という点のみ。underlying engineはCLIそのもの。

#### 導入手順

公式インストーラー未対応（Obsidianコミュニティプラグイン一覧に非掲載）。以下の手順が必要:

```
1. GitHub Releases から main.js / manifest.json / styles.css をダウンロード
2. Vault/.obsidian/plugins/claudian/ フォルダを作成してファイルを配置
3. Obsidian → Settings → Community Plugins → Claudian を有効化
4. または BRAT プラグインマネージャー経由でインストール
```

#### できること

- VaultをClaude Codeの作業ディレクトリとして完全に活用（ファイル読み書き・検索・bashコマンド実行）
- Obsidianサイドバーで対話（ターミナルを別途開かずに済む）
- フォーカス中のノートを自動アタッチ
- `@ファイル名` でノートをメンション
- ドラッグ&ドロップ・ペーストによる画像解析（Vision対応）
- 単語レベルのdiff表示付きインライン編集
- スラッシュコマンドによる再利用可能なプロンプトテンプレート
- Plan モード（実行前に設計を確認）
- Claude Code プラグイン・MCPサーバーの利用（CLI経由で設定済みのものを引き継ぎ）
- モデル選択（Haiku / Sonnet / Opus、1M contextウィンドウ対応）

#### できないこと / 既知の制限

- Obsidian公式コミュニティプラグイン一覧には未掲載（手動インストール必須）
- モバイル非対応
- Claude Code CLIのAnthropicサブスクリプションまたはAPIキーが必須
- 多数のissue報告あり（後述）

#### トークン消費への影響

Claude Code CLIを直接実行するため、**通常のCLI使用と同等のトークン消費**が発生する。Vault全体をコンテキストに入れるのではなく、Claude Codeのツール呼び出し（ファイル読み取り等）ごとにトークンを消費する構造。コスト節約の工夫としてAPIエンドポイントのカスタム設定が可能（環境変数 `ANTHROPIC_BASE_URL` で代替プロバイダーも利用可）。

#### 安定性評価

**頻繁な更新と多数の未解決issueが共存している状況**。

確認されている主な問題:
- AbortSignal / EventEmitter エラー（複数のissueで報告・一部修正済み）
- API 502エラー（バージョン更新後に発生、Issue #397）
- レート制限エラーの解消しない問題（Issue #408）
- セッション切り替え時のハング（Issue #335）
- UI表示とActual設定の不一致（Issue #389）

開発ペースは非常に速い（2026年3月だけで1.3.xx系のマイナーアップデートを連続リリース）が、安定性よりも機能追加が優先されている印象。スター数5,300超は人気の証明だが、プロダクション用途には検証が必要。

---

### ツール 4: Claude Desktop + MCP サーバー経由のObsidian連携

#### 位置づけ

「Claude Desktop」アプリ（gui版）を使い、MCP経由でObsidianのVaultにアクセスするパターン。**これはClaude Code CLIとは別物**であり、Claude Code CLIとの連携を求める場合には該当しない。

代表的なMCPサーバー実装:
- `MarkusPfundstein/mcp-obsidian`（Obsidian Local REST API プラグインを仲介）
- `StevenStavrakis/obsidian-mcp`
- `cyanheads/obsidian-mcp-server`

#### Claude Code CLI との互換性

**直接の互換性なし**

Claude Desktop（GUI）向けの設計。MCP設定ファイルは `claude_desktop_config.json`（Claude Code CLIの `~/.claude.json` とは別）。

ただし、`@bitbonsai/mcpvault` 等のスタンドアロンMCPサーバーは、Claude Code CLIの `~/.claude.json` にも追記可能であるため、「MCPサーバー」自体はCLIと共用できる。Claude Desktopアプリそのものがターミナルでの `claude` コマンドに置き換わることはない。

#### 代表的な導入手順（MarkusPfundstein/mcp-obsidian の場合）

```
1. Obsidian → Community Plugins → "Local REST API" をインストール・有効化
2. Local REST API でAPIキーを生成
3. Claude Desktop の claude_desktop_config.json に以下を追加:

{
  "mcpServers": {
    "mcp-obsidian": {
      "command": "npx",
      "args": ["-y", "mcp-obsidian", "VAULT_PATH"],
      "env": {
        "OBSIDIAN_API_KEY": "your-api-key"
      }
    }
  }
}
```

#### ユーザーレビュー（Obsidian Forum より）

- Claude Desktopは「プロンプト1件あたり5〜10分かかる」という速度問題の報告あり
- 約4,000ノートのVaultでトークン制限に抵触したユーザーの報告
- 「週次ジャーナルのサマリー作成」「ノート作成」等の単純タスクには有効
- 大規模Vaultのサマリーや複雑な分析には不向きとの評価
- 研究者用途（正規表現検索の代替）では期待値を下回るとの意見
- 全体的な評価：「試すには面白いが、メインVaultへの永続導入には至らない」

---

## 比較表

| 比較軸 | obsidian-claude-code-mcp | MCPVault | Claudian | Claude Desktop + MCP |
|---|---|---|---|---|
| **Claude Code CLI 対応** | 明示的に対応（主目的） | 対応（設定例あり） | CLI自体が必須前提 | 非対応 |
| **アーキテクチャ** | Obsidianプラグイン（MCPサーバー） | スタンドアロンMCPサーバー | ObsidianプラグインがCLIをホスト | GUIアプリ + MCPサーバー |
| **Obsidianアプリ必須** | 必須 | 不要 | 必須 | 必須 |
| **GitHubスター数** | 206 | 971 | 5,300+ | 各実装により異なる |
| **最終更新** | 2025年6月（約9ヶ月前） | 2026年3月22日 | 2026年3月26日 | 各実装により異なる |
| **安定性** | 中（セキュリティ問題未解決） | 高（継続的改善） | 中〜低（多数のissue） | 実装により差あり |
| **トークン効率** | 情報なし（推定: 標準的） | 40〜60%圧縮（明記） | CLIと同等 | Vault規模に依存 |
| **インストール難易度** | 低（Community Plugin） | 低（npx 1行） | 中（手動コピー必須） | 中（REST APIプラグイン必要） |
| **検索機能** | なし（ファイル操作のみ） | BM25全文検索 | CLIのbash/grep経由 | 実装により異なる |
| **Windows対応** | 問題あり（未解決） | 対応 | 対応 | 対応 |

---

## 主要トレンドと構造分析

### なぜ今このエコシステムが形成されているか

2025年以降、Claude Code CLIがターミナルを超えてIDE・ノートツール・知識管理ツールへの統合を求められている背景には2つの構造的要因がある。

**1. MCP標準化の進展**: AnthropicがMCPをオープン標準として整備したことで、各ツールが共通プロトコルで接続可能になった。Obsidian側のエコシステムも迅速に反応し、複数の実装が短期間に出現した。

**2. 「コンテキスト最適化」へのニーズ**: Vault全体をプロンプトに渡すブルートフォースアプローチの限界（トークン上限・コスト）が実証済みであることから、BM25検索・ファイル単位アクセス等のオンデマンド型設計に集約しつつある。MCPVaultの「40〜60%圧縮」対応はこの流れの象徴。

---

## SWOT分析（Seep Logos 視点）

### Strengths（強み）
- MCPVaultが最も実用度が高い：Claude Code CLIとの統合、トークン効率化、活発なメンテナンスの三拍子が揃っている
- Claude Code CLIが既に導入済みであれば、追加設定コストが低い（`npx` 1行）

### Weaknesses（弱み）
- Claudian（最も人気）は多数の未解決issueを抱えており、制作業務のような継続的・高頻度利用には安定性リスクがある
- obsidian-claude-code-mcpはセキュリティ問題（CORS脆弱性）が未対処

### Opportunities（機会）
- Seep Logos の場合、Vaultを「設定資料・世界観文書の格納場所」として運用するのであれば、MCPVault経由でClaude Code CLIから直接ノートを読み書きする統合は、現行ワークフローの延長として自然に導入できる
- 世界観設定・シナリオ草稿等をObsidianで管理している場合、検索ベースアクセスによりトークン消費を最小化しつつAI活用が可能

### Threats（リスク）
- MCP仕様自体が2025〜2026年に連続更新されており、既存実装の互換性問題が今後も発生しうる
- Claudianのような急速成長プロジェクトは、メンテナー一人依存のリスクがある

---

## 機会・リスクの整理

### 導入を推奨するシナリオ

| シナリオ | 推奨ツール |
|---|---|
| Claude Code CLIから最小コストでVaultにアクセスしたい | MCPVault（@bitbonsai/mcpvault） |
| ObsidianのUI内でClaude Codeを完結させたい | Claudian（安定性を許容できる場合） |
| Claude Code CLIとClaude Desktopの両方を使い分けたい | obsidian-claude-code-mcp |
| Claude Desktopのみ使用、CLIは不要 | Claude Desktop + MCP（MarkusPfundstein/mcp-obsidian 等） |

### 留意すべきリスク

1. **obsidian-claude-code-mcp**: CORSセキュリティ問題（Issue #12）が未解決。ローカル環境限定の利用であればリスクは限定的だが、公共ネットワーク上での使用は推奨しない。
2. **Claudian**: 開発ペースは速いが、issueの数と性質（APIエラー、セッション不安定）は制作業務での安定運用に慎重な検討を要する。
3. **MCPVault**: パッケージ名変更（v0.9.0）により、既存ユーザーは設定の更新が必要。`mcpvault` から `@bitbonsai/mcpvault` への置換が必要。
4. **大規模Vault**: 4,000ノート超の規模ではトークン制限への抵触リスクがあり、MCPVaultのような検索ベースアクセスが実質的に必須となる。

---

## 戦略的示唆・提言

**短期実験向け（リスク最小）**:
MCPVaultを `claude mcp add` コマンド1行で Claude Code CLIに追加し、既存Vaultへのアクセスを試験的に評価することを提言する。設定が単純で、機能対トークン効率の比が最も優れている。

**本格導入を検討する場合**:
Claudianのissue #335（セッションハング）、#397（502エラー）、#408（レート制限）の解消状況を確認した上で判断する。スター数5,300という数字は実際の使用者数を反映しており、コミュニティのフィードバックループは機能している。

**Claude Desktop連携（CLIを使わない場合）**:
Obsidian Local REST API + Claude Desktop構成は枯れた実装が複数存在するが、処理速度（5〜10分/プロンプト）の問題が実用上のボトルネックになりうる点を考慮する必要がある。

---

## 補足資料・出典一覧

- [iansinnott/obsidian-claude-code-mcp - GitHub](https://github.com/iansinnott/obsidian-claude-code-mcp)
- [Getting Started - DeepWiki](https://deepwiki.com/iansinnott/obsidian-claude-code-mcp/1.1-getting-started)
- [bitbonsai/mcpvault - GitHub](https://github.com/bitbonsai/mcpvault)
- [MCPVault CHANGELOG](https://github.com/bitbonsai/mcpvault/blob/main/CHANGELOG.md)
- [YishenTu/claudian - GitHub](https://github.com/YishenTu/claudian)
- [Claudian Releases](https://github.com/YishenTu/claudian/releases)
- [Obsidian Forum: MCP servers experiences and recommendations](https://forum.obsidian.md/t/obsidian-mcp-servers-experiences-and-recommendations/99936)
- [Obsidian Forum: New Plugin - Agent Client](https://forum.obsidian.md/t/new-plugin-agent-client-bring-claude-code-codex-gemini-cli-inside-obsidian/108448)
- [XDA Developers: I put Claude Code inside Obsidian](https://www.xda-developers.com/claude-code-inside-obsidian-and-it-was-eye-opening/)
- [MarkusPfundstein/mcp-obsidian - GitHub](https://github.com/MarkusPfundstein/mcp-obsidian)
- [Obsidian Forum: Claude MCP for Obsidian using Rest API](https://forum.obsidian.md/t/claude-mcp-for-obsidian-using-rest-api/93284)

---

*調査者: 情報屋（マーケティングPR部 / competitive-analyst）*
*作成日: 2026-03-27*
*参照Skill: competitive-research*
