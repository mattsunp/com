# DESIGN.md — 無印良品ネットストア (muji.com)

> このファイルはAIエージェントが正確な日本語UIを生成するためのデザイン仕様書です。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: ミニマリズムの極致。装飾を完全に排し、余白で語るデザイン
- **密度**: ゆったりとしたメディア型。商品画像と余白を活かした構成
- **キーワード**: 素朴、静謐、無装飾、自然体、余白

---

## 2. Color Palette & Roles

### Primary（ブランドカラー）

- **MUJI Red** (`#7f0019`): 深みのあるブランドカラー。ロゴ、アクセントに控えめに使用
- **Red** (`#dd0c14`): 強調・セール・エラー表示

### Brand Neutral（MUJIらしさ）

- **Kinari（きなり色）** (`#f4eede`): MUJIの象徴。ヒーロー背景、セクション背景
- **Beige** (`#e0ceaa`): 温かみのあるアクセント面

### Neutral

- **Text Primary** (`#3c3c43`): 本文テキスト（純黒ではない）
- **Text Secondary** (`#6d6d72`)
- **Text Tertiary** (`#76767b`)
- **Border** (`#d8d8d9`)
- **Border Light** (`#ebebec`)
- **Background** (`#fff`)
- **Background Secondary** (`#f5f5f5`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
font-family: "Helvetica Neue", Arial, "Noto Sans JP", "Noto Sans JP Fallback",
  "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height | Letter Spacing | 備考 |
|------|------|--------|-------------|----------------|------|
| Heading 2 | 32px | 700 | 1.6 | normal | 大見出し |
| Heading 3 | 26px | 700 | 1.15 | 2.4px | 広いトラッキング（例外） |
| Body | 16px | 400 | 1.6 | normal | ページ全体ベース |
| Paragraph | 12px | 400 | 1.6 | normal | 商品説明等 |

### 行間・字間

- **line-height: 1.6 を全体で統一**（見出しも本文も）
- **h3 のみ例外**: `line-height: 1.15` / `letter-spacing: 2.4px`
- **palt**: 未使用 / **字間**: normal（h3除く）

---

## 4. Component Stylings

### Buttons

**Primary (CTA)**
- Background: `#3c3c43`（テキスト色と同じ暗いグレー）
- Text: `#fff` / Border Radius: 4px / Font Size: 12px / Weight: 700

**Secondary**
- Background: `transparent` / Text: `#3c3c43`
- Border: 1px solid `#d8d8d9` / Border Radius: 4px

### Inputs

- Border Radius: 0px（角丸なし）/ Font Size: 16px
- Border (focus): 1px solid `#3c3c43`

### Cards

- Border: 1px solid `#ebebec`
- Border Radius: 0px / Shadow: なし（フラット）

---

## 5. Layout Principles

### Spacing Scale（12段階）

```
XXXXS: 4px / XXXS: 8px / XXS: 12px / XS: 16px / S: 20px / SM: 24px
M: 32px / ML: 40px / L: 48px / XL: 56px / XXL: 64px / XXXL: 80px / XXXXL: 96px
```

CSS Custom Properties: `--space-v-xxxxs` (4px) から `--space-v-xxxxl` (96px) まで12段階

---

## 7. Do's and Don'ts

### Do（推奨）

- テキスト色は `#3c3c43`（純黒 `#000` を避ける）
- line-height は 1.6 で統一する
- 余白を十分に取り、要素間にゆとりを持たせる
- ボタンの角丸は 4px に留める
- きなり色 `#f4eede` で温かみを加える
- 装飾は最小限に

### Don't（禁止）

- 装飾的なグラデーション、シャドウ、アニメーションを多用しない
- MUJI Red `#7f0019` を広い面積に使わない
- palt を適用しない
- 角丸を 8px 以上にしない

---

## 9. Agent Prompt Guide

```
Brand Color: #7f0019 (MUJI Red)
Text Color: #3c3c43
Background: #fff / Kinari: #f4eede / Beige: #e0ceaa
Font: "Helvetica Neue", Arial, "Noto Sans JP", "Noto Sans JP Fallback",
  "Hiragino Kaku Gothic ProN", Meiryo, sans-serif
Body Size: 16px / Line Height: 1.6
Button Radius: 4px / Input Radius: 0px
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
