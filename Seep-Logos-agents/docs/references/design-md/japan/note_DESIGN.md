# DESIGN.md — note

> note（https://note.com/）のデザイン仕様書。
> 実サイトのCSS（Tailwind CSS v3.4.1 + Svelte スコープドスタイル）および CSS Custom Properties に基づく。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 読みやすさを最優先にした、落ち着いたメディアプラットフォーム
- **密度**: ゆったりとした余白。記事コンテンツエリアは 620px 幅で可読性を重視
- **キーワード**: 読みやすい、温かい、ミニマル、コンテンツファースト、落ち着き
- **特徴**: 純粋な黒（`#000000`）ではなく、ほぼ黒の `#08131a` を使用し、柔らかい読書体験を提供。ダークモード完全対応

---

## 2. Color Palette & Roles

### Primary（ブランドカラー）

- **note Green** (`#5ac8b8`): ブランドアイデンティティカラー。ロゴ、アクセントに使用

### Semantic（CSS Custom Properties 実測値）

- **Success** — surface: `#1e7b65`, text: `#1e7b65`
- **Danger** — surface: `#b22323`, text: `#b22323`
- **Caution** — surface: `#916626`, text: `#916626`
- **Like** — surface: `#d13e5c`, text: `#d13e5c`
- **Badge** (`#d53c21`): 通知バッジ

### Neutral — Gray Scale

- **Gray 900** (`#08131a`): 本文テキスト（ほぼ黒）
- **Gray 800** (`#202a30`)
- **Gray 700** (`#363f42`)
- **Gray 600** (`#5a656b`): セカンダリテキスト
- **Gray 500** (`#7e888f`)
- **Gray 400** (`#9ca7ad`)
- **Gray 200** (`#c5ccd1`)
- **Gray 100** (`#dce0e3`)
- **Gray 50** (`#f5f8fa`): セカンダリ背景

### Surface & Borders

- **Background Primary** (`#fff`)
- **Background Secondary** (`#f5f8fa`)
- **Border Default** (`rgba(8,19,26,0.14)`)
- **Border Strong** (`rgba(8,19,26,0.22)`)
- **Border Focus** (`#292d9e`)

### CTA

- **Custom Accent** (`#08131a`): CTA（ライトモード）

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* デフォルト（ゴシック体） */
font-family: "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN",
  Arial, "Noto Sans JP", Meiryo, sans-serif;

/* 明朝体（記事本文オプション） */
font-family: "Hiragino Mincho ProN", "Hiragino Mincho Pro", HGSMinchoE,
  "Yu Mincho", YuMincho, "MS PMincho", serif;

/* 等幅 */
font-family: SFMono-Regular, Consolas, Menlo, Courier, monospace;

/* 数字専用 */
font-family: "Open Sans", sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

**記事ページ**

| Role | Size | Weight | Line Height | Letter Spacing | palt |
|------|------|--------|-------------|----------------|------|
| Article Title (h1) | 32px | 700 | 48px (×1.5) | 1.28px (0.04em) | あり |
| Heading 2 | 28px | 700 | 36px (×1.286) | 1.12px (0.04em) | あり |
| Body (p) | 18px | 400 | 36px (×2.0) | normal | なし |

**トップページ**

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Heading 2 | 16px | 600 | 24px |
| Heading 3 | 16px | 600 | 24px |
| Caption (p) | 12px | 600 | 18px |

### 3.5 行間・字間

- **記事本文**: `font-size: 18px` + `line-height: 2.0`（非常にゆったり）
- **`letter-spacing: 0.04em` と `palt` は見出し専用**。本文には適用しない

---

## 4. Component Stylings

### Buttons

**Primary（CTA）**
- Background: `#08131a`
- Text: `#ffffff`

**Like Button**
- Active Color: `#d13e5c`

### Cards

- Background: `#fff`
- Border Radius: 12px
- Shadow: `0px 1px 3px 1px rgba(0,0,0,0.14), 0px 1px 2px 0px rgba(0,0,0,0.22)`

---

## 5. Layout Principles

### Content Width

| Area | Width |
|------|-------|
| Main Content | 940px |
| Article (Small) | 620px |
| Editor | 580px |

### Breakpoints

| Name | Width |
|------|-------|
| XS | 361px |
| SM | 481px |
| MD | 769px |
| LG | 941px |
| XL | 1280px |

---

## 7. Do's and Don'ts

### Do（推奨）

- テキスト色は `#08131a`（ほぼ黒）を使い、純粋な `#000000` を避ける
- 記事本文は `font-size: 18px` + `line-height: 2.0` で組む
- `letter-spacing: 0.04em` と `palt` は見出し (h1, h2) にのみ適用する
- 記事コンテンツ幅は 620px を維持する

### Don't（禁止）

- 純粋な `#000000` をテキストに使わない
- 記事コンテンツ幅を 620px 以上にしない
- ブランドカラー `#5ac8b8` をテキストに使わない（コントラスト不足）
- `letter-spacing: 0.04em` や `palt` を本文 (p) に適用しない

---

## 9. Agent Prompt Guide

```
Brand Color: #5ac8b8（ロゴ・アクセント用）
CTA Background: #08131a（ライトモード）
Text Primary: #08131a
Text Secondary: rgba(8,19,26,0.66)
Background: #ffffff
Background Secondary: #f5f8fa
Border: rgba(8,19,26,0.14)
Like Color: #d13e5c
Focus Ring: #292d9e

Sans-Serif Font: "Helvetica Neue", "Hiragino Sans",
  "Hiragino Kaku Gothic ProN", Arial, "Noto Sans JP", Meiryo, sans-serif
Serif Font: "Hiragino Mincho ProN", "Hiragino Mincho Pro", HGSMinchoE,
  "Yu Mincho", YuMincho, "MS PMincho", serif

Body Size (top): 16px / line-height: 1.5 / letter-spacing: normal
Body Size (article): 18px / line-height: 2.0 / letter-spacing: normal
Heading: letter-spacing: 0.04em + font-feature-settings: "palt"
Article Width: 620px
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
