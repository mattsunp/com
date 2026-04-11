# DESIGN.md — Qiita

> Qiita（https://qiita.com/）のデザイン仕様書。開発者コミュニティとしてコードブロックとの混植を重視。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 技術記事に特化した読みやすいデザイン。コードと日本語テキストの混植を前提とした組版
- **キーワード**: テクニカル、クリーン、読みやすい、コードフレンドリー、開発者向け
- **特徴**: YakuHanJPs（約物半角化フォント）を font-family の先頭に配置。テキスト色は `rgba(0,0,0,0.87)` で Material Design 的な opacity ベース

---

## 2. Color Palette & Roles

### Primary

- **Qiita Green** (`#55c500`): CTAボタン、リンク、アクセント
- **Qiita Green Dark** (`#468c00`): ホバー時

### Semantic

- **Danger** (`#d32f2f`) / **Warning** (`#f57c00`) / **Success** (`#388e3c`)

### Neutral

- **Text Primary** (`rgba(0,0,0,0.87)`)
- **Text Secondary** (`rgba(0,0,0,0.54)`)
- **Text Disabled** (`rgba(0,0,0,0.38)`)
- **Border** (`#e0e0e0`)
- **Background** (`#f5f6f6`)
- **Surface** (`#ffffff`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* YakuHanJPs が先頭（約物半角化）— Qiita 独自の特徴 */
font-family: YakuHanJPs, -apple-system, "system-ui", "Segoe UI",
  "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif;

/* コードブロック */
font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Body | 16px | 400 | 1.8 |
| Label | 14px | 600 | 1.5 |
| Code | 14px | 400 | 1.5 |

### 行間・字間

- **本文**: `line-height: 1.8`（ゆったりとした行間）
- **字間**: normal / **palt**: 未使用（YakuHanJPs で約物を処理）

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#55c500` / Text: `#ffffff`
- Padding: 8px 16px / Border Radius: 4px / Weight: 600

### Code Blocks

- Background: `#364549`（ダーク系）/ Text: `#e3e3e3`
- Font Family: 等幅スタック / Padding: 16px / Border Radius: 4px

### Inline Code

- Background: `#f0f0f0` / Padding: 2px 6px / Border Radius: 3px

---

## 7. Do's and Don'ts

### Do（推奨）

- font-family の先頭に YakuHanJPs を指定する（約物半角化のため）
- 本文の line-height は 1.8 にする
- テキスト色は `rgba(0,0,0,0.87)` を使用する
- コードブロックと本文の書体を明確に区別する

### Don't（禁止）

- テキスト色に純粋な `#000000` を使わない
- 本文に palt を適用しない（YakuHanJPs との二重適用）
- YakuHanJPs を省略しない

---

## 9. Agent Prompt Guide

```
Primary Color: #55c500
Text Color: rgba(0,0,0,0.87)
Background: #f5f6f6 / Surface: #ffffff
Font: YakuHanJPs, -apple-system, "system-ui", "Segoe UI",
  "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif
Code Font: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace
Body Size: 16px / Line Height: 1.8
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
