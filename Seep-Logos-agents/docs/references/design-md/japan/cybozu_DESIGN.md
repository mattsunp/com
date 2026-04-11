# DESIGN.md — サイボウズ (cybozu.co.jp)

> サイボウズのデザイン仕様書。CSS Custom Properties は未使用の伝統的なCSS構成。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 企業理念「チームワークあふれる社会を創る」を反映した、誠実で温かみのあるコーポレートデザイン
- **キーワード**: 誠実、チームワーク、読みやすい、ゆったり、信頼感
- **特徴**: line-height: 2.0 のグローバル適用。ヒラギノ角ゴ Pro（ProNではなく Pro = JIS90字形）

---

## 2. Color Palette & Roles

- **Text Primary** (`#333`): 本文テキスト
- **Background** (`#fff`): ページ背景

（体系的なカラートークンは未確認。コーポレートサイトのためシンプルな構成）

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* 和文名を先に指定する和文優先アプローチ */
font-family: "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro",
  Meiryo, メイリオ, "ＭＳ Ｐゴシック", "MS PGothic", sans-serif;
```

**特徴**:
- ヒラギノ角ゴ **Pro**（ProN ではない）= JIS90字形
- 全角フォント名（`"ＭＳ Ｐゴシック"`）も含めてレガシー環境に対応

### 3.4 文字サイズ・ウェイト階層

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Body | 16px | 400 | **2.0** |
| Body Bold | 16px | 700 | 2.0 |
| Heading 2 | 16px | 400 | 2.0 |

### 行間・字間

- **line-height: 2.0 をグローバルに適用**（note の記事本文と同じ水準）
- **字間**: normal / **palt**: 未使用

---

## 7. Do's and Don'ts

### Do（推奨）

- line-height: 2.0 をグローバルに適用し、ゆったりとした読書体験を維持する
- フォントスタックは和文名を先に記述する（「ヒラギノ角ゴ Pro W3」が先頭）
- テキストカラーは #333 を使い、純粋な #000000 は避ける

### Don't（禁止）

- line-height を 1.5 以下に下げない
- ヒラギノ角ゴ ProN と Pro を混在させない（字形が異なる）
- palt を本文に適用しない

---

## 9. Agent Prompt Guide

```
Text Color: #333 / Background: #fff
Font: "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", Meiryo, メイリオ,
  "ＭＳ Ｐゴシック", "MS PGothic", sans-serif
Body Size: 16px / Line Height: 2.0
palt: なし / CSS Custom Properties: なし
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
