# 議事録
日時：2026-04-04
参加エージェント：書記
記録者：スタジオ運営管理部 / 書記（recorder）

## 議題一覧
1. セッション管理の自動化
2. DESIGN.md 実装プラン
3. Web制作部 独立検討
4. Web制作部の新設・部門再編

---

## やり取りサマリー

### トピック1：セッション管理の自動化（完了・実装済み）

- 依頼内容：複数トピックが混在するセッションにおける「混在」と「分断（コンテキスト圧縮）」2つのリスクへの対処
- 対応エージェント：（本セッション中に実装済み。担当エージェント名の記録なし）
- 主な出力・決定事項：
  - CLAUDE.md にトピック混在検知ルールを追加。新しいトピックが来たとき、Claude が着手前に宣言して書記への記録を提案するルールが追加された。
  - `.reminiscence/context-watch.py` フックを新設・稼働済み。ユーザー発言20ターンで注意、35ターンで強い警告を自動注入する動作。
  - 設定ファイルは `.claude/settings.json`（プロジェクト専用）に記載。グローバルの reminiscence フックとは干渉しない設計とされた。
- 次のアクション：なし（実装完了）

---

### トピック2：DESIGN.md 実装プラン（プランのみ確定、未実装）

- 依頼内容：Web制作における具体値（hex・フォント名・サイズ・Do's/Don'ts）の管理方法の整理
- 対応エージェント：（本セッション中に検討。担当エージェント名の記録なし）
- 主な出力・決定事項：
  - DESIGN.md のスコープは **Web制作に限定する**（ゲーム開発・映像制作には適用しない）ことが決定した。
  - 置き場所は **`web/DESIGN.md`** とすることが決定した。ルートに置くと全エージェントに自動参照されるため、意図しないスコープ拡大を防ぐことが理由として挙げられた。
  - 役割分離の核心として以下が決定した：

    | ファイル | 役割 |
    |---|---|
    | `web/DESIGN.md` | 具体値の唯一の出所（hex・フォント名・サイズ・Do's/Don'ts） |
    | `docs/visual-style-guide.md` | 哲学の唯一の出所（なぜその値か・設計思想） |

- 次のアクション（未実行・順番に実施）：
  1. `web/DESIGN.md` を新規作成（`visual-style-guide.md` から値を抽出）
  2. `docs/visual-style-guide.md` から具体値を削除し「→ DESIGN.md 参照」に差し替え
  3. `web-designer.md` の参照先を更新
  4. IP固有アクセントは `titles/[作品名]/DESIGN.md` に分離する枠を定義
  5. `CLAUDE.md` の参照テーブルに追記

---

### トピック3：Web制作部 独立検討（保留）

- 依頼内容：DESIGN.md をWeb専用部署が保有する形として、デジタル技術部からWeb制作部を独立させる案の検討
- 対応エージェント：（本セッション中に検討。担当エージェント名の記録なし）
- 主な出力・決定事項：
  - web-director・web-designer はWeb専業であり、論理的には分離可能であることが確認された。
  - ただし orchestrator 辞書・agents.md・ルーティングルールへの連鎖変更が大きいことが指摘された。
  - ui-engineering がゲームUIとWebフロント両方を担っており、帰属判断が別途必要であることが確認された。
  - **別タスクとして積み上げ、DESIGN.md 実装とは切り離すことが決定した。**
- 次のアクション：ui-engineering の帰属を含めて別タスクとして検討

---

### トピック4：Web制作部の新設・部門再編（完了・実装済み）

- 依頼内容：Web制作部を新設し、ui-engineering の帰属を含む部門再編を実施する
- 対応エージェント：（本セッション中に実装済み。担当エージェント名の記録なし）
- 主な出力・決定事項：
  - **新部門「Web制作部」を新設することが決定した。**
  - 構成エージェントは以下の通り確定した：
    - Web管理者（web-director）— 戦略・サイト設計
    - Webデザイナー（web-designer）— ビジュアル設計
    - 構築人（web-coder）— HTML/CSS/JS実装（新設）
  - **ui-engineering（機巧人）はデジタル技術部に残留することが決定した。**
    - 理由：ui-engineering はゲームUI実装を主担当とする。Web実装との分離が明確なため、別エージェントとして新設する方が適切と判断された。
  - **web-coder は ui-engineering から分割せず、別設計で新規作成することが決定した。**
    - 理由：ui-engineering がゲームUI色が強く、分割しても書き直し量が多い。Web制作部専用として一から設計する方がクリーンと判断された。
  - オーケストレーションフローが以下の通り確定した：
    ```
    orchestrator → web-director（戦略書を出力・ファイル保存）
                 ↓
    orchestrator → web-designer（仕様書を出力・ファイル保存）
                 ↓
    orchestrator → web-coder（HTML/CSS/JS を実装・完成）
    ```
    - 注記：web-designer と web-coder は順序依存があり並列不可。web-director の成果はファイルに書き出すことで情報劣化を防ぐ。
  - デジタル技術部（再編後）の構成は以下の通り確定した：
    - ゲーム開発人（game-dev-coordinator）
    - 映像管理者（video-production-director）
    - 機巧人（ui-engineering）— ゲームUI実装専任
  - 実装済みファイル：
    - `.claude/agents/Web制作部/web-coder.md`（新規作成）
    - `.claude/rules/agents.md`（部門6をWeb制作部、部門7をデジタル技術部に再編。部門8・9に番号繰り下げ）
    - `.claude/agents/orchestrator.md`（構築人を辞書追加、LP制作標準編成を更新）
- 次のアクション：なし（実装完了）

---

---

### トピック5：DESIGN.md 作成・スコープ確定（完了・実装済み）

- 依頼内容：DESIGN.md の実際の作成・内容の確定および配置場所の最終決定
- 対応エージェント：（本セッション中に実装済み。担当エージェント名の記録なし）
- 主な出力・決定事項：
  - **配置場所は `web/templates/DESIGN.md` とすることが決定した。**（プロジェクトルートではなく、web/ スコープ限定の配置）
  - **作成方法：** Google Stitch に pattern-A, A_2, N, O, P を渡して自動生成したのち、手動修正を実施した。
  - Stitch 自動生成版に存在した問題点と実施した修正内容は以下の通り：
    - フォント：Noto Serif / Manrope → Georgia / Helvetica Neue / Monospace の三層構成に修正
    - アクセント：`#e9c349` ゴールド固定 → IP 固有プレースホルダーに変更（スタジオ共通色なしと確定）
    - 背景値：記述なし → `#080810` を明示
    - アニメーション：「reveal animations」の記述のみ → 0.2s〜0.9s タイミング表および CSS 仕様を追加
    - スタジオ哲学：なし → 浸透（Seep）・没入感テスト・余白・Agent Prompt Guide（Section 9）を追加
  - **役割分担（重複回避）の最終確定：**

    | ファイル | 役割 |
    |---|---|
    | `web/templates/DESIGN.md` | 具体値の唯一の出所 |
    | `docs/visual-style-guide.md` | 哲学の唯一の出所（hex 値は持たない） |

  - **参照先の更新：** web-designer.md および web-director.md の参照先を `web/templates/DESIGN.md` に更新済み。
- 次のアクション：なし（実装完了）

---

### トピック6：Web制作フロースキル新設（完了・実装済み）

- 依頼内容：Web制作フローを再現性のあるスキルとして定義・保存する
- 対応エージェント：（本セッション中に実装済み。担当エージェント名の記録なし）
- 主な出力・決定事項：
  - **ファイル `.claude/skills/web-production.md` を新設することが決定した。**（rootの `skills/` ではなく `.claude/skills/` への配置）
  - 理由：`.claude/skills/` は Claude Code がスキルとして認識し、スラッシュコマンドで呼び出せるため。
  - **フロー定義（情報劣化リスク対策済み）：**
    - Round 1：web-director → `web/[案件名]/instructions/director.md` に保存（必須）
    - Round 2：orchestrator がファイルを参照して web-designer に渡す → `web/[案件名]/instructions/designer.md` に保存
    - Round 3：orchestrator がファイルを参照して web-coder に渡す → `web/[案件名]/index.html` を実装
    - 補注：要約ではなくファイルパスを渡すことで情報劣化を防ぐ設計とされた。
  - **orchestrator.md 更新：** LP制作パターンに `.claude/skills/web-production.md` 参照を追記済み。
  - **命名規則：** `brief/` は使用禁止（過去に確定済み）。`instructions/` を使用することが再確認された。
- 次のアクション：なし（実装完了）

---

### トピック7：Web制作部 稼働テスト（完了）

- 依頼内容：新設した Web制作部のフロー・品質を実案件でテストする
- 対応エージェント：指揮者、Web管理者、Webデザイナー、構築人
- 主な出力・決定事項：
  - **テスト内容：** pattern-AA「void-invitation」を新設 Web制作部で制作。
  - **コンセプト：** 受け手を「観客」ではなく「応答者」として位置づける新方向性を採用。
  - **感情フェーズ：** 静寂 → 感知 → 共鳴 → 応答。
  - **A〜P との差異：**
    - ナビゲーションを意図的に排除
    - 情報密度を「疎 → 極疎 → 中密 → 疎」の波形設計
    - CTA が命令形でなく招待形式
  - **画像組み込み仕様：**
    - `background.png` → Hero の背景（3層グラデーションオーバーレイで没入感維持）
    - `scene.png` → SIGNAL-ECHO 間のシーンブレイク（opacity 0.35、上下フェード、1.6s スクロールイン）
  - **成果物：**
    - `web/templates/instructions/pattern-AA/director.md`
    - `web/templates/instructions/pattern-AA/designer.md`
    - `web/templates/pattern-AA_void-invitation.html`
  - **評価：** 「いい感じ」。フロー・出力品質ともに初回稼働テスト合格とされた。
- 次のアクション：なし（テスト完了）

---

## 決定事項まとめ

- セッション管理の自動化として、CLAUDE.md へのトピック混在検知ルール追加および `context-watch.py` フックの新設・稼働が完了した。
- DESIGN.md のスコープはWeb制作に限定することが決定した。
- DESIGN.md の置き場所は `web/DESIGN.md` とすることが決定した（トピック2時点の計画）。
- `web/templates/DESIGN.md` を具体値の唯一の出所、`docs/visual-style-guide.md` を哲学の唯一の出所とする役割分離方針が決定した（トピック5にて最終確定・実装完了）。
- Web制作部の独立は別タスクとして積み上げ、DESIGN.md 実装とは切り離すことが決定した（トピック3時点）。
- 新部門「Web制作部」を新設することが決定した（トピック4にて正式決定・実装完了）。
- Web制作部の構成エージェントは web-director・web-designer・web-coder（新設）の3名とすることが決定した。
- ui-engineering（機巧人）はデジタル技術部に残留することが決定した。
- web-coder は ui-engineering から分割せず新規設計で作成することが決定した。
- `web/templates/DESIGN.md` を新設し、フォント三層構成・IP固有アクセントプレースホルダー・背景値・アニメーション仕様・スタジオ哲学を明記することが決定した（トピック5）。
- Web制作フロースキル `.claude/skills/web-production.md` を新設し、3ラウンド構成でのファイルパス受け渡しフローを確定した（トピック6）。
- pattern-AA「void-invitation」の制作をもって Web制作部の初回稼働テストが合格と判断された（トピック7）。

---

## 未解決・継続課題

- 天才化プロジェクトの続き（シナリオ書き・ゲームディレクターなど）
- frontend-design スキルの試用
- DESIGN.md から visual-style-guide.md の具体値を削除する作業（Step2、未実施）
- IP固有の `titles/[作品名]/DESIGN.md` 分離の枠組み定義（未実施）
