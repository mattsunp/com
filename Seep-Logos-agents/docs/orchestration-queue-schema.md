# オーケストレーション YAMLキュースキーマ定義

orchestratorがセッション状態をファイルに書き出すためのフォーマット。
コンパクション（コンテキスト圧縮）後にこのファイルを読むことで、どこまで進んだかを復元できる。

---

## ファイル配置

```
queue/
└── [task-id].yaml    # 1案件1ファイル。orchestratorが作成・更新する。
```

例：`queue/game-v9-20260331.yaml`、`queue/web-mnemosyne-lp-20260331.yaml`

---

## YAMLスキーマ

```yaml
task_id: "[ドメイン]-[案件名]-[YYYYMMDD]"   # 例: game-v9-20260331
task_type: "[game-planning / web-design / pr / etc.]"
status: pending                              # pending / in_progress / completed
started_at: "YYYY-MM-DD HH:MM"
last_updated: "YYYY-MM-DD HH:MM"

instruction: |
  タスクの概要・指示内容を記載する

staffing:
  recruited:
    - "[愛称（agent-id）]"
  not_recruited:
    - "[愛称（agent-id）]: [除外理由]"

rounds:
  round1:
    status: pending                          # pending / in_progress / completed
    started_at: ""
    completed_at: ""
    agents_completed: []                     # 完了したエージェントの愛称リスト
    output: ""                               # 成果物ファイルパス
  round2:
    status: pending
    started_at: ""
    completed_at: ""
    agents_completed: []
    output: ""
  round3:
    status: pending
    started_at: ""
    completed_at: ""
    agents_completed: []
    output: ""                               # 最終統合成果物のパス

dynamic_staffing:                            # 動的招集が発生した場合のみ記載
  triggered: false
  added_agents: []
  reason: ""

notes: ""
```

---

## ステータス定義

| 値 | 意味 |
|---|---|
| `pending` | 未着手 |
| `in_progress` | 着手中 |
| `completed` | 完了。output に成果物が存在する |

---

## Session Recovery（コンパクション復帰手順）

コンパクション後にorchestratorが再起動された場合：

1. `queue/` ディレクトリを確認し、直近の案件YAMLを特定する
2. YAMLを読んで `status` と各ラウンドの状態を把握する
3. `in_progress` のラウンドから再開する
   - `agents_completed` に記載のないエージェントの作業が未完了
   - 既存の `output` ファイルが存在する場合はその内容を参照してから再開する
4. 再開時にYAMLの `last_updated` を更新する

---

## 更新タイミング

orchestratorは以下のタイミングで必ずYAMLを更新する：

| タイミング | 更新内容 |
|---|---|
| オーケストレーション開始時 | ファイル新規作成。status: in_progress |
| 各ラウンド開始時 | rounds.roundN.status: in_progress、started_at 記入 |
| 各エージェント完了時 | agents_completed にエージェント愛称を追加 |
| 各ラウンド完了時 | rounds.roundN.status: completed、output・completed_at 記入 |
| 動的招集発生時 | dynamic_staffing セクションを更新 |
| 全完了時 | status: completed |
