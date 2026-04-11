# セッション決定事項 2026-04-11 #8

## トピック: DESIGN.md 収集 完了記録

---

## 完了事項

### タスクA: DESIGN.md 国内外ブランド収集 — 完了

**日本版（22ブランド + テンプレート1件）**
`docs/references/design-md/japan/` に保存済み。
ABEMA, pixiv, LINE, note, メルカリ, SmartHR, 楽天市場, MUJI, Qiita, Zenn, freee, クックパッド, Toyota, 食べログ, マネーフォワード, Sansan, STUDIO, サイボウズ, connpass, Novasell, Notion, テンプレート

**国際版（62ファイル）**
`docs/references/design-md/international/` に保存済み。
取得手段: `npx getdesign@latest add [brand]`（getdesign CLI、要アカウント）
主要ブランド: Airbnb, Claude, Spotify, Apple, Figma, Vercel, Supabase, Cursor, Linear, Superhuman, Ferrari, BMW, Lamborghini, Tesla, Nike, Binance, Coinbase, Stripe, Shopify, Meta, Nvidia, SpaceX, IBM ほか

**インデックス**: `docs/references/design-md/INDEX.md`
（INDEX.md表記は「60ブランド」だが実ファイル数は62。lovable重複カウントと収集後追加分による差異）

---

## 判明した副次情報

- **superhuman_DESIGN.md 誤検知の原因**: バッチ処理スクリプトの `-i` フラグ（大文字小文字無視）により本文中の `critical` を `CRITICAL` と誤ってマッチ。ファイル自体のコンテンツはクリーン。
- **inject フック**: AHA Music 拡張機能が無効化された後も類似パターンが検出されたが、inject.log の範囲では経路特定に至らず。
- **getdesign CLI**: `npx getdesign@latest add [brand]` で取得。アカウント作成後に全ブランドが取得可能になる。

---

## 継続事項

### タスクB: Webデザイナー業務マニュアル作成（未着手）
- 対象読者: 採用予定の素人Webデザイナー
- 目的: DESIGN.md を読んで web-designer / web-coder エージェントと協働できる人材の育成
- 内容: DESIGN.md の書き方 + AIエージェントとの協業フロー
- 保存先: 未定
