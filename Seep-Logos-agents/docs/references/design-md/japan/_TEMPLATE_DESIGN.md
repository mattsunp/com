# DESIGN.md — [サービス名]

> このファイルはAIエージェントが正確な日本語UIを生成するためのデザイン仕様書です。
> セクションヘッダーは英語、値の説明は日本語で記述しています。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: （例: クリーン、プロフェッショナル、温かみのある）
- **密度**: （例: 情報密度が高い業務UI / ゆったりとしたメディア型）
- **キーワード**: （3〜5つの形容詞でデザインの雰囲気を表現）

---

## 2. Color Palette & Roles

### Primary（ブランドカラー）

- **Primary** (`#______`): メインのブランドカラー。CTAボタン、リンク等に使用
- **Primary Dark** (`#______`): ホバー・プレス時のプライマリカラー

### Semantic（意味的な色）

- **Danger** (`#______`): エラー、削除、危険な操作
- **Warning** (`#______`): 警告、注意喚起
- **Success** (`#______`): 成功、完了

### Neutral（ニュートラル）

- **Text Primary** (`#______`): 本文テキスト
- **Text Secondary** (`#______`): 補足テキスト、ラベル
- **Text Disabled** (`#______`): 無効状態のテキスト
- **Border** (`#______`): 区切り線、入力欄の枠
- **Background** (`#______`): ページ背景
- **Surface** (`#______`): カード、モーダル等の面

---

## 3. Typography Rules

### 3.1 和文フォント

- **ゴシック体**: （例: Noto Sans JP, 游ゴシック, ヒラギノ角ゴ ProN）
- **明朝体**（使用する場合）: （例: Noto Serif JP, 游明朝, ヒラギノ明朝 ProN）

### 3.2 欧文フォント

- **サンセリフ**: （例: Helvetica Neue, Arial）
- **等幅**: （例: SFMono-Regular, Consolas, Menlo）

### 3.3 font-family 指定

```css
/* 本文 */
font-family: "和文フォント", "欧文フォント", sans-serif;

/* 等幅 */
font-family: "等幅フォント", monospace;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Font | Size | Weight | Line Height | Letter Spacing | 備考 |
|------|------|------|--------|-------------|----------------|------|
| Display | — | —px | — | — | — | ページタイトル等 |
| Heading 1 | — | —px | — | — | — | セクション見出し |
| Heading 2 | — | —px | — | — | — | サブ見出し |
| Body | — | —px | — | — | — | 本文 |
| Caption | — | —px | — | — | — | 補足、注釈 |

### 3.5 行間・字間

- **本文の行間 (line-height)**: （例: 1.7〜2.0）
- **見出しの行間**: （例: 1.3〜1.5）
- **本文の字間 (letter-spacing)**: （例: 0.04em）
- **palt**: 使用する/しない

### 3.6 禁則処理・改行ルール

```css
word-break: break-all;
overflow-wrap: break-word;
line-break: strict;
```

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#______` / Text: `#______`
- Padding: —px —px / Border Radius: —px / Weight: —

**Secondary**
- Background: `transparent` / Text: `#______`
- Border: 1px solid `#______`

### Inputs

- Background: `#______`
- Border: 1px solid `#______`
- Border (focus): 1px solid `#______`
- Border Radius: —px / Font Size: —px / Height: —px

### Cards

- Background: `#______`
- Border Radius: —px / Padding: —px

---

## 5. Layout Principles

### Spacing Scale

| Token | Value |
|-------|-------|
| XS | 4px |
| S | 8px |
| M | 16px |
| L | 24px |
| XL | 32px |
| XXL | 48px |

### Container

- Max Width: —px / Padding (horizontal): —px

---

## 7. Do's and Don'ts

### Do（推奨）

- フォントは必ずフォールバックチェーンを指定する
- 日本語本文の line-height は 1.5 以上にする

### Don't（禁止）

- font-family に和文フォント1つだけを指定しない
- 日本語本文に line-height: 1.2 以下を使わない

---

## 9. Agent Prompt Guide

```
Primary Color: #______
Text Color: #______
Background: #______
Font: "和文フォント", "欧文フォント", sans-serif
Body Size: __px / Line Height: __
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp (template)*
