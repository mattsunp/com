# DESIGN.md — LINE

> このファイルはAIエージェントが正確な日本語UIを生成するためのデザイン仕様書です。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: クリーン、信頼感、大きくシンプルなタイポグラフィ
- **密度**: ゆったりとしたランディング型。body font-size 20px と大きめの設定
- **キーワード**: グリーン、大胆、メッセンジャー、親しみやすい、モダン

---

## 2. Color Palette & Roles

### Primary（ブランドカラー）

- **LINE Green** (`#06c755`): メインのブランドカラー。CTAボタン、アクセント等に使用
- **LINE Green Dark** (`#05b34c`): ホバー・プレス時

### Semantic（意味的な色）

- **Danger** (`#d93025`)
- **Warning** (`#f9ab00`)
- **Success** (`#06c755`)（LINE Green と共用）

### Neutral（ニュートラル）

- **Text Primary** (`#000000`)
- **Text Secondary** (`#666666`)
- **Text Disabled** (`#999999`)
- **Border** (`#e5e5e5`)
- **Background** (`#ffffff`)
- **Surface** (`#f7f8f9`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
font-family: SFPro, Arial, "Noto Sans JP", "Noto Sans KR", sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height | 備考 |
|------|------|--------|-------------|------|
| Hero (EN) | 70px | 700 | normal | 英語ヒーロー |
| Heading 2 (JP) | 60px | 700 | ~1.3 | 日本語大見出し |
| Body | 20px | 400 | normal | 本文（非常に大きい） |

### 3.5 行間・字間

- **本文の行間**: normal（ブラウザデフォルト）
- **字間**: normal

---

## 4. Component Stylings

### Buttons

**Primary（LINE Green CTA）**
- Background: `#06c755`
- Text: `#ffffff`
- Padding: 12px 32px
- Border Radius: 8px
- Font Weight: 700

### Cards

- Background: `#ffffff`
- Border: 1px solid `#e5e5e5`
- Border Radius: 12px
- Padding: 24px
- Shadow: `0 2px 8px rgba(0,0,0,0.08)`

---

## 5. Layout Principles

### Spacing Scale

| Token | Value |
|-------|-------|
| XS | 4px |
| S | 8px |
| M | 16px |
| L | 24px |
| XL | 40px |
| XXL | 64px |

### Container

- Max Width: 1120px
- Padding (horizontal): 24px
- Grid: 12 columns, 24px gutter

---

## 7. Do's and Don'ts

### Do（推奨）

- LINE Green `#06c755` をCTAやアクセントに一貫して使用する
- body font-size は 20px を維持する
- 見出しは 60-70px の大きなサイズで大胆に表示する
- 韓国語フォールバック（Noto Sans KR）を含める

### Don't（禁止）

- LINE Green 以外のブランドカラーをCTAに使わない
- body font-size を 20px 未満に変更しない
- palt を本文に適用しない

---

## 9. Agent Prompt Guide

```
Primary Color: #06c755 (LINE Green)
Text Color: #000000
Background: #ffffff
Font: SFPro, Arial, "Noto Sans JP", "Noto Sans KR", sans-serif
Body Size: 20px
Line Height: normal
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
