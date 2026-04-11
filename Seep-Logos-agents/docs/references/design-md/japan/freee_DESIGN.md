# DESIGN.md — freee

> freee（https://www.freee.co.jp/）のデザイン仕様書。freee Vibes Design System の公式デザイントークンに基づく。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 親しみやすく、明快な業務UI。複雑な会計・人事業務を直感的で軽やかなインターフェースで提供する
- **キーワード**: 親しみやすい、明快、信頼性、シンプル、アクセシブル
- **特徴**: ブルーを基調としたクリーンな配色。プロダクトUI（Vibes）とコーポレートサイトで異なるフォント戦略

---

## 2. Color Palette & Roles

### Primary

- **Primary Blue** (`#2864f0`): CTAボタン、リンク、アクティブ状態
- **Primary Dark** (`#1e46aa`): h3 等のブルー見出し
- **Heading Blue** (`#1e46aa`): サブ見出しカラー

### Semantic

- **Danger** (`#dc1e32`) / **Warning** (`#ffb91e`) / **Success** (`#00963c`)
- **Orange** (`#fa6414`): 通知、アクセント

### Neutral

- **Text Heading** (`#323232`): 見出し、強調テキスト
- **Text Body** (`#595959`): body デフォルト（実測値）
- **Text Muted** (`#8c8c8c`): プレースホルダー
- **Background Light** (`#f7f5f5`)
- **Border** (`#e9e7e7`) / **Input Border** (`#cccccc`（実測値）)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* プロダクトUI（Vibes Design System） */
font-family: '-apple-system', BlinkMacSystemFont, 'Helvetica Neue',
  'ヒラギノ角ゴ ProN', 'Hiragino Kaku Gothic ProN', Arial,
  'メイリオ', Meiryo, sans-serif;

/* コーポレートサイト */
font-family: "Noto Sans JP", sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

**プロダクトUI（Vibes）**

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Heading 1 | 24px | 700 | 1.5 |
| Heading 2 | 16px | 700 | 1.5 |
| Body | 14px | 400 | 1.5 |
| Caption | 12px | 400 | 1.5 |

**コーポレートサイト**（実測値）

| Role | Size | Weight | Letter Spacing | Color |
|------|------|--------|----------------|-------|
| H2 (hero) | 40px | 500 | 0.04em | `#323232` |
| H2 | 34px | 500/700 | 0.04em | `#323232` |
| H3 | 24px | 500/700 | normal | `#1e46aa` |
| Body | 16px | 400 | normal | `#595959` |

- **見出し weight は 500（medium）が多い**（700は強調見出しのみ）
- プロダクトUI: `line-height: 1.5` で統一 / コーポレート: 文脈で変化

---

## 4. Component Stylings

### Buttons

**Primary（コーポレートサイト実測値）**
- Background: `#2864f0` / Text: `#fff`
- Border: 2px solid `#2864f0` / Border Radius: 8px
- Font Size: 16px / Weight: 500/700

**Secondary（ヘッダー）**
- Background: `#fff` / Text: `#2864f0`
- Border: 1px solid `#2864f0` / Border Radius: 5px

### Cards

- Background: `#ffffff`
- Border Radius: 0.75rem (12px)
- Shadow: `0 0 1rem rgba(0,0,0,0.1), 0 0.125rem 0.25rem rgba(0,0,0,0.2)`

---

## 5. Layout Principles

### Spacing Scale（Vibes）

```
XSmall: 4px / Small: 8px / Basic: 16px / Large: 24px / XLarge: 32px / XXLarge: 48px
```

### Border Radius Scale（Vibes）

```
Base: 8px / Card: 12px / Floating: 16px / Dialog: 24px / Full: 99rem
```

---

## 7. Do's and Don'ts

### Do（推奨）

- コーポレートサイトのボタンは `border-radius: 8px`（Vibes のピル型は使わない）
- 見出し weight は `500`（medium）を基本とし、強調時のみ `700`
- 大見出し（34px以上）には `letter-spacing: 0.04em`
- 色のコントラスト比は WCAG AA 以上を確保する

### Don't（禁止）

- テキスト色に `#000000` を使わない（`#323232` / `#595959` を使用）
- ブランドブルー `#2864f0` の上に暗いテキストを置かない
- プロダクトUIに Noto Sans JP を使わない（パフォーマンスへの影響）

---

## 9. Agent Prompt Guide

```
Primary Color: #2864f0
Heading Blue: #1e46aa
Text Heading: #323232
Text Body (default): #595959
Background: #ffffff / Surface Light: #f7f5f5
Border: #e9e7e7 / Input Border: #cccccc
Danger: #dc1e32

Product UI Font: '-apple-system', BlinkMacSystemFont, 'Helvetica Neue',
  'ヒラギノ角ゴ ProN', 'Hiragino Kaku Gothic ProN', Arial, 'メイリオ', Meiryo, sans-serif
Website Font: "Noto Sans JP", sans-serif
Body Size (Product): 14px / Body Size (Website): 16px
Line Height: 1.5（全体統一）
Heading Weight: 500（強調時700）
Button Radius (Website): 8px / Button Radius (Product): 99rem
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
