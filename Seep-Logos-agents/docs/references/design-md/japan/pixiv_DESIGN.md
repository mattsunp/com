# DESIGN.md — pixiv

> このファイルはAIエージェントが正確な日本語UIを生成するためのデザイン仕様書です。
> セクションヘッダーは英語、値の説明は日本語で記述しています。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: クリーン、機能的、コンテンツ中心のギャラリーUI
- **密度**: 情報密度が高いグリッドレイアウト（イラスト一覧）と、ゆったりとした作品詳細ページの二面構成
- **キーワード**: クリエイティブ、鮮明、軽快、ギャラリー的、システマティック

---

## 2. Color Palette & Roles

### Primary（ブランドカラー）

- **Primary / pixiv Blue** (`#0096fa`): メインのブランドカラー。CTAボタン、リンク、アクセント要素に使用
- **Primary Dark** (`#0069b5`): ホバー・プレス時のプライマリカラー

### Semantic（意味的な色）

- **Danger** (`#ff0000`): エラー、削除、危険な操作
- **Warning** (`#f5a623`): 警告、注意喚起
- **Success** (`#00c853`): 成功、完了
- **Like / Bookmark** (`#ff4060`): いいね、ブックマーク

### Neutral（ニュートラル）

- **Text Primary** (`#464a4d`): 本文テキスト
- **Text Secondary** (`#8c8c8c`): 補足テキスト、ラベル
- **Text Disabled** (`#b8b8b8`): 無効状態のテキスト
- **Border** (`#d6d6d6`): 区切り線、入力欄の枠
- **Background** (`#eeeeee`): ページ背景
- **Surface** (`#ffffff`): カード、モーダル等の面

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* 本文（システムフォントスタック） */
font-family: system-ui, -apple-system, "Segoe UI", Roboto, Ubuntu, Cantarell, "Noto Sans", sans-serif;

/* 等幅 */
font-family: SFMono-Regular, Consolas, Menlo, monospace;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height | 備考 |
|------|------|--------|-------------|------|
| Body (default) | 12px | 400 | 18px (×1.5) | body 要素のデフォルト |
| Body Text | 14px | 400 | 22px (×1.57) | 段落テキスト |
| Link | 14px | 400 | 22px | アンカーテキスト |
| Caption | 10px | 400 | 14px | 最小テキスト |

### 3.5 行間・字間

- **本文の行間**: 1.5
- **字間**: normal（全体）
- **palt**: 未使用

---

## 4. Component Stylings

### Buttons

**Primary**
- Background: `#0096fa`
- Text: `#ffffff`
- Padding: 8px 24px
- Border Radius: 4px
- Font Weight: 700

**Like / Bookmark**
- Text/Icon: `#ff4060`
- Border: 1px solid `#ff4060`
- Border Radius: 20px

### Inputs

- Background: `#ffffff`
- Border: 1px solid `#d6d6d6`
- Border (focus): 1px solid `#0096fa`
- Border Radius: 4px
- Height: 36px

### Cards

- Background: `#ffffff`
- Border Radius: 4px
- Shadow: `0 1px 4px rgba(0,0,0,0.08)`

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

- Max Width: 1224px
- Padding (horizontal): 16px

---

## 7. Do's and Don'ts

### Do（推奨）

- システムフォントスタックを使用し、Web フォントの読み込みを省略する
- ブランドカラー `#0096fa` を CTA やリンクの主要色として一貫して使用する
- 背景 `#eee` とカード白 `#fff` のコントラストで情報の層を作る
- テキスト色は `#464a4d` を使用し、純粋な黒を避ける

### Don't（禁止）

- body の font-size を 12px 未満にしない
- 作品サムネイルにアスペクト比の歪みを発生させない
- `#0096fa` 以外の色をプライマリアクションに使用しない
- テキスト色に純粋な `#000000` を使わない

---

## 8. Responsive Behavior

### Breakpoints

| Name | Width |
|------|-------|
| Mobile | ≤ 767px |
| Tablet | ≤ 1023px |
| Desktop | > 1023px |

---

## 9. Agent Prompt Guide

```
Primary Color: #0096fa
Text Color: #464a4d
Background: #eeeeee
Surface: #ffffff
Font: system-ui, -apple-system, "Segoe UI", Roboto, Ubuntu, Cantarell, "Noto Sans", sans-serif
Body Size: 12px (default) / 14px (paragraph)
Line Height: 1.5
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
