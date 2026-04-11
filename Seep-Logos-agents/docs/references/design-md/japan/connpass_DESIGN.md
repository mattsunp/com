# DESIGN.md — connpass

> connpass（https://connpass.com/）のデザイン仕様書。エンジニア向けイベント管理サービス。

---

## 1. Visual Theme & Atmosphere

- **デザイン方針**: 実用的、シンプル、情報密度重視。エンジニア向けに最適化されたUI
- **キーワード**: 実用的、シンプル、情報密度、エンジニア向け、フラット
- **特徴**: Lucida Grande を先頭に指定する欧文優先のフォントスタック。body 12px の情報密度優先設計

---

## 2. Color Palette & Roles

### Primary

- **connpass Orange** (`#f18d05`): ブランドカラー
- **Red** (`#e8283f`): セカンダリカラー

### Neutral

- **Border** (`#ddd`)

---

## 3. Typography Rules

### 3.3 font-family 指定

```css
/* 欧文優先スタック */
font-family: "Lucida Grande", Verdana, "ヒラギノ角ゴ ProN", "Hiragino Kaku Gothic ProN",
  Meiryo, sans-serif;
```

### 3.4 文字サイズ・ウェイト階層

- **Body**: 12px / weight 400 / line-height 1.5
- **見出し**: weight 400（サイズ差で階層表現）

### 行間・字間

- **line-height: 1.5**
- 見出し weight は 400（bold を使わずサイズで差別化）

---

## 4. Component Stylings

### Cards

- Border: `#ddd` / Shadow: なし（フラット）/ ボーダーで区切る設計

---

## 7. Do's and Don'ts

### Do（推奨）

- Lucida Grande を先頭に配置する（欧文優先）
- フラットデザインを維持（影なし、ボーダー区切り）
- 情報密度を保つ

---

## 9. Agent Prompt Guide

```
Primary Color: #f18d05 / Red: #e8283f
Font: "Lucida Grande", Verdana, "ヒラギノ角ゴ ProN", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif
Body Size: 12px / Line Height: 1.5
Heading Weight: 400（サイズ差で階層表現）
```

*Source: https://github.com/kzhrknt/awesome-design-md-jp*
