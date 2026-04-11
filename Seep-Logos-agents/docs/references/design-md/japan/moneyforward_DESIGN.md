# DESIGN.md — マネーフォワード (moneyforward.com)

> マネーフォワードのデザイン仕様書。CSS Custom Properties は未使用の従来型CSS設計。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 堅実で信頼感のある業務ツール型UI。家計簿・資産管理という金融領域に相応しい落ち着いたトーン
- **キーワード**: 堅実、信頼性、業務的、効率的、和文優先
- **特徴**: ヒラギノ角ゴ Pro を先頭に置く和文優先フォントスタック。見出しは weight 500（medium）で控えめな強調

---

## 2. Color Palette & Roles

### Primary

- **Primary Green** (`#4db848`): CTAボタン、アクセント
- **Dark** (`#3a9a35`): ホバー時

### Semantic

- **Danger** (`#e74c3c`) / **Warning** (`#f39c12`) / **Success** (`#27ae60`)

### Neutral

- **Text Primary** (`#333333`) / **Text Secondary** (`#666666`)
- **Border** (`#dddddd`) / **Background** (`#ffffff`)
- **Surface** (`#f5f5f5`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* 和文優先スタック */
font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro W3",
  Meiryo, メイリオ, "MS PGothic", Osaka, sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Heading 2 | 20px | 500 | normal |
| Heading 3 | 17px | 500 | 1.7 |
| Body Nav | 14px | 500 | 1.5 |
| Body | 14px | 400 | 1.5 |
| Caption | 12px | 400 | 1.5 |

### 行間・字間

- **本文**: `line-height: 1.5`
- **見出し weight**: 500（medium）— bold ではない
- **字間**: normal / **palt**: 未使用

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#4db848` / Text: `#ffffff`
- Padding: 8px 24px / Border Radius: 4px / Weight: 500

### Cards

- Background: `#ffffff`
- Border: 1px solid `#eeeeee`
- Border Radius: 4px
- Shadow: `0 1px 3px rgba(0,0,0,0.08)`

---

## 7. Do's and Don'ts

### Do（推奨）

- 見出しの weight は 500 に統一する（bold ではなく medium）
- 14px ベースの密度を維持する
- 日本語本文の line-height は 1.5 以上にする

### Don't（禁止）

- 見出しに font-weight: 700 を使わない（500 medium が基本）
- palt を適用しない
- CSS Custom Properties を新たに導入しない

---

## 9. Agent Prompt Guide

```
Primary Color: #4db848
Text Color: #333333 / Background: #ffffff
Font: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro W3", Meiryo, メイリオ, "MS PGothic", Osaka, sans-serif
Body Size: 14px / Line Height: 1.5
Heading Weight: 500 / palt: なし / CSS Custom Properties: なし
```

### freee との主な違い

| 項目 | マネーフォワード | freee |
|------|-----------------|-------|
| ブランドカラー | グリーン `#4db848` | ブルー `#2864f0` |
| 本文サイズ | 14px | 14px(Product)/16px(Web) |
| 見出し weight | 500 (medium) | 500/700 |
| 和文フォント | ヒラギノ角ゴ Pro 優先 | Noto Sans JP / システム |
| CSS Custom Properties | なし | Vibes で使用 |

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
