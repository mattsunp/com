# DESIGN.md — SmartHR

> SmartHR（https://smarthr.jp/）のデザイン仕様書。SmartHR Design System の公式デザイントークンに基づく。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: クリーンで信頼感のある業務UI。装飾を排し、コンテンツと操作性を優先するミニマルなデザイン
- **キーワード**: 信頼性、明快、効率的、アクセシブル、ニュートラル
- **特徴**: ウォームグレー（Stone系）を基調とした柔らかいニュートラルカラー

---

## 2. Color Palette & Roles

### Primary（ブランドカラー）

- **SmartHR Blue** (`#00c4cc`): ブランドアイデンティティカラー。ロゴ、イラスト用。テキストやUI要素には非推奨
- **Product Main** (`#0077c7`): プロダクトUIのプライマリカラー。ボタン、アクティブ状態

### Semantic

- **Danger** (`#e01e5a`)
- **Warning** (`#ffcc17`)
- **Text Link** (`#0071c1`)

### Neutral — Stone Scale（ウォームグレー）

- **Text Black** (`#23221e`): 本文テキスト
- **Text Grey** (`#706d65`): 補足テキスト
- **Text Disabled** (`#c1bdb7`)
- **Stone 01** (`#f8f7f6`): ページ背景
- **Stone 02** (`#edebe8`): テーブルヘッダー背景
- **Border** (`#d6d3d0`)
- **Surface** (`#ffffff`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* @font-face で游ゴシック Medium を 400 にマッピング */
@font-face {
  font-family: AdjustedYuGothic;
  font-weight: 400;
  src: local("Yu Gothic Medium");
}

font-family: AdjustedYuGothic, "Yu Gothic", YuGothic, "Hiragino Sans", sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Token | Size | Weight | Line Height |
|------|-------|------|--------|-------------|
| Display | XXL | 2rem (32px) | 700 | 1.25 |
| Heading 1 | XL | 1.5rem (24px) | 700 | 1.25 |
| Heading 2 | L | 1.2rem (19.2px) | 700 | 1.5 |
| Body | M | 1rem (16px) | 400 | 1.5 |
| Small | S | 0.857rem (13.7px) | 400 | 1.5 |
| Caption | XS | 0.75rem (12px) | 400 | 1.5 |

### 行間・字間

- **本文**: `line-height: 1.5`（NORMAL）
- **見出し**: `line-height: 1.25`（TIGHT）
- **字間**: 0（デフォルト）

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#0077c7` / Text: `#ffffff`
- Border Radius: 6px / Padding: 8px 16px / Weight: 700

**Secondary**
- Background: `transparent` / Text: `#0077c7`
- Border: 1px solid `#0077c7` / Border Radius: 6px

**Danger**
- Background: `#e01e5a` / Text: `#ffffff`

### Inputs

- Background: `#ffffff`
- Border: 1px solid `#d6d3d0`
- Border (focus): 2px solid `#0077c7`
- Border Radius: 6px

### Tables

- Header Background: `#edebe8`
- Border: 1px solid `#d6d3d0`

---

## 5. Layout Principles

### Spacing Scale（8px ベース）

| Token | Value |
|-------|-------|
| XS | 4px |
| S | 8px |
| M | 16px |
| L | 24px |
| XL | 32px |
| XXL | 40px |

### Breakpoints

| Name | Width |
|------|-------|
| SP | ≤ 599px |
| Tablet | 600px–959px |
| Desktop | ≥ 960px |

---

## 7. Do's and Don'ts

### Do（推奨）

- Windows での游ゴシック表示には必ず `AdjustedYuGothic` の @font-face を使う
- テキストカラーは `#23221e`（Text Black）を使い、純粋な `#000000` は避ける
- ブランドカラー `#00c4cc` はイラスト・チャート用。UIの操作要素には `#0077c7` を使う

### Don't（禁止）

- ブランドカラー `#00c4cc` をテキストや小さなUI要素に使わない
- 游ゴシックを @font-face なしで font-weight: 400 指定しない
- 純粋なグレーを使わない（Stone 系のウォームグレーを使う）

---

## 9. Agent Prompt Guide

```
Brand Color: #00c4cc（ロゴ・チャート用）
Product Main: #0077c7
Text Color: #23221e
Text Secondary: #706d65
Link Color: #0071c1
Background: #f8f7f6
Surface: #ffffff
Border: #d6d3d0
Danger: #e01e5a
Font: AdjustedYuGothic, "Yu Gothic", YuGothic, "Hiragino Sans", sans-serif
Body Size: 16px / Line Height: 1.5
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
