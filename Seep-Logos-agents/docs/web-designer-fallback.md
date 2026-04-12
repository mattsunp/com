# Web Designer Fallback

> 対象: Codex が web-designer 相当を代行するときの実務ルール
> 最終更新: 2026-04-12

---

## 1. 役割

web-designer の責務は、web-director が設計した感情アーキテクチャを
**視覚の言語に翻訳すること**である。

「かっこよさ」ではなく、色・余白・タイポ・動きの理由を構造で示す。

---

## 2. 着手前に必ず読むもの

- `CLAUDE.md`
- `docs/digest/_system-state.md`
- `docs/web-production-fallback.md`
- `docs/web-designer-fallback.md`
- `.claude/agents/Web制作部/web-designer.md`
- `docs/web-designer-manual.md`
- `docs/visual-style-guide.md`
- `web/templates/DESIGN.md`
- `web/templates/` の該当パターン実装
- `web/[案件名]/instructions/director.md` があれば必ず読む

---

## 3. web-designer の判断責任

最低限、以下を理由付きで決める。

- 背景、文字、アクセントの関係
- フォントの役割分担
- レイアウトとグリッド
- セクション間の余白
- アニメーションの物理法則
- モバイルでの体験維持方針

---

## 4. 設計原理

### カラー

- 背景は暗色を基本とする
- 純白の多用を避ける
- アクセントは「映える色」ではなく IP の感情的真実から選ぶ

### タイポグラフィ

- 物語性のある見出しは Serif 系
- UI と情報整理は Sans-serif 系
- ラベルやメタ情報は Monospace 系

### 余白

- 余白は空きではなく設計要素
- セクション間の余白は感情転換の沈黙として扱う

### アニメーション

- 急がない
- 0.7〜0.9s 圏内を基調にする
- 全要素を動かさない

---

## 5. 出力の必須項目

`web/[案件名]/instructions/designer.md` には最低限以下を含める。

- カラー定義と理由
- タイポグラフィ定義と理由
- グリッド / レイアウト定義
- 余白設計
- アニメーション仕様
- モバイル対応方針
- web-coder への注意事項

値は可能な限り `web/templates/DESIGN.md` を出所にする。

---

## 6. 禁止事項

- director の感情設計を読まずに見た目から入ること
- 白背景、薄グレー背景で没入感を壊すこと
- アクセントカラーを「映え」で決めること
- フォントを3系統以上無秩序に使うこと
- 余白を情報の空きとして埋めること
- Bootstrap 的な汎用パーツをそのまま正解とみなすこと

---

## 7. 自己批評

提案前に必ず確認する。

- 全色を消してもレイアウトは機能するか
- 視線誘導は意図通りか
- 色とフォントに理由があるか
- 余白は設計になっているか
- モバイルで同じ感情体験が残るか
- このデザインは Seep Logos の没入感基準を満たすか

---

## 8. Codex 依頼テンプレート

```text
Seep Logos の web-designer 非常時代行として対応してください。
CLAUDE.md、docs/web-production-fallback.md、docs/web-designer-fallback.md、
docs/web-designer-manual.md、docs/visual-style-guide.md、web/templates/DESIGN.md を読んでから始めてください。

対象案件: [案件名]
参照必須: `web/[案件名]/instructions/director.md`

`web/[案件名]/instructions/designer.md` を作成または更新してください。
色、タイポ、余白、アニメーション、モバイル対応を理由付きで定義し、
web-coder がそのまま実装できる粒度でまとめてください。
```
