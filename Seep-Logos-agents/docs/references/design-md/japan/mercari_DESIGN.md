# DESIGN.md — メルカリ (mercari.com/jp)

> このファイルはAIエージェントが正確な日本語UIを生成するためのデザイン仕様書です。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: クリーン、ミニマル、白背景ベースの実用志向UI
- **密度**: 商品一覧のグリッド表示は情報密度が高いが、余白は十分に確保
- **キーワード**: シンプル、信頼感、ホワイトスペース、メルカリレッド、機能的
- **特記**: CSSフレームワークに Panda CSS を採用。body font-size が 15px（一般的な 16px ではない）。見出しの色が `#666666` でメイン `#333333` より薄い珍しいパターン

---

## 2. Color Palette & Roles

### Primary（ブランドカラー）

- **Mercari Red** (`#ff333f`): メインのブランドカラー。CTAボタン、アクティブタブに使用

### Semantic（意味的な色）

- **Link** (`#0073cc`): テキストリンク

### Neutral（ニュートラル）

- **Text Primary** (`#333333`): 本文テキスト
- **Text Secondary** (`#666666`): 見出し（h2）、非アクティブタブ
- **Background** (`#ffffff`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN Custom", "Hiragino Sans Custom", "Meiryo Custom", sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height | 備考 |
|------|------|--------|-------------|------|
| Heading 2 | 20px | 700 | 28px (×1.4) | 色 #666666 |
| Heading 3 | 17px | 700 | 23.8px (×1.4) | 色 #333333 |
| Body | 15px | 400 | 21px (×1.4) | 色 #333333 |
| CTA Button | 14px | 700 | — | 色 #fff / bg #ff333f |
| Input | 16px | 400 | 22.4px | 検索入力欄 |

### 3.5 行間・字間

- **全体で line-height ×1.4 に統一**
- **letter-spacing**: normal（全要素）
- **palt**: 未使用

---

## 4. Component Stylings

### Buttons

**Primary (CTA)**
- Background: `#ff333f`
- Text: `#ffffff`
- Border Radius: 4px
- Font Weight: 700

**Tabs（Active）**
- Text: `#ff333f`
- Font Weight: 700

### Inputs

- Border Radius: 0px（角丸なし）
- Font Size: 16px

---

## 5. Layout Principles

### CSS Custom Properties（実測値）

| Token | Value |
|-------|-------|
| --grid-layout-gutter | 24px |
| --grid-layout-inset | 16px |
| --grid-layout-page-padding-top | 40px |
| --grid-layout-page-padding-bottom | 64px |
| --grid-layout-page-padding-horizontal | 36px |

### z-index 階層

| Token | Value |
|-------|-------|
| --mer-z-index-menu | 1100 |
| --mer-z-index-navigation | 1200 |
| --mer-z-index-modal | 1400 |
| --mer-z-index-snackbar | 1500 |
| --mer-z-index-tooltip | 1600 |

---

## 7. Do's and Don'ts

### Do（推奨）

- ブランドカラー `#ff333f` はCTAとアクティブ状態にのみ使用する
- body の font-size は 15px を守る（16px にしない）
- line-height は ×1.4 で統一する
- ボタンの角丸は 4px に統一する
- 見出しには `#666666` を使用し、本文 `#333333` と差をつける

### Don't（禁止）

- `#ff333f` を背景色やテキスト色として多用しない
- letter-spacing を追加しない（全要素で normal が統一ルール）
- palt を適用しない（サイト全体で未使用）
- line-height を ×1.4 以外に変えない

---

## 9. Agent Prompt Guide

```
Primary Color: #ff333f (Mercari Red)
Link Color: #0073cc
Text Color: #333333
Text Secondary: #666666
Background: #ffffff
Font: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN Custom", "Hiragino Sans Custom", "Meiryo Custom", sans-serif
Body Size: 15px
Line Height: 1.4
Letter Spacing: normal
palt: なし
CSS Framework: Panda CSS
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
