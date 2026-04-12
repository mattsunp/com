# セッション決定事項 2026-04-11 (10)

## トピック: DESIGN.md ブランドサンプルHTML制作

### 完了事項

- `docs/references/design-md/samples/brand/` — Claude Code 直接生成版（5件）
  - apple.html / airbnb.html / ferrari.html / cursor.html / stripe.html
  - 各ブランドの構造・レイアウト・哲学を反映した手書きHTML

- `docs/references/design-md/samples/brand-flow/` — パイプライン経由版（5件）
  - 同5ブランドを web-director → web-designer → web-coder の3段パイプラインで生成
  - orchestrator を経由して並列処理

### 決定事項

1. **今後の残りブランドはパイプライン経由で制作する**
   - 理由: web-designerたちにWebデザインの経験を蓄積させる目的
   - 方式: orchestrator → web-director → web-designer → web-coder

2. **brand/ と brand-flow/ の両方を保持する**
   - 比較資産として残す
   - 削除しない

3. **評価**: brand-flow版はまだ均一感があり、「天才になりきれていない」
   - 今後の経験蓄積で改善を期待

### 未着手（次回セッション以降）

- 残り約77ブランドのパイプライン経由HTML制作
  - 制限明け（0時以降）に再開予定
  - 次バッチ候補: Notion, Linear, Nike, Muji, Spotify 等

### ビジネス課題（別セッションで対応）

- Webデザイン＆SNS運用チームの人選 → 初売上
- アニメ・ゲーム企業リストからの営業先選定
- デザイン会社 Qbist との関係活用
- FlipSide 等 人気アーティストの活用
- アートディレクターの発掘
- 名刺のリスト化と人脈検索の仕組みづくり
