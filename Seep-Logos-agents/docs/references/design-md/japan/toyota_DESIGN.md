# DESIGN.md — Toyota

> トヨタ（https://toyota.jp/）のデザイン仕様書。実サイトの CSS（128件のカスタムプロパティ）に基づく。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 信頼感とイノベーション。クリーンでプロフェッショナルなデザイン。車両情報を主役に
- **キーワード**: 信頼感、クリーン、プロフェッショナル、グローバル

---

## 2. Color Palette & Roles

### Primary

- **Toyota Red** (`#eb0a1e`): ブランドカラー
- **Text Primary** (`#222222`): 本文テキスト（純黒より柔らかい）
- **Neutral Border** (`#dddddd`)
- **Surface** (`#f5f5f5`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
font-family: "SF Pro", -apple-system, "system-ui",
  "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| Display | 40px | 700 | 1.5 | 0.04em |
| Body | 16px | 400 | 1.5 | 0.04em |

- **全体に letter-spacing: 0.04em を適用**

---

## 5. Layout Principles

### Spacing Scale

XS: 4px / S: 8px / M: 16px / L: 24px / XL: 32px / XXL: 64px

### Container

- Max Width: 1200px / Padding: 20px

### Breakpoints

| Name | Width |
|------|-------|
| Mobile | ≤ 767px |
| Tablet | ≤ 1024px |
| Desktop | > 1024px |

---

## 9. Agent Prompt Guide

```
Primary Color: #eb0a1e (Toyota Red)
Text Color: #222222
Font: "SF Pro", -apple-system, "system-ui", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif
Body Size: 16px / Line Height: 1.5 / Letter Spacing: 0.04em
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
