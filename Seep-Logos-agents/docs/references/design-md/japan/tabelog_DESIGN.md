# DESIGN.md — 食べログ (tabelog.com)

> このファイルはAIエージェントが正確な日本語UIを生成するためのデザイン仕様書です。CSS Custom Properties は未使用。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 情報密度が高く、テキスト中心の実用的なグルメ・レビューポータル
- **密度**: 高密度。body 12px を基本とし、一覧ページに多くの店舗情報を詰め込む
- **キーワード**: 実用的、情報密度、スコア重視、オレンジ、レビュー文化
- **特徴**: 日本語名を先に指定する旧来の慣習（「メイリオ」が先）。CSS Custom Properties なし

---

## 2. Color Palette & Roles

### Primary

- **食べログオレンジ** (`#f09000`): ロゴ、評価スコア、ハイライト
- **Dark** (`#d07e00`): ホバー時

### Semantic

- **Danger** (`#cc3333`) / **Success** (`#339933`)
- **Score High** (`#f09000`) / **Score Low** (`#666666`)

### Neutral

- **Text Primary** (`#595960`) / **Text Heading** (`#333333`)
- **Border** (`#dddddd`) / **Background** (`#ffffff`)
- **Background Secondary** (`#f5f5f5`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
font-family: メイリオ, Meiryo, "Hiragino Sans", ヒラギノ角ゴシック,
  "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Section Heading | 22.5px | 600 | 1.0 |
| Body | 12px | 400 | 1.4 |
| Score | 16px | 700 | 1.2 |
| Caption | 10px | 400 | 1.4 |

### 行間・字間

- **本文**: `line-height: 1.4`（情報密度優先）
- **字間**: normal / **palt**: 未使用

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#f09000` / Text: `#ffffff`
- Border Radius: 3px / Font Size: 12px / Weight: 700

### Cards（店舗カード）

- Background: `#ffffff`
- Border: 1px solid `#dddddd`
- Border Radius: 0px / Shadow: none

---

## 7. Do's and Don'ts

### Do（推奨）

- body のフォントサイズは 12px を守る（情報密度が崩れる）
- 評価スコアには `#f09000` を使用
- ボーダー `#dddddd` でフラットに区切る
- 角丸は 3px 以下

### Don't（禁止）

- line-height を 1.5 以上に広げない
- CSS Custom Properties を追加しない
- 欧文フォントを先頭に置かない（和文優先スタック）

---

## 9. Agent Prompt Guide

```
Primary Color: #f09000
Text Color: #595960 / Heading Color: #333333
Background: #ffffff / Border: #dddddd
Font: メイリオ, Meiryo, "Hiragino Sans", ヒラギノ角ゴシック, "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", sans-serif
Body Size: 12px / Line Height: 1.4
Score Color: #f09000 / palt: 未使用 / CSS Variables: なし
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
