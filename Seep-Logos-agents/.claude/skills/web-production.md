# スキル：Webサイト・LP制作フロー

> **用途：** orchestrator が Webサイト・LP制作タスクを受けたときに参照する実行手順。
> Web制作部（web-director / web-designer / web-coder）の3段階フローを定義する。

---

## 前提

- 本フローは **順序依存**。各ラウンドの成果物ファイルが存在することを確認してから次を開始する
- 成果物はすべてファイルに書き出す。orchestrator は要約ではなくファイルパスを次エージェントに渡す
- ファイル命名規則：`web/[案件名]/instructions/` 以下に保存する

---

## フロー

### Round 1 — Web管理者（web-director）：戦略・設計

**入力：** プロデューサーからの依頼内容（対象IP・目的・フェーズ・公開時期など）

**指示：**
```
以下の情報をもとに、Webサイトの戦略設計を行い、
結果を `web/[案件名]/instructions/director.md` に保存してください。

[依頼内容をここに記載]
```

**完了条件：** `web/[案件名]/instructions/director.md` が存在すること

**成果物の必須項目：**
- 採用パターン（pattern-A〜P から選択・理由付き）
- 感情アーキテクチャ（着地時→離脱時の感情変化）
- スクロール構造（セクション順・各セクションの役割）
- IP固有アクセントカラーの方向性
- 公開フェーズ（ティザー / リリース前 / リリース後）

---

### Round 2 — Webデザイナー（web-designer）：ビジュアル設計

**入力：** `web/[案件名]/instructions/director.md`

**指示：**
```
`web/[案件名]/instructions/director.md` を読み、
ビジュアル仕様書を `web/[案件名]/instructions/designer.md` に保存してください。
値は `web/templates/DESIGN.md` から取得してください。
```

**完了条件：** `web/[案件名]/instructions/designer.md` が存在すること

**成果物の必須項目（`web/templates/DESIGN.md` の出力型に準拠）：**
- カラー定義（`--bg` / `--surface` / `--text` / `--accent` + 各理由）
- タイポグラフィ定義（フォント・サイズ・字間・行間 + 各理由）
- グリッド・レイアウト定義
- アニメーション仕様（duration / easing / transform）
- 余白設計
- モバイル対応方針
- 構築人（web-coder）への注意事項

---

### Round 3 — 構築人（web-coder）：実装

**入力：** `web/[案件名]/instructions/director.md` + `web/[案件名]/instructions/designer.md`

**指示：**
```
以下の2ファイルを読み、HTMLとCSSを実装して `web/[案件名]/index.html` に保存してください。
- `web/[案件名]/instructions/director.md`（サイト戦略・構造）
- `web/[案件名]/instructions/designer.md`（ビジュアル仕様）

値は `web/templates/DESIGN.md` から取得し、ハードコードしないこと。
`web/templates/` の該当パターンHTMLを参照実装として使うこと。
```

**完了条件：** `web/[案件名]/index.html` が存在し、ブラウザで表示できること

---

## orchestrator の進行ルール

1. 各ラウンド開始前に、前ラウンドの成果物ファイルの存在を確認する
2. ファイルが存在しない場合、前ラウンドを再実行してから次に進む
3. YAML キュー（`queue/[task-id].yaml`）に各ラウンドの状態を記録する
4. ギャップ診断：Round 2 完了後、director.md の戦略と designer.md の設計に乖離がないか確認する

## ファイル構成（完成時）

```
web/
└── [案件名]/
    ├── instructions/
    │   ├── director.md    # Round 1 成果物
    │   └── designer.md    # Round 2 成果物
    └── index.html         # Round 3 成果物
```

---

*Seep Logos クリエイティブスタジオ | Web制作部スキル | 2026-04-04*
