# DESIGN.md — Novasell

> Novasell（https://novasell.com/）のデザイン仕様書。ラクスルグループのAIマーケティングエージェンシー。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 大胆でエネルギッシュなエージェンシーデザイン。超巨大タイポグラフィとネオングリーンで強い印象
- **密度**: 極めてゆったり。1セクション=1メッセージの大胆な構成
- **キーワード**: 大胆、エネルギッシュ、ネオン、モノクロ+アクセント、テクノロジー感
- **特徴**: 全テキスト `font-weight: 700`（bold）。Display 書体に最大 486px のサイズ。ネオングリーン `#00fa27` がブランドカラー

---

## 2. Color Palette & Roles

### Primary（CSS Custom Properties）

- **Novasell Green** (`#00fa27` / `--color--green`): ブランドカラー
- **Black** (`#000` / `--color--black`)
- **White** (`#fff` / `--color--white`)
- **Near Black** (`#101112`): ヘッダーリンク等
- **Error Red** (`#e4250e`): フォームエラー
- **Green Link** (`#00aa14`): テキストリンク

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* 和文本文・UI */
font-family: "Zen Kaku Gothic New", sans-serif;

/* 巨大 Display（gazzetta-variable / Adobe Fonts） */
font-family: gazzetta-variable, sans-serif;

/* 欧文ラベル・中見出し（neue-haas-grotesk / Adobe Fonts） */
font-family: neue-haas-grotesk-display, sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

**gazzetta-variable（Display用）**

| Size | Weight | Line Height | Letter Spacing | 備考 |
|------|--------|-------------|----------------|------|
| 486px | 700 | 0.5 | normal | 背景装飾テキスト（#00fa27） |
| 390px | 400 | 0.8 | -7.8px | "FREE ANALYSIS" |
| 160px | 400 | 0.75 | normal | "OUR SERVICES" |

**Zen Kaku Gothic New（和文）**

| Size | Weight | Line Height | Letter Spacing | 備考 |
|------|--------|-------------|----------------|------|
| 106px | 700 | 1.0 | -7.95px | 和文Display |
| 40px | 700 | 1.2 | -0.24px | キャッチコピー |
| 16px | 700 | 1.75 | normal | body デフォルト |

### 行間・字間

- **全テキスト font-weight: 700**（gazzetta-variable の一部 weight 400 を除く）
- 巨大 Display: `line-height: 0.5〜1.0`（極めてタイト）
- 和文本文: `line-height: 1.75`
- 大きいサイズほど強い負の letter-spacing
- **palt**: 未使用

---

## 4. Component Stylings

### Buttons

**Primary（"資料請求"）**
- Background: `#000` / Text: `#fff`
- Border Radius: 16.5px（ピル型）/ Font Size: 12px / Weight: 700

**Secondary（"お問い合わせ"）**
- Background: `#fff` / Text: `#000` / Border Radius: 16.5px

---

## 7. Do's and Don'ts

### Do（推奨）

- 全テキストを `font-weight: 700` にする
- ネオングリーン `#00fa27` を大胆に使う（背景・テキスト両方）
- Display 見出しは 100px 以上で超巨大に
- 大きいサイズほど letter-spacing を負にする
- 黒背景 + ネオングリーンを基本とする

### Don't（禁止）

- font-weight: 400 を和文テキストに使わない
- 見出しを小さくしない（最低 40px 以上）
- 影やグラデーションを使わない

---

## 9. Agent Prompt Guide

```
Novasell Green: #00fa27 / Black: #000 / White: #fff / Error: #e4250e

JP Font: "Zen Kaku Gothic New", sans-serif (all bold)
Display Font: gazzetta-variable, sans-serif
Label Font: neue-haas-grotesk-display, sans-serif

Body: 16px / weight: 700 / line-height: 1.75
JP Heading: 40px / weight: 700 / line-height: 1.2
Display EN: 100px+ / gazzetta-variable
All text: font-weight: 700
Letter Spacing: 大きいサイズほど負に詰める
Button: 12px / radius: 16.5px（ピル型）
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
