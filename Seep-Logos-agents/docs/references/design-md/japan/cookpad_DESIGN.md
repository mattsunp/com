# DESIGN.md — クックパッド (cookpad.com)

> このファイルはAIエージェントが正確な日本語UIを生成するためのデザイン仕様書です。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 温かみのある家庭的なデザイン。料理と暮らしに寄り添う親しみやすさ
- **キーワード**: 温かみ、家庭的、親しみやすい、実用的、UGC

---

## 2. Color Palette & Roles

### Primary

- **Cookpad Orange** (`#f28c06`): CTAボタン、ロゴ
- **Dark** (`#d97a00`): ホバー時

### Semantic

- **Danger** (`#e53935`) / **Warning** (`#f9a825`) / **Success** (`#43a047`)

### Neutral

- **Text Primary** (`#0f0f0f`): ほぼ黒
- **Text Secondary** (`#757575`)
- **Border** (`#e0e0e0`)
- **Background** (`#f8f6f2`): 温かみのあるオフホワイト
- **Surface** (`#fff`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
font-family: noto-sans, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, arial, sans-serif;
```

（Adobe Fonts の noto-sans を先頭に指定）

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| Heading 1 | 18px | 600 | 1.556 | -0.4px |
| Heading 2 | 16px | 600 | 1.5 | -0.4px |
| Body | 16px | 400 | 1.5 | -0.4px |
| Label | 14px | 600 | 1.429 | -0.4px |
| Caption | 12px | 400 | 1.333 | -0.4px |

### 行間・字間

- **line-height**: 1.5
- **letter-spacing: -0.4px（全体に適用 — 詰める方向）**
- **見出し weight**: 600（semibold）/ **palt**: 未使用
- **font-feature-settings**: `"liga"`（合字を有効化）

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#f28c06` / Text: `#fff`
- Padding: 8px 24px / Border Radius: 8px / Weight: 600

### Cards

- Background: `#fff`
- Border: 1px solid `#e0e0e0`
- Border Radius: 12px
- Shadow: `0 1px 3px rgba(0,0,0,0.08)`

---

## 7. Do's and Don'ts

### Do（推奨）

- letter-spacing: -0.4px を全体に適用する（クックパッドの詰め組み）
- 背景色は #f8f6f2（温かみのあるオフホワイト）を使用する
- 見出しの weight は 600（semibold）で統一する
- font-feature-settings: "liga" を適用する

### Don't（禁止）

- 背景に純白 #ffffff を使わない
- テキスト色に `#000000` を使わない（`#0f0f0f` を使用）
- letter-spacing を 0 にしない
- 見出しに font-weight: 700 を使わない（600 が正しい）

---

## 9. Agent Prompt Guide

```
Primary Color: #f28c06
Text Color: #0f0f0f / Background: #f8f6f2
Font: noto-sans, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, arial, sans-serif
Body Size: 16px / Line Height: 1.5 / Letter Spacing: -0.4px
Heading Weight: 600 / font-feature-settings: "liga"
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
