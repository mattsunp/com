# DESIGN.md — Zenn

> Zenn（https://zenn.dev/）のデザイン仕様書。CSS Custom Properties は未使用。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: クリーンで余白を活かしたモダンなデザイン。技術記事の読みやすさを重視
- **キーワード**: クリーン、モダン、テクニカル、読みやすい、ブルーアクセント
- **特徴**: テキスト色に `rgba(0,0,0,0.82)`（Qiita の 0.87 よりわずかに薄い）。CSS Custom Properties 未使用

---

## 2. Color Palette & Roles

### Primary

- **Zenn Blue** (`#3ea8ff`): CTAボタン、リンク、アクセント
- **Zenn Blue Dark** (`#0f83fd`): ホバー時

### Semantic

- **Danger** (`#f43f5e`) / **Warning** (`#f59e0b`) / **Success** (`#10b981`)

### Neutral

- **Text Primary** (`rgba(0,0,0,0.82)`)
- **Text Secondary** (`rgba(0,0,0,0.55)`)
- **Border** (`#d6e3ed`)
- **Background** (`#ffffff`)
- **Surface** (`#f1f5f9`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* YakuHanJPs（約物半角化）は未使用 — Qiita との違い */
font-family: -apple-system, "system-ui", "Hiragino Kaku Gothic ProN",
  "Hiragino Sans", Meiryo, sans-serif;

/* コードブロック */
font-family: SFMono-Regular, Consolas, Menlo, monospace;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display (h3) | 38.4px | 700 | 1.5 |
| Heading 2 | 16–16.8px | 700 | 1.5 |
| Body | 16px | 400 | 1.8 |
| Label | 14px | 600 | 1.5 |

### 行間・字間

- **本文**: `line-height: 1.8`
- **字間**: normal / **palt**: normal（適用なし）

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#3ea8ff` / Text: `#ffffff`
- Padding: 8px 24px / Border Radius: 8px / Weight: 700

### Cards

- Background: `#ffffff`
- Border: 1px solid `#d6e3ed`
- Border Radius: 12px

---

## 7. Do's and Don'ts

### Do（推奨）

- テキスト色は rgba opacity ベースで指定する
- 本文の line-height は 1.8 を維持する
- ブランドカラー #3ea8ff はリンクと CTA に限定

### Don't（禁止）

- palt を本文に適用しない
- Zenn Blue を背景色として広範囲に使わない
- CSS Custom Properties に依存しない（Zenn は CSS vars 未使用）

---

## 9. Agent Prompt Guide

```
Primary Color: #3ea8ff (Zenn Blue)
Text Color: rgba(0,0,0,0.82)
Background: #ffffff / Surface: #f1f5f9
Font: -apple-system, "system-ui", "Hiragino Kaku Gothic ProN",
  "Hiragino Sans", Meiryo, sans-serif
Body Size: 16px / Line Height: 1.8
palt: なし / CSS vars: なし
```

### Qiita との差分

| 項目 | Zenn | Qiita |
|------|------|-------|
| ブランドカラー | #3ea8ff (Blue) | #55c500 (Green) |
| テキスト色 | rgba(0,0,0,0.82) | rgba(0,0,0,0.87) |
| font-family 先頭 | -apple-system | YakuHanJPs |
| 約物半角化 | なし | あり |
| ページ背景 | #ffffff | #f5f6f6 |

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
