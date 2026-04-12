# Web制作部 非常時代行パッケージ

> 対象: Claude Code の web制作部エージェントが使えないときの代行運用
> 適用先: web-director / web-designer / web-coder 相当の作業
> 最終更新: 2026-04-12

---

## 1. この文書の目的

Claude Code が使用制限、overloaded、または一時停止で使えない場合でも、
Seep Logos の Web 制作品質を落とさずに作業継続できるようにする。

本書は、Codex が Web制作部の専門性を**その場しのぎではなく再現可能な手順**として読み込み、代行するための入口である。

---

## 2. 基本方針

- 代行時も `CLAUDE.md` を共通憲章として扱う
- Web 制作は単発のデザイン依頼ではなく、`web-director → web-designer → web-coder` の順序依存フローで扱う
- Codex 本体の汎用判断に頼らず、既存の専門文書と成果物を明示的にロードしてから作業する
- 迷ったら「派手さ」ではなく「没入感」と「IP固有性」を優先する

---

## 3. 参照優先順位

非常時代行では、以下の順で読む。

1. `CLAUDE.md`
2. `docs/digest/_system-state.md`
3. `docs/handoff-protocol.md`
4. 本書 `docs/web-production-fallback.md`
5. `docs/web-director-fallback.md`
6. `docs/web-designer-fallback.md`
7. `docs/visual-style-guide.md`
8. `.claude/skills/web-production.md`
9. `web/templates/DESIGN.md`
10. `web/templates/` の該当パターン実装

検証依頼や設定確認を兼ねる場合は `docs/digest/_index.md` も追加で参照する。

---

## 4. 役割分担

### web-director 相当

- パターン選定
- 感情アーキテクチャ設計
- セクション順とスクロール構造設計
- フェーズ判断
- IP 固有アクセント方向性の整理

### web-designer 相当

- 色、タイポ、余白、グリッド、アニメーションの視覚仕様化
- `web-director` の設計を視覚言語へ翻訳
- `web-coder` へ渡せる設計理由付きの仕様化

### web-coder 相当

- `director.md` と `designer.md` を実装に落とす
- `web/templates/DESIGN.md` の具体値を使って HTML / CSS を構築する

---

## 5. 非常時の標準フロー

### ケースA: まだ何も始まっていない

1. `web-director` fallback で戦略設計を行う
2. `web-designer` fallback でビジュアル仕様を行う
3. 必要なら `web-coder` 相当の実装へ進む

### ケースB: director までは完了している

1. `director.md` を読み込む
2. `web-designer` fallback で視覚仕様を作る
3. 必要なら実装へ進む

### ケースC: designer 途中で停止した

1. 既存の `designer.md`、handoff、関連成果物を読む
2. すでに確定した判断と未確定部分を分ける
3. 未確定部分だけを追記する

---

## 6. Codex に依頼するときの基本文

```text
Seep Logos の Web制作部非常時代行として対応してください。
まず CLAUDE.md、docs/digest/_system-state.md、docs/web-production-fallback.md を読んでください。
今回は [web-director / web-designer / web-coder] 相当で作業してください。
既存成果物と未コミット変更は壊さず、必要なら handoff を残してください。
```

---

## 7. 品質基準

- Seep Logos の没入感を壊さない
- 汎用 LP の見た目に逃げない
- パターン選定と視覚設計に理由がある
- `web/templates/DESIGN.md` の具体値を無視しない
- モバイルでも同じ感情体験が成立する
- 代行結果を次回 Claude Code が吸収できるよう、handoff 可能な粒度で残す

---

## 8. 禁止事項

- 既存パターンや設計文書を読まずに「雰囲気」で作ること
- 白背景や薄グレー背景で没入感を壊すこと
- Bootstrap 的な汎用 UI をそのまま持ち込むこと
- director の感情設計を無視して designer を進めること
- designer の理由付き仕様なしに coder 実装へ飛ぶこと

---

## 9. 実務上の出口

作業終了時は、必要に応じて以下を残す。

- `web/[案件名]/instructions/director.md`
- `web/[案件名]/instructions/designer.md`
- 実装ファイル
- `Return Handoff`
- 重要判断があれば `minutes/` または `docs/` への反映

非常時代行の目的は、Claude Code の不在中に雑に前進することではない。
**専門性を維持したまま業務を止めないこと**である。
