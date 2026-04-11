# DESIGN.md — Notion 日本語版

> Notionのデザイン仕様書。日本語版トップは #191918 のダーク背景を使用。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: ミニマル、ツールライク、ダーク基調のランディングページ
- **キーワード**: ミニマル、プロフェッショナル、モノクロ、ダーク、ドキュメント指向

---

## 2. Color Palette & Roles

### Primary

- **Accent** (`#2383E2`): リンク、インラインハイライト

### Semantic

- **Danger** (`#EB5757`) / **Warning** (`#F2C94C`) / **Success** (`#6FCF97`)

### Neutral（ダークモード）

- **Text Primary** (`rgba(255,255,255,0.95)`)
- **Text Secondary** (`rgba(255,255,255,0.6)`)
- **Border** (`rgba(255,255,255,0.13)`)
- **Background** (`#191918`): ダーク背景（日本語版LP）
- **Surface** (`#2F2F2F`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
font-family: NotionInter, Inter, -apple-system, "system-ui", "Segoe UI",
  Helvetica, "Apple Color Emoji", Arial, sans-serif;
```

（和文フォントは明示指定せず OS のシステムフォントスタックに委ねる）

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display | 64px | 700 | 1.0 |
| Heading 1 | 54px | 700 | 1.04 |
| Heading 2 | 22px | 700 | 1.27 |
| Body | 16px | 400 | 1.5 |
| Caption | 14px | 400 | 1.43 |

### 行間・字間

- **本文**: `line-height: 1.5` / **大見出し**: `line-height: 1.0`（タイト）
- **字間**: normal / **palt**: 未使用
- **font-feature-settings**: `"lnum", "locl" 0`（数字をベースラインに揃える）

---

## 4. Component Stylings

### Buttons

**Primary（ダーク背景上の白ボタン）**
- Background: `#FFFFFF` / Text: `#191918`
- Padding: 8px 16px / Border Radius: 8px / Weight: 500

**Secondary（ゴースト）**
- Background: `transparent` / Text: `rgba(255,255,255,0.95)`
- Border: 1px solid `rgba(255,255,255,0.2)` / Border Radius: 8px

### Cards

- Background: `#2F2F2F`
- Border: 1px solid `rgba(255,255,255,0.08)`
- Border Radius: 12px
- Shadow: `0 2px 8px rgba(0,0,0,0.2)`

---

## 7. Do's and Don'ts

### Do（推奨）

- ダーク背景には `#191918` を使い、純粋な `#000000` は避ける
- 数字表示には `font-feature-settings: "lnum"` を有効にする
- テキストカラーには `rgba()` で透明度で階層を表現する
- 日本語本文は line-height: 1.5 以上を確保する

### Don't（禁止）

- 大見出しの line-height を 1.5 にしない（1.0〜1.1 でタイトに）
- letter-spacing を大きく広げない

---

## 9. Agent Prompt Guide

```
Primary Color: #FFFFFF（ダーク上CTA）
Text Color: rgba(255,255,255,0.95)（ダーク）
Background: #191918（ダーク）/ #FFFFFF（ライト）
Accent: #2383E2
Font: NotionInter, Inter, -apple-system, "system-ui", "Segoe UI",
  Helvetica, "Apple Color Emoji", Arial, sans-serif
Body Size: 16px / Line Height: 1.5
font-feature-settings: "lnum", "locl" 0
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
