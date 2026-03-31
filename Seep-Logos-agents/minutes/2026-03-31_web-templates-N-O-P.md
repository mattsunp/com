# 議事録
日時：2026-03-31
参加エージェント：情報屋、指揮者、Web管理者、アート管理者、ゲームUIデザイナー、ゲームUIエンジニア、書記
記録者：スタジオ運営管理部 / 書記（recorder）

---

## 議題一覧
1. CoDD（Coherence-Driven Development）調査と導入判断
2. Webテンプレート Pattern N 作成（Chapter Scroll）
3. Webテンプレート Pattern O 作成（Card Carousel）
4. Webテンプレート Pattern P 作成（Dual Column Chapter）
5. セキュリティ情報共有（axios サプライチェーン攻撃）

---

## やり取りサマリー

### 議題1：CoDD（Coherence-Driven Development）調査と導入判断

- 依頼内容：`codd-dev`（pip install codd-dev）の実態調査
- 対応エージェント：情報屋
- 主な出力・決定事項：
  - PyPI に実在することを確認（v0.7.0、2026-03-29 リリース、Public Alpha）
  - 核心機能として `codd scan`（依存グラフ構築）と `codd impact`（変更影響分析・Green/Amber/Gray 分類）の存在を確認
  - 導入の選択肢として「①pip install codd-dev による実導入」「②思想のみを参照し実装は行わない」の2案が提示された
  - プロデューサーの判断により、当該セッションでは着手せず、Webデザイン作業を優先することが決定した
- 次のアクション：CoDD 導入は積み残し事項として継続検討

---

### 議題2：Webテンプレート Pattern N 作成（Chapter Scroll）

- 依頼内容：チャプタースクロール型のWebテンプレート作成
- 対応エージェント：指揮者、Web管理者、アート管理者、ゲームUIエンジニア
- 主な出力・決定事項：
  - コンセプト名：Chapter Scroll（チャプタースクロール型）
  - 出力ファイル：
    - `web/templates/pattern-N_chapter-scroll.md`（仕様書）
    - `web/templates/pattern-N_chapter-scroll.html`（実装）
  - YAMLキュー：`queue/web-pattern-n-20260331.yaml`
  - Pattern E（Scrollytelling）との差別化方針として、演出が主役ではなくテキスト・物語が主役であることを明確化
  - 主な実装特徴：チャプターNAVドットの3状態管理、キーボード操作対応、プログレスバー表示
  - Pattern N の制作が完了したことが確認された
- 次のアクション：なし（完了）

---

### 議題3：Webテンプレート Pattern O 作成（Card Carousel）

- 依頼内容：カードカルーセル型のWebテンプレート作成
- 対応エージェント：指揮者、Web管理者、アート管理者、ゲームUIデザイナー、ゲームUIエンジニア
- 主な出力・決定事項：
  - コンセプト名：Card Carousel（カードカルーセル型）
  - 出力ファイル：
    - `web/templates/pattern-O_card-carousel.md`（仕様書）
    - `web/templates/pattern-O_card-carousel.html`（実装）
  - YAMLキュー：`queue/web-pattern-o-20260331.yaml`
  - 用途として更新頻度が高いコンテンツ向けと位置付けられた
  - Pattern L（News Feed）との差別化方針として「読む」体験ではなく「めくって発見する」体験を軸とすることが決定した
  - 主な実装特徴：カテゴリタブ→カルーセル→カードホバーの三層構造、自動スライド5秒
  - Pattern O の制作が完了したことが確認された
- 次のアクション：なし（完了）

---

### 議題4：Webテンプレート Pattern P 作成（Dual Column Chapter）

- 依頼内容：プロデューサー指示による中央線交互レイアウト型のWebテンプレート作成
- 対応エージェント：指揮者、Web管理者、アート管理者、ゲームUIエンジニア
- 主な出力・決定事項：
  - コンセプト名：Dual Column Chapter（中央線交互レイアウト型チャプタースクロール）
  - プロデューサー指示の内容：中央に縦線を引き、左右交互に画像とテキストを配置する
  - 出力ファイル：
    - `web/templates/pattern-P_dual-column-chapter.md`（仕様書）
    - `web/templates/pattern-P_dual-column-chapter.html`（実装）
  - YAMLキュー：`queue/web-pattern-p-20260331.yaml`
  - 主な実装特徴：CSSグリッド `1fr 2px 1fr` によるレイアウト、センターラインがスクロールに連動して描かれる演出、偶数チャプターは右揃えとなる「鏡」構造
  - Pattern N との差分として「書物を読む」体験から「展覧会を歩く」体験へのシフトが定義された
  - Pattern P の制作が完了したことが確認された
- 次のアクション：なし（完了）

---

### 議題5：セキュリティ情報共有（axios サプライチェーン攻撃）

- 依頼内容：セキュリティ情報の共有と対応方針の確認
- 対応エージェント：（プロデューサーより共有）
- 主な出力・決定事項：
  - axios がサプライチェーン攻撃を受けているとの情報が共有された
  - npm アカウント乗っ取りによるリスクが指摘された
  - 当面の間、npm 系コマンド（npm install / update / audit 等）を実行しない方針が確認された
  - 当プロジェクトは外部依存ゼロの方針を採用しているため、直接の影響はないと判断された
- 次のアクション：npm 系コマンドの実行を控える方針を継続する

---

## 決定事項まとめ

- CoDD 導入は当セッションでは着手しないことが決定した
- Pattern N（Chapter Scroll）の制作が完了した
- Pattern O（Card Carousel）の制作が完了した
- Pattern P（Dual Column Chapter）の制作が完了した
- axios サプライチェーン攻撃への対応として、npm 系コマンドを当面実行しない方針が確認された

---

## 未解決・継続課題

- CoDD 導入（Stage 0〜3）は積み残し事項として継続検討
- ゲーム企画チームへの YAML キュー適用確認は未着手

---

## 参考：本セッション終了時点のテンプレートラインナップ

| ID | コンセプト名 |
|---|---|
| A | Teaser |
| B | World-first |
| C | Editorial |
| D | Bento-reveal |
| E | Scrollytelling |
| F | Cinematic LP |
| G | Character Encyclopedia |
| H | Dark Immersive |
| I | Japanese Texture |
| J | Hub-and-Spoke |
| K | Pastel Pop |
| L | News Feed |
| M | Timeline Immersion |
| N | Chapter Scroll |
| O | Card Carousel |
| P | Dual Column Chapter |
