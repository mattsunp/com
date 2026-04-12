# Handoff Sample Collection

> 対象: Claude Code と Codex の実運用サンプル
> 参照元: `docs/handoff-protocol.md`
> 最終更新: 2026-04-12

---

## 1. この文書の使い方

この文書は、handoff を実際にどう書くかの見本集である。

最初から完全な文章を書く必要はない。
重要なのは、次の担当 AI が**誤解なく再開できるだけの要点**が揃っていることだ。

---

## 2. サンプルA: Claude Code → Codex

想定:
`Claude Code` が overloaded になり、`queue/web/` の案件整理を Codex に代行させるケース。

```md
# Handoff

## 目的
- `queue/web/web-mnemosyne-lp-20260330-html.yaml` を基準に、現行の HTML 制作フローを見直したい

## 背景
- Web 制作フローを queue ベースで再利用しやすくしたい
- Claude 側で方針整理までは済んだが、実ファイルの整備途中で停止した

## 参照必須
- `CLAUDE.md`
- `docs/digest/_system-state.md`
- `docs/handoff-protocol.md`
- `queue/web/web-mnemosyne-lp-20260330-html.yaml`
- `docs/orchestration-queue-schema.md`

## 現在地
- queue の命名と項目粒度は概ね固まっている
- ただし、再利用時に説明不足になる項目が残っている

## 決定事項
- `CLAUDE.md` を共通憲章として扱う
- queue は案件の進行メモではなく、再利用可能な制作指示として整える

## 未解決事項
- どこまでテンプレート化するか
- Web 制作部向けの補足説明を queue 側に入れるか、docs 側に寄せるか

## 触ってよい範囲
- `queue/web/`
- `docs/` の補助文書

## 触らないでほしい範囲
- `docs/digest/`
- `minutes/` の既存議事録
- `.reminiscence/`

## 次アクション
- 対象 YAML を読んで、再利用の妨げになる不足項目を洗い出す
- 必要なら queue か docs のどちらに追記すべきか判断する

## 記録先
- 重要な運用判断が出たら `docs/` の運用文書に反映
- 次回 Claude に戻すための要点は Return Handoff で返す
```

---

## 3. サンプルB: Codex → Claude Code

想定:
Codex が `docs/` を整備した後、`Claude Code` に再吸収させるケース。

```md
# Return Handoff

## 実施内容
- `docs/codex-collaboration.md` を追加
- `docs/handoff-protocol.md` を追加
- `docs/_index.md` に導線を追加

## 変更ファイル
- `docs/codex-collaboration.md`
- `docs/handoff-protocol.md`
- `docs/_index.md`

## 判断事項
- `CLAUDE.md` は共通憲章として維持
- Codex は司令塔ではなく、共有記録へ戻せる実務担当として定義
- AI 間の継続性は内部記憶共有ではなく handoff と共有記録で担保する

## 残課題
- `CLAUDE.md` 側に共通憲章である旨を明記するとさらに分かりやすい
- handoff の実例集がまだない

## Claude に引き継ぐ要点
- 文書追加そのものは完了
- 次は `CLAUDE.md` の一文追加と handoff サンプル整備を行うと運用開始しやすい
```

---

## 4. サンプルC: 短時間代行の簡略版

想定:
5〜15分程度の軽い修正を代行するケース。

```md
# Handoff

## 目的
- `docs/_index.md` に新規文書のリンクだけ追加したい

## 現在地
- 文書本体は作成済み、索引だけ未反映

## 触ってよい範囲
- `docs/_index.md`

## 記録先
- 変更後はそのまま Return Handoff で報告
```

短時間作業でも、この4項目があるだけで再開のしやすさが大きく変わる。

---

## 5. 運用メモ

- 決定事項は断定で書く
- 未解決事項は「何が未解決か」を曖昧にしない
- 触ってよい範囲と触らない範囲を分けて書く
- handoff は長さより再開性を優先する
