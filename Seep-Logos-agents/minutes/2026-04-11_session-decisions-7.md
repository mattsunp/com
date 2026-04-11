# セッション決定事項 2026-04-11 #7

## トピック: DESIGN.md収集 & Webデザイナー業務マニュアル構想

---

## 完了事項

### タスクA: DESIGN.md収集
- `docs/references/design-md/japan/` に日本版22ブランドを保存
- 保存済みブランド: ABEMA, pixiv, LINE, note, メルカリ, SmartHR, 楽天市場, MUJI, Qiita, Zenn, freee, クックパッド, Toyota, 食べログ, マネーフォワード, Sansan, STUDIO, サイボウズ, connpass, Novasell, Notion, テンプレート
- インデックスファイル: `docs/references/design-md/INDEX.md`
- 国際版（60+ブランド）は getdesign.md（ログイン必須）に存在。取得方法は未確定

### 背景
- 初芝賢(@hatushiba_ken)のツイートでDESIGN.mdの概念を認知
- 「デザインルールをMarkdown1枚に集約 → AIが直接読める」という概念
- ゲーム・アニメIPサイトの参考資料として収集

---

## 未解決・継続事項

### タスクB: Webデザイナー業務マニュアル作成（着手前）
- 対象読者: 素人Webデザイナー（実際に雇い入れ予定）
- 目的: AIエージェント（web-designer, web-coder）と連携してWeb制作を事業化
- 内容確認中: DESIGN.mdを書く仕事としてのハンドブック + AIエージェントとの協業フロー
- 保存先: 未定

### 国際版DESIGN.md取得
- getdesign.md にアカウントを作ればCLI（npx getdesign@latest add [brand]）で取得可能
- WebFetchは認証不可のため、取得方法の選択が必要

---

## 決定事項

- DESIGN.mdコレクションは今後 `docs/references/design-md/` に集積していく方針
- WebデザイナーマニュアルはタスクBとして別途着手
