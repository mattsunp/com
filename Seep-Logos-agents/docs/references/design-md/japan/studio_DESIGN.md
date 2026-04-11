# DESIGN.md — STUDIO (studio.design)

> このファイルはAIエージェントが正確な日本語UIを生成するためのデザイン仕様書です。対象: https://studio.design/ja

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: クリーン、モダン、プロフェッショナル。ノーコードWebサイトビルダーとしての信頼感と先進性を両立
- **キーワード**: ミニマル、テック、洗練、高速、ダークテキスト on ホワイト

---

## 2. Color Palette & Roles

### Primary

- **STUDIO Blue** (`#0275fd`): アクセント、リンク、ハイライト（CTAには使わない）
- **CTA Surface** (`#222222`): CTAボタンの背景色（ほぼ黒）
- **Light Blue BG** (`#eef9ff`)

### Neutral

- **Text Primary** (`#222222`): ほぼ黒（純黒ではない）
- **Text Secondary** (`#707070`)
- **Text on Dark** (`#f7f7f7`): ダークボタン上のテキスト
- **Background** (`#ffffff`) / **Surface Light** (`#f7f7f7`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* メイン（欧文優先の和欧混植） */
font-family: Inter, "Noto Sans JP", sans-serif;

/* モリサワ（法人向けラベル限定） */
font-family: "ゴシックMB101 B JIS2004", "Hiragino Kaku Gothic ProN", sans-serif;

/* モノスペース（FOR BUSINESS等ラベル） */
font-family: "IBM Plex Mono", monospace;

/* セリフ（装飾用） */
font-family: "Instrument Serif", serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| Hero H1 | 35.04px | 600 | 1.2 | normal |
| Section H2 | 36px | 600 | 1.25 | normal |
| Body | 15.04px | 400 | 1.7 | normal |
| Nav | 14px | 500 | 14px | -0.28px |
| CTA Label | 13px | 500 | 1.2 | -0.26px |
| Mono Label | 11px | 500 | — | -0.44px |

### 行間・字間

- **本文**: `line-height: 1.7`
- **見出し**: `line-height: 1.2〜1.25`、weight: 600（semibold）
- **小さいテキスト（11〜14px）**: 負の letter-spacing を多用（Appleに似たアプローチ）
- **palt**: 未使用

---

## 4. Component Stylings

### Buttons

**Primary CTA（ピル型）**
- Background: `#222222` / Text: `#f7f7f7`
- Border Radius: **500px**（完全なピル型）
- Font Size: 13px / Weight: 500 / Letter Spacing: -0.26px

**Secondary**
- Background: `transparent` / Text: `#222222`
- Border: 1px solid `#222222` / Border Radius: 4px

> ポイント: CTAはピル型（500px）、補助ボタンは 4px の使い分けが STUDIO の特徴

---

## 7. Do's and Don'ts

### Do（推奨）

- font-family は `Inter, "Noto Sans JP", sans-serif` の順（欧文優先）
- 見出し weight は 600（semibold）を基本
- 小さいテキストには負の letter-spacing を適用
- CTAボタンは radius: 500px のピル型にする
- ブランドカラー `#0275fd` はアクセントに限定

### Don't（禁止）

- palt を適用しない / 見出しに weight 700 を使わない（600が基本）
- CTAボタンの radius を 4px にしない（ピル型でないとSTUDIOらしくない）
- ブランドブルー `#0275fd` をCTAボタンの背景にしない（CTAは `#222222`）

---

## 9. Agent Prompt Guide

```
Primary Color: #0275fd (アクセント用)
CTA Color: #222222 (ボタン背景)
Text Color: #222222 / Text Secondary: #707070
Background: #ffffff / Surface: #f7f7f7
Font: Inter, "Noto Sans JP", sans-serif
Mono: "IBM Plex Mono", monospace
Body Size: 15px / Line Height: 1.7
Heading Weight: 600
Letter Spacing (small text): -0.28px
Button Radius (CTA): 500px / Button Radius (secondary): 4px
```

### 特記事項

- **ゴシックMB101 B**: モリサワの有料フォント。法人向けラベル等で限定使用。再現時はヒラギノ角ゴ ProN で代替
- **IBM Plex Mono**: `FOR BUSINESS` 等の英字ラベルに使用

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
