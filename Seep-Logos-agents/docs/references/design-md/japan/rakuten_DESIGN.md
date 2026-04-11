# DESIGN.md — 楽天市場

> 楽天市場（https://www.rakuten.co.jp/）のデザイン仕様書。CSS Custom Properties は使用されていない。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 情報密度が極めて高い、商品の露出を最大化するEC型レイアウト
- **密度**: 極めて高密度。body 12px / line-height 1.1 という国内サイト最小級の本文設定
- **キーワード**: 高密度、商売的、にぎやか、和文優先、レガシー
- **特徴**: CSS Custom Properties を使用せず、インラインスタイルとクラス直書きが中心。メイリオ先頭の和文優先フォントスタック

---

## 2. Color Palette & Roles

### Primary（ブランドカラー）

- **楽天レッド** (`#bf0000`): ブランドカラー。ヘッダー背景、CTA、セール表示など全面的に使用
- **楽天レッド Dark** (`#990000`): ホバー・プレス時

### Semantic

- **Danger / Sale** (`#bf0000`)（ブランドカラーと兼用）
- **Warning / Point** (`#ff8c00`)
- **Success** (`#008000`)

### Neutral

- **Text Primary** (`#666666`)
- **Text Dark** (`#333333`)
- **Text Secondary** (`#999999`)
- **Border** (`#dddddd`)
- **Background** (`#ffffff`)
- **Background Gray** (`#f6f6f6`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
font-family: Meiryo, "Hiragino Kaku Gothic ProN", "MS PGothic", sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height | 備考 |
|------|------|--------|-------------|------|
| Heading 2 | 20px | 600 | 1.3〜1.4 | セクション見出し |
| Body | 12px | 400 | 1.1 | 本文テキスト（極めてタイト） |
| Price | 14px | 700 | — | 商品価格 |
| Price (Sale) | 16px | 700 | — | セール価格（赤字） |
| Caption | 10px | 400 | 1.1 | 注釈 |

### 行間・字間

- **本文**: `line-height: 1.1`（日本語として極めてタイト。情報密度最大化の設計思想）
- **字間**: normal / **palt**: 未使用

---

## 4. Component Stylings

### Buttons

**Primary（購入ボタン）**
- Background: `#bf0000` / Text: `#ffffff`
- Padding: 8px 16px / Border Radius: 4px / Weight: 700

### Cards（商品カード）

- Background: `#ffffff`
- Border: 1px solid `#dddddd`
- Border Radius: 0px（角丸なし）
- Shadow: none

---

## 5. Layout Principles

### Spacing Scale

| Token | Value |
|-------|-------|
| XS | 4px |
| S | 8px |
| M | 12px |
| L | 16px |
| XL | 24px |

### Container

- Max Width: 1120px
- Padding (horizontal): 0px（余白なし設計）

---

## 7. Do's and Don'ts

### Do（推奨）

- メイリオ先頭の和文優先フォントスタックを維持する
- 商品情報は高密度に配置し、一覧性を重視する
- 価格表示は `#bf0000` で統一する
- ボーダー（`#dddddd`）で要素を区切る

### Don't（禁止）

- line-height を 1.5 以上に広げない（情報密度が崩れる）
- 角丸を多用しない（シャープな矩形が基本）
- CSS Custom Properties を使わない（直書きスタイルが基本）
- 欧文フォントを和文フォントの前に配置しない

---

## 9. Agent Prompt Guide

```
Primary Color: #bf0000 (楽天レッド)
Text Color: #666666
Text Dark: #333333
Background: #ffffff
Font: Meiryo, "Hiragino Kaku Gothic ProN", "MS PGothic", sans-serif
Body Size: 12px / Line Height: 1.1
Letter Spacing: normal / palt: 未使用 / CSS Variables: なし
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
