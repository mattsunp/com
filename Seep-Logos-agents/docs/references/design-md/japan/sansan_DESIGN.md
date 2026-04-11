# DESIGN.md — Sansan

> Sansan（https://jp.sansan.com/）のデザイン仕様書。CSS カスタムプロパティ 51件。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: プロフェッショナルかつ信頼感のあるビジネスSaaS。深いネイビーブルーを基調とし、堅実さと先進性を両立
- **キーワード**: 信頼、堅実、ネイビーブルー、ビジネス、クリーン
- **特徴**: helvetica（小文字）を先頭に配置し游ゴシックと組み合わせる。大見出し 54.8px の迫力

---

## 2. Color Palette & Roles

### Primary

- **Sansan Navy** (`#042a6d`): ブランドカラー。ダークネイビーで信頼感
- **Sansan Blue** (`#2566d4`): CTAボタン、リンク、アクセント

### Semantic

- **Danger** (`#cc0000`) / **Warning** (`#f5a623`) / **Success** (`#2e8b57`)

### Neutral

- **Text Primary** (`#1a1a1a`) / **Text Secondary** (`#666666`)
- **Border** (`#dddddd`) / **Background** (`#ffffff`) / **Surface** (`#f5f5f5`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* 欧文優先スタック（helveticaは小文字指定） */
font-family: helvetica, arial, YuGothic, "Yu Gothic",
  "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display | 54.8px | 700 | 1.4 |
| Heading 1 | 40px | 700 | 1.4 |
| Heading 2 | 28px | 700 | 1.4 |
| Body | 14px | 400 | **1.0**（！） |
| Caption | 12px | 400 | 1.0 |

**注意**: body line-height: 1.0 はSansan固有の設定。コンポーネント単位で 1.5〜1.8 に上書き推奨。

### 行間・字間

- **見出し**: `line-height: 1.4` / **本文**: `line-height: 1.0`（リセット用。コンポーネントで上書き）
- **字間**: normal / **palt**: 未使用

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#2566d4` / Text: `#ffffff`
- Padding: 12px 32px / Border Radius: 4px / Weight: 700

**Navy（ダーク背景用）**
- Background: `#042a6d` / Text: `#ffffff`

### Cards

- Background: `#ffffff`
- Border Radius: 8px
- Shadow: `0 2px 8px rgba(0,0,0,0.08)`

---

## 7. Do's and Don'ts

### Do（推奨）

- helvetica は小文字で指定する（font-family: helvetica）
- 游ゴシックは macOS / Windows 両対応のフォールバックを記述
- 見出しの line-height は 1.4 を維持

### Don't（禁止）

- 日本語長文本文に line-height: 1.0 をそのまま使わない（コンポーネントで上書き）
- Sansan Navy をテキストカラーとして使わない（背景色として使用）

---

## 9. Agent Prompt Guide

```
Primary Color (Navy): #042a6d / Primary Color (Blue): #2566d4
Text Color: #1a1a1a / Background: #ffffff
Font: helvetica, arial, YuGothic, "Yu Gothic", "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", sans-serif
Body Size: 14px / Line Height: 1.0（コンポーネントで1.5〜1.8に上書き）
Heading Line Height: 1.4
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
