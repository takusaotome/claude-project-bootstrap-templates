---

# FILE: README.md

# Claude Project Bootstrap Template Pack

作成日: 2026-03-21

## このパックの目的

新しいプロジェクトを始めるときに、AIエージェントが最初から次のことを理解できる状態を素早く作るためのテンプレート集です。

- このプロジェクトの目的・制約・重要リスク
- どのフェーズでどのスキルを使うべきか
- 完了判定をどう定義するか
- 本番同等テストをどう設計するか
- 重要な意思決定や隠れた契約をどこに残すか

## 最小導入セット

まずは次の5つだけ導入すれば十分です。

1. `CLAUDE.md.template.md` → `CLAUDE.md` にコピーして編集
2. `docs/PROJECT_BRIEF.template.md` → `docs/PROJECT_BRIEF.md`
3. `docs/SKILL_ROUTING.template.md` → `docs/SKILL_ROUTING.md`
4. `docs/QUALITY_GATES.template.md` → `docs/QUALITY_GATES.md`
5. `docs/TEST_STRATEGY.template.md` → `docs/TEST_STRATEGY.md`

## 拡張導入セット

余裕があれば次も入れると運用がかなり安定します。

- `docs/HIDDEN_CONTRACT_REGISTER.template.md`
- `docs/CROSS_MODULE_CONSISTENCY_MATRIX.template.md`
- `docs/DECISION_LOG.template.md`
- `.claude/rules/*.template.md`
- `.claude/commands/project-kickoff.md.template.md`

## 推奨ディレクトリ構成

```text
{{PROJECT_ROOT}}/
├── CLAUDE.md
├── .claude/
│   ├── rules/
│   │   ├── backend-api.md
│   │   ├── db-and-migrations.md
│   │   └── testing-and-release.md
│   └── commands/
│       └── project-kickoff.md
└── docs/
    ├── PROJECT_BRIEF.md
    ├── SKILL_ROUTING.md
    ├── QUALITY_GATES.md
    ├── TEST_STRATEGY.md
    ├── DECISION_LOG.md
    ├── HIDDEN_CONTRACT_REGISTER.md
    └── CROSS_MODULE_CONSISTENCY_MATRIX.md
```

## 導入手順

### 1. ソースオブトゥルースを決める

最初に `PROJECT_BRIEF.md` を埋めて、プロジェクトの目的・スコープ・環境・外部依存を明確にします。

### 2. スキル起動条件を決める

`SKILL_ROUTING.md` に「どの状況でどのスキルを使うか」を明記します。

### 3. 完了判定を明確にする

`QUALITY_GATES.md` に、実装完了・テスト完了・リリース可否を分けて定義します。

### 4. テスト盲点を埋める

`TEST_STRATEGY.md` で、unit / integration / e2e / production parity の責務を分けます。

### 5. ルールをパス単位で当てる

`.claude/rules/` で、API・DB・テスト周りなどにパス依存ルールを置きます。

### 6. 初期化コマンドを置く

`/project-kickoff` を導入すると、新規リポジトリや既存リポジトリへの後付け導入が楽になります。

## このパックで想定するスキル群

### 既存スキル
- `project-manager`
- `project-plan-creator`
- `critical-code-reviewer`
- `design-implementation-reviewer`
- `project-completeness-scorer`
- `tdd-developer`
- `migration-validation-explorer`
- `qa-bug-analyzer`
- `incident-rca-specialist`

### 追加予定スキル
- `completion-quality-gate-designer`
- `hidden-contract-investigator`
- `safe-by-default-architect`
- `cross-module-consistency-auditor`
- `production-parity-test-designer`

## 運用上の考え方

- `CLAUDE.md` は短く保ち、重い内容は `docs/` に分ける
- ルールはできるだけ `.claude/rules/` に分割する
- 重要な判断は `DECISION_LOG.md` に残す
- 既存コード再利用時の思い込みは `HIDDEN_CONTRACT_REGISTER.md` で潰す
- 完了判定は「コードを書いた」ではなく「必要証跡が揃った」で判断する

## 置換対象プレースホルダ

- `{{PROJECT_NAME}}`
- `{{PROJECT_SUMMARY}}`
- `{{PRIMARY_LANGUAGE}}`
- `{{STACK}}`
- `{{BUILD_COMMAND}}`
- `{{TEST_COMMAND}}`
- `{{LINT_COMMAND}}`
- `{{TYPECHECK_COMMAND}}`
- `{{CI_COMMAND}}`
- `{{PACKAGE_OR_DEPLOY_COMMAND}}`
- `{{MAIN_SOURCE_DIR}}`
- `{{TEST_DIR}}`
- `{{DB_DIR}}`
- `{{OWNER_OR_TEAM}}`

## 導入時の注意

テンプレートは最初から全部埋める必要はありません。  
ただし、次の4つだけは空欄にしないほうがよいです。

- 目的 / スコープ
- 実行コマンド
- 高リスク領域
- 完了判定


---

# FILE: CLAUDE.md.template.md

# CLAUDE.md

このファイルは、{{PROJECT_NAME}} に対して Claude Code / AI エージェントが継続的に従うべきプロジェクト共通ルールを定義する。

@docs/PROJECT_BRIEF.md
@docs/SKILL_ROUTING.md
@docs/QUALITY_GATES.md
@docs/TEST_STRATEGY.md

## Session Operating Mode

- すべての作業は、まず対象フェーズを `discovery / design / implementation / verification / release` のいずれかに分類する。
- 中規模以上または高リスクの変更では、実装前に `docs/SKILL_ROUTING.md` を参照し、使うべきスキルを選択する。
- 既存コード・共通関数・外部ライブラリ・他チーム提供モジュールを使うときは、挙動を推測せず、必要に応じて `hidden-contract-investigator` 相当の手順を先に実施する。
- 完了報告前に `docs/QUALITY_GATES.md` の該当ゲートを満たした証跡を確認する。
- 実装・設計・テスト方針に重要な判断が入った場合は `docs/DECISION_LOG.md` に残す。

## Default Workflow

1. 目的、対象範囲、制約、影響範囲、環境差分を明確化する。
2. `docs/SKILL_ROUTING.md` から使用スキルを選ぶ。
3. 変更前に短い作業計画を示す。
4. 小さな単位で実装・修正する。
5. `docs/TEST_STRATEGY.md` と `docs/QUALITY_GATES.md` に沿って検証する。
6. 最後に、変更内容・検証結果・残課題・リスクを明示する。

## Non-Negotiables

- 「コードを書いた」だけでは完了扱いにしない。
- 成功表示、ログ出力、関数戻り値だけで成功を断定しない。必要なら永続化・副作用・外部連携結果まで確認する。
- 認可、課金・金額、日時、タイムゾーン、ファイルI/O、DB差分、マイグレーション、ジョブ、並行実行は高リスク領域として扱う。
- 既存の危険な実装を踏襲せず、可能な限り安全側の標準パターンを優先する。
- 仮説・未確認事項・未実施テストは明確に区別して報告する。

## Project Defaults

- Primary language: `{{PRIMARY_LANGUAGE}}`
- Main stack: `{{STACK}}`
- Main source directory: `{{MAIN_SOURCE_DIR}}`
- Test directory: `{{TEST_DIR}}`
- Database / migration directory: `{{DB_DIR}}`

## Standard Commands

- Build: `{{BUILD_COMMAND}}`
- Test: `{{TEST_COMMAND}}`
- Lint: `{{LINT_COMMAND}}`
- Typecheck: `{{TYPECHECK_COMMAND}}`
- CI equivalent: `{{CI_COMMAND}}`
- Package / Deploy check: `{{PACKAGE_OR_DEPLOY_COMMAND}}`

## Output Expectations

回答や変更サマリでは、必要に応じて次を含める。

- 何を変更したか
- なぜ変更したか
- どのスキル / ルールを使ったか
- どのテストを実行したか
- 未確認事項と残リスク
- 次の推奨アクション

## Missing Information Policy

以下のどれかが欠けている場合、勝手に前提固定せず不足として明示する。

- 環境差分
- 成功条件
- 既存資産の契約
- 影響範囲
- リリース条件

## Template Maintenance Rule

この `CLAUDE.md` は短く保つ。  
長くなった場合は `docs/` か `.claude/rules/` に分割し、ここには参照関係と最重要ルールだけを残す。


---

# FILE: docs/PROJECT_BRIEF.template.md

# PROJECT_BRIEF

## 1. Project Overview

- Project name: `{{PROJECT_NAME}}`
- One-line summary: `{{PROJECT_SUMMARY}}`
- Owner / team: `{{OWNER_OR_TEAM}}`
- Current phase: `{{CURRENT_PHASE}}`
- Repository URL: `{{REPOSITORY_URL}}`

## 2. Goal and Success Criteria

### Goal
- 何を実現するプロジェクトか
- どの利用者 / 業務 / KPI に効くか

### Success Criteria
- 例: エラー率、応答時間、業務時間削減、売上影響、導入期限

## 3. Scope

### In Scope
- 
- 
- 

### Out of Scope
- 
- 
- 

## 4. Key Stakeholders

| Role | Name / Team | Responsibility | Decision Authority |
|---|---|---|---|
| Product owner |  |  |  |
| Tech lead |  |  |  |
| QA / Tester |  |  |  |
| Ops / SRE |  |  |  |
| Security / Compliance |  |  |  |

## 5. Architecture Snapshot

### Major Components
- Frontend:
- Backend / API:
- Batch / Jobs:
- Database:
- External services:

### High-Level Flow
1. 
2. 
3. 

## 6. Repository Map

| Area | Path | Purpose | Notes |
|---|---|---|---|
| Main app | `{{MAIN_SOURCE_DIR}}` |  |  |
| Tests | `{{TEST_DIR}}` |  |  |
| DB / migrations | `{{DB_DIR}}` |  |  |
| Infrastructure | `{{INFRA_DIR}}` |  |  |
| Docs | `docs/` |  |  |

## 7. Runtime and Environment Matrix

| Environment | App Runtime | DB | External Dependencies | Notes |
|---|---|---|---|---|
| Local |  |  |  |  |
| CI |  |  |  |  |
| Staging |  |  |  |  |
| Production |  |  |  |  |

## 8. Standard Commands

| Purpose | Command | Expected Result |
|---|---|---|
| Install | `{{INSTALL_COMMAND}}` |  |
| Build | `{{BUILD_COMMAND}}` |  |
| Unit test | `{{UNIT_TEST_COMMAND}}` |  |
| Integration test | `{{INTEGRATION_TEST_COMMAND}}` |  |
| E2E / smoke | `{{E2E_OR_SMOKE_COMMAND}}` |  |
| Lint | `{{LINT_COMMAND}}` |  |
| Typecheck | `{{TYPECHECK_COMMAND}}` |  |
| CI equivalent | `{{CI_COMMAND}}` |  |
| Packaging / deploy verify | `{{PACKAGE_OR_DEPLOY_COMMAND}}` |  |

## 9. High-Risk Areas

以下は、最初から AI が慎重に扱うべき領域を列挙する。

| Risk Area | Why Risky | Typical Failure Mode | Primary Skill |
|---|---|---|---|
| Authentication / Authorization |  |  | `safe-by-default-architect` |
| DB / SQL / Migration |  |  | `production-parity-test-designer` |
| Time / Timezone |  |  | `design-implementation-reviewer` |
| Money / Rounding / Tax |  |  | `critical-code-reviewer` |
| External API / File I/O |  |  | `hidden-contract-investigator` |
| Cross-module business rules |  |  | `cross-module-consistency-auditor` |

## 10. Known Constraints

- Delivery date:
- Budget / staffing:
- Compliance / regulation:
- Performance constraints:
- Backward compatibility constraints:
- Operations constraints:

## 11. Open Questions

- 
- 
- 

## 12. References

- Main README:
- System design docs:
- API docs:
- Ops runbook:
- Product spec:


---

# FILE: docs/SKILL_ROUTING.template.md

# SKILL_ROUTING

## 1. Purpose

この文書は、プロジェクト内で AI エージェントが「どのタイミングで」「どのスキルを」「何のために」使うかを定義する。

## 2. Operating Rule

- 低リスクの小修正を除き、作業開始時に **Primary Skill** を1つ選ぶ。
- 高リスク変更では **Primary Skill + Secondary Skill** を選ぶ。
- スキルが未導入なら、同等の手順を手動で実施し、その不足を報告する。
- 完了判定は `QUALITY_GATES.md` を優先する。

## 3. Phase-Based Routing

| Phase | Situation / Trigger | Primary Skill | Secondary Skill | Expected Output | Exit Condition |
|---|---|---|---|---|---|
| Discovery | 要件が曖昧 / スコープが広い / 関係者調整が必要 | `project-manager` | `project-plan-creator` | 目的・範囲・WBS・リスク | 実装対象と成功条件が明確 |
| Kickoff | 完了条件が曖昧 / 品質ゲートが未定義 | `completion-quality-gate-designer` | `project-completeness-scorer` | `QUALITY_GATES.md` | Ready / Done / Release の定義が固定 |
| Design | 既存コード再利用だが挙動が怪しい / 契約が不明 | `hidden-contract-investigator` | `design-implementation-reviewer` | `HIDDEN_CONTRACT_REGISTER.md` 更新 | 実契約が確認済み |
| Design | 認可、SQL、ファイルI/O、外部連携、危険パターンを含む | `safe-by-default-architect` | `critical-code-reviewer` | 安全側の標準案 / 禁止パターン | 危険な実装を避ける標準が決まった |
| Design / Implementation | 2モジュール以上に影響 / 類似フローが複数 / コピペ懸念 | `cross-module-consistency-auditor` | `project-manager` | `CROSS_MODULE_CONSISTENCY_MATRIX.md` 更新 | 影響範囲と更新漏れが見える |
| Implementation | テスト先行で進めたい / 失敗条件から固めたい | `tdd-developer` | `production-parity-test-designer` | テスト計画 / テスト実装 | 主要失敗ケースがテスト化 |
| Verification | 本番との差分が不安 / DB方言差 / 依存差 / packaging差 | `production-parity-test-designer` | `migration-validation-explorer` | `TEST_STRATEGY.md` 更新 | parity テスト観点が定義済み |
| Pre-merge | 批判的レビューが必要 / バグを積極的に探したい | `critical-code-reviewer` | `design-implementation-reviewer` | レビュー指摘一覧 | 高優先度指摘の扱いが確定 |
| Release | リリース可否を判断したい / 未解決リスクがある | `project-completeness-scorer` | `completion-quality-gate-designer` | リリース判定メモ | 必須ゲート充足 or 例外承認 |
| Post-incident | 不具合が出た / 傾向を見たい | `incident-rca-specialist` | `qa-bug-analyzer` | RCA / 再発防止策 | 真因と対策が整理済み |

## 4. Signal-Based Routing

### Use `hidden-contract-investigator` when:
- 名前から挙動を推測して使いそう
- 共通関数・共通サービスを流用する
- 戻り値型、エラー挙動、副作用が不明
- テストでモックされていて実実装が見えていない

### Use `safe-by-default-architect` when:
- 認可・権限・機微データを触る
- 生SQLや直書きファイル操作を入れたくなる
- 危険だが手軽な実装と、安全だがやや手間な実装が並んでいる
- 今後似た実装が増える見込みがある

### Use `cross-module-consistency-auditor` when:
- 同じ仕様が複数画面 / 複数バッチ / 複数APIにまたがる
- 集計ルールや判定ルールが複数箇所にある
- 変更漏れが起こりやすい構造になっている

### Use `production-parity-test-designer` when:
- 本番でしか使わない DB / middleware / secret / packaging がある
- staging / CI / local の差がある
- UI の成功と永続化成功がズレる可能性がある
- migration, background job, container build, runtime dependency が絡む

### Use `completion-quality-gate-designer` when:
- 「どこまでできたら完了か」が曖昧
- 証跡が人によって違う
- テストはしたと言うが何をしたか残らない
- 例外運用や waiver の扱いが決まっていない

## 5. Required Outputs by Skill

| Skill | Required Artifact |
|---|---|
| `completion-quality-gate-designer` | `docs/QUALITY_GATES.md` |
| `hidden-contract-investigator` | `docs/HIDDEN_CONTRACT_REGISTER.md` |
| `safe-by-default-architect` | 設計メモ または `.claude/rules/` 更新 |
| `cross-module-consistency-auditor` | `docs/CROSS_MODULE_CONSISTENCY_MATRIX.md` |
| `production-parity-test-designer` | `docs/TEST_STRATEGY.md` |
| `critical-code-reviewer` | レビュー結果メモ |
| `project-completeness-scorer` | 完成度 / リリース判定メモ |

## 6. Escalation Rule

次のいずれかに当てはまる場合、低リスク作業として扱わず、レビュー・テスト深度を上げる。

- 金額、税、丸め、計算ロジック
- 権限、認証、個人情報、秘密情報
- 日付、時刻、タイムゾーン、締め時刻
- DBスキーマ変更、クエリ変更、マイグレーション
- 外部 API、メッセージング、ジョブ、ファイル保存
- 同一仕様が複数箇所に散っている変更


---

# FILE: docs/QUALITY_GATES.template.md

# QUALITY_GATES

## 1. Purpose

この文書は、プロジェクトにおける完了判定を「実装完了」「テスト完了」「リリース可能」に分解して定義する。

## 2. Definitions

| Gate | Meaning | Typical Owner |
|---|---|---|
| Ready for Design | 目的・スコープ・制約・依存が最低限明確 | PM / Tech Lead |
| Ready for Implementation | 設計方針・対象範囲・完了条件が明確 | Tech Lead |
| Implementation Complete | コード変更が揃い、意図した実装が完了 | Developer |
| Test Complete | 必要な検証が終わり、結果が記録済み | Developer / QA |
| Release Ready | 残リスクと未解決事項を含めて出荷判断可能 | PM / Tech Lead / QA |

## 3. Gate Criteria

### 3.1 Ready for Design
- 目的、対象範囲、非対象範囲が書かれている
- 成功条件がある
- 主要ステークホルダーが定義されている
- 高リスク領域が列挙されている

### 3.2 Ready for Implementation
- 変更対象ファイル / モジュールの見当がついている
- 影響範囲が整理されている
- 使うスキルとレビュー深度が決まっている
- テスト方針の当たりがついている
- 不明契約がある場合は調査タスクが切られている

### 3.3 Implementation Complete
- コード変更が反映済み
- 主要なエラーパス / 境界条件が考慮済み
- ログ、監視、エラーメッセージの方針が妥当
- 変更理由と要点を説明できる

### 3.4 Test Complete
- 実行したテストが列挙されている
- 未実施テストがあれば理由付きで記録されている
- 高リスク領域に対するテストが含まれる
- 本番同等性が必要な箇所は parity 観点がカバーされている
- 重要な結果ログ / スクリーンショット / レポートへの参照がある

### 3.5 Release Ready
- 必須テストが通っている
- 未解決課題と暫定対策が明示されている
- 運用上の注意が共有されている
- rollback / recovery の考え方がある
- 例外承認が必要なら承認者と期限が明記されている

## 4. Evidence Table

| Gate | Mandatory Evidence | Where to Record |
|---|---|---|
| Ready for Design | 目的、スコープ、制約、リスク | `PROJECT_BRIEF.md` |
| Ready for Implementation | 設計方針、対象範囲、テスト方針 | `PROJECT_BRIEF.md`, `TEST_STRATEGY.md` |
| Implementation Complete | 変更ファイル、概要、既知制約 | PR / 変更サマリ |
| Test Complete | 実行コマンド、結果、未実施項目 | `TEST_STRATEGY.md` or PR comment |
| Release Ready | 判定結果、残リスク、rollback 観点 | リリース判定メモ |

## 5. Required Commands

以下をプロジェクト実態に合わせて埋める。

| Check Type | Command | Mandatory? |
|---|---|---|
| Build | `{{BUILD_COMMAND}}` | Yes / No |
| Unit tests | `{{UNIT_TEST_COMMAND}}` | Yes / No |
| Integration tests | `{{INTEGRATION_TEST_COMMAND}}` | Yes / No |
| E2E / smoke | `{{E2E_OR_SMOKE_COMMAND}}` | Yes / No |
| Lint | `{{LINT_COMMAND}}` | Yes / No |
| Typecheck | `{{TYPECHECK_COMMAND}}` | Yes / No |
| CI equivalent | `{{CI_COMMAND}}` | Yes / No |
| Packaging / deploy verify | `{{PACKAGE_OR_DEPLOY_COMMAND}}` | Yes / No |

## 6. Risk-Based Extra Gates

次の変更では追加ゲートを入れる。

| Risk | Extra Evidence |
|---|---|
| Auth / Permission | 許可 / 拒否両方の確認 |
| Money / Tax / Rounding | 境界値、丸め差、例外系確認 |
| Time / Timezone | TZ混在、DST、締め時刻確認 |
| SQL / Migration | 対象 DB 方言、rollback、データ整合確認 |
| External API / File I/O | 接続失敗、再試行、部分失敗、永続化確認 |
| Cross-module rules | 更新漏れがないことの確認 |

## 7. Exception / Waiver Policy

例外を認める場合は、最低限次を記録する。

- 何を未実施にしたか
- なぜ未実施か
- リスクは何か
- 暫定対策は何か
- だれが承認したか
- いつまでに解消するか

## 8. Release Decision Template

```md
# Release Decision
- Decision: Go / Conditional Go / No-Go
- Scope:
- Mandatory checks passed:
- Waivers:
- Residual risks:
- Rollback notes:
- Decision owner:
- Timestamp:
```


---

# FILE: docs/TEST_STRATEGY.template.md

# TEST_STRATEGY

## 1. Purpose

この文書は、どのテストを、どの環境で、どの深さまで行うかを定義する。

## 2. System Under Test

- Feature / change target:
- Affected modules:
- Critical user / business flow:
- Main failure concerns:

## 3. Test Levels and Responsibilities

| Level | Main Objective | What to Catch | What Not to Rely On |
|---|---|---|---|
| Unit | ロジック単体の正しさ | 分岐、境界値、純粋関数の誤り | 環境差分、接続、永続化 |
| Integration | モジュール間 / DB / API 接続 | 契約ズレ、SQL、依存関係 | ブラウザ全体の実動線 |
| E2E / Workflow | 利用者動線の成立 | 画面遷移、成功 / 失敗体験、永続化確認 | 細かい全分岐の網羅 |
| Production Parity / Smoke | 本番同等条件での破綻検知 | DB方言差、runtime依存、packaging、環境差 | 単体ロジック網羅 |

## 4. Risk Coverage Matrix

| Risk Area | Unit | Integration | E2E | Production Parity | Notes |
|---|---|---|---|---|---|
| Business rule correctness | Yes | Optional | Optional | Optional |  |
| Auth / permission | Optional | Yes | Yes | Optional |  |
| DB query / migration | Optional | Yes | Optional | Yes |  |
| File I/O / storage | Optional | Yes | Optional | Yes |  |
| External API / runtime dependency | Optional | Yes | Optional | Yes |  |
| Time / timezone / scheduling | Yes | Yes | Optional | Yes |  |
| Money / rounding / calculation | Yes | Yes | Optional | Optional |  |
| Cross-module consistency | Optional | Yes | Yes | Optional |  |

## 5. Environment Matrix

| Environment | Purpose | Closest to Prod? | Key Differences | Required Test Types |
|---|---|---|---|---|
| Local | 開発中の高速確認 | No |  |  |
| CI | 自動回帰 | Partial |  |  |
| Staging | 結合確認 / リリース前確認 | Usually |  |  |
| Production-like sandbox | 本番同等検証 | Yes |  |  |

## 6. Mandatory Test Scenarios

### Happy Path
- 
- 

### Error Path
- 
- 

### Boundary / Edge Cases
- 
- 

### Data Integrity
- 保存、更新、削除、再実行、冪等性

### Environment Parity
- DB dialect 差
- secret / config 差
- packaging / image build 差
- optional dependency / runtime import 差

## 7. Production Parity Checklist

- [ ] 本番DBと同じ方言 / 主要機能で確認した
- [ ] migration の forward / rollback を考慮した
- [ ] UI 成功表示だけでなく永続化結果を確認した
- [ ] mock に隠れた依存を洗い出した
- [ ] background job / async 処理の最終結果を確認した
- [ ] packaging / container / deployment artifact で起動確認した
- [ ] 外部連携失敗時の挙動を確認した

## 8. Commands and Evidence

| Scenario | Command / Procedure | Evidence Location |
|---|---|---|
| Unit | `{{UNIT_TEST_COMMAND}}` |  |
| Integration | `{{INTEGRATION_TEST_COMMAND}}` |  |
| E2E / smoke | `{{E2E_OR_SMOKE_COMMAND}}` |  |
| Prod parity | `{{PROD_PARITY_COMMAND}}` |  |
| Packaging | `{{PACKAGE_OR_DEPLOY_COMMAND}}` |  |

## 9. Exit Criteria

テスト完了とみなすための条件。

- 必須シナリオが実行済み
- 結果が残っている
- 未実施項目が明示されている
- 高リスク領域に盲点が残っていない、または残っているなら合意済み

## 10. Open Risks

| Risk | Why Not Fully Tested | Temporary Mitigation | Owner |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


---

# FILE: docs/DECISION_LOG.template.md

# DECISION_LOG

## Usage Rule

- 設計・品質・運用に影響する判断を残す
- 後から見て「なぜこうしたのか」を説明できる粒度で書く
- 1件1セクションで追記する

---

## Decision {{YYYY-MM-DD}}-01: {{TITLE}}

### Context
- 背景:
- 問題:
- 影響範囲:

### Options Considered
1. 
2. 
3. 

### Decision
- 採用案:
- 理由:

### Skill Support
- 使ったスキル:
- 参照した文書:

### Consequences
- 良い影響:
- 悪い影響 / トレードオフ:
- 今後のフォロー:

### Approval
- Decision owner:
- Reviewers:
- Date:


---

# FILE: docs/HIDDEN_CONTRACT_REGISTER.template.md

# HIDDEN_CONTRACT_REGISTER

## Purpose

既存関数・共通サービス・外部モジュール・ライブラリ利用時の「名前から見えない契約」を記録する。

## Register

| Item | Location | Why It Was Risky | Assumed Contract | Actual Contract | Side Effects / Error Behavior | Environment Assumptions | Verification Evidence | Owner |
|---|---|---|---|---|---|---|---|---|
| Example: `keepTwoDecimal` | `utils/money.py` | 名前から数値返却に見えた | float を返すと思った | string を返す | 文字列比較・型変換が必要 | locale / format 依存あり | 実装読解 / 実テスト |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |

## Investigation Checklist

- [ ] 関数名 / API 名だけで判断していない
- [ ] 戻り値型を確認した
- [ ] 例外発生条件を確認した
- [ ] 副作用を確認した
- [ ] mock と実実装の差を確認した
- [ ] 環境差分の影響を確認した


---

# FILE: docs/CROSS_MODULE_CONSISTENCY_MATRIX.template.md

# CROSS_MODULE_CONSISTENCY_MATRIX

## Purpose

同一仕様が複数モジュール・複数フロー・複数ジョブに散っている場合の変更漏れを防ぐための管理表。

## Matrix

| Business Rule / Behavior | Modules / Files / Flows Affected | Shared or Duplicated? | Required Updates | Test Coverage | Owner | Status |
|---|---|---|---|---|---|---|
| Example: Refund total calculation | API, batch, admin screen, export job | Duplicated | 4箇所更新 | unit + integration |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

## Consistency Checklist

- [ ] 仕様が複数箇所に散っていないか確認した
- [ ] コピペ箇所を特定した
- [ ] 共通化候補を検討した
- [ ] 更新漏れ候補を列挙した
- [ ] テスト対象を全フローにひも付けた
- [ ] レビュー対象者に影響範囲を共有した


---

# FILE: docs/PROJECT_KICKOFF_CHECKLIST.template.md

# PROJECT_KICKOFF_CHECKLIST

## Human + AI Kickoff Checklist

### A. Project Context
- [ ] プロジェクトの目的を1文で書いた
- [ ] スコープ / 非スコープを書いた
- [ ] ステークホルダーを定義した
- [ ] 高リスク領域を列挙した
- [ ] 環境差分を整理した

### B. AI Context
- [ ] `CLAUDE.md` を配置した
- [ ] `PROJECT_BRIEF.md` を作成した
- [ ] `SKILL_ROUTING.md` を作成した
- [ ] `QUALITY_GATES.md` を作成した
- [ ] `TEST_STRATEGY.md` を作成した
- [ ] `.claude/rules/` を必要に応じて配置した
- [ ] `/project-kickoff` コマンドを配置した

### C. Execution Readiness
- [ ] build/test/lint/typecheck コマンドを埋めた
- [ ] main source / test / db ディレクトリを明記した
- [ ] リリース判定者を決めた
- [ ] 例外運用のルールを決めた

### D. Risk Controls
- [ ] 隠れ契約を記録する場所を決めた
- [ ] モジュール横断整合性を記録する場所を決めた
- [ ] production parity の最低ラインを決めた
- [ ] 重大欠陥のエスカレーション先を決めた


---

# FILE: .claude/rules/backend-api.md.template.md

---
paths:
  - "src/api/**/*"
  - "src/backend/**/*"
  - "app/api/**/*"
  - "server/**/*"
  - "{{MAIN_SOURCE_DIR}}/**/*.py"
  - "{{MAIN_SOURCE_DIR}}/**/*.ts"
---

# Backend / API Rules

- 既存サービス、共通関数、ラッパーを流用する場合は、必要に応じて `hidden-contract-investigator` 相当の手順を先に行う。
- 認可、機微データ、ファイルI/O、外部API、SQL を含む場合は `safe-by-default-architect` の観点で実装方針を選ぶ。
- 成功レスポンスや UI メッセージだけで成功とみなさず、必要に応じて永続化・副作用・外部連携結果まで確認する。
- 入力バリデーション、認可判定、エラー処理、監査可能性を考慮する。
- 高リスク変更では integration test 以上を必須候補とする。


---

# FILE: .claude/rules/db-and-migrations.md.template.md

---
paths:
  - "db/**/*"
  - "database/**/*"
  - "migrations/**/*"
  - "alembic/**/*"
  - "prisma/**/*"
  - "**/*.sql"
---

# DB / Migration Rules

- クエリやマイグレーション変更時は、ターゲット DB 方言と transaction 挙動を明示する。
- 本番と開発で DB が異なる場合は `production-parity-test-designer` 相当の観点を必ず入れる。
- schema change が 2 モジュール以上に影響する場合は `cross-module-consistency-auditor` 相当の確認を行う。
- forward だけでなく rollback、再実行、データ整合性も確認対象に含める。
- 生SQLを使う場合は、パラメータ化、方言依存、インデックス影響、NULL/集計挙動を明示する。


---

# FILE: .claude/rules/testing-and-release.md.template.md

---
paths:
  - "tests/**/*"
  - ".github/workflows/**/*"
  - "ci/**/*"
  - "scripts/**/*"
  - "Makefile"
  - "package.json"
  - "pyproject.toml"
---

# Testing / Release Rules

- テスト設計では unit / integration / e2e / production parity の責務を混同しない。
- 高リスク変更で happy path だけしかない場合は不十分として扱う。
- `QUALITY_GATES.md` に定義した必須証跡とテスト結果を結びつける。
- packaging / container build / runtime dependency がある場合は、本番同等確認を検討する。
- リリース判定では、通ったテストだけでなく未実施テストと残リスクも明示する。


---

# FILE: .claude/commands/project-kickoff.md.template.md

---
description: Bootstrap Claude project context and quality controls for a new or existing repository. Create or refresh PROJECT_BRIEF, SKILL_ROUTING, QUALITY_GATES, and TEST_STRATEGY from repository evidence and user answers.
argument-hint: [optional-focus]
allowed-tools: Read,Write,Edit,Grep,Glob,LS,TodoRead,TodoWrite,AskUserQuestion
---

# Project Kickoff Bootstrap

プロジェクト開始時または AI 導入後追い時に、Claude 用の初期文脈と品質統制ドキュメントを整備する。

## Goals

- プロジェクトの目的・スコープ・主要リスクを明確化する
- スキルの使い分けルールを定義する
- 完了判定を明文化する
- テスト戦略と production parity 観点を定義する
- 不足情報はユーザーに確認し、推測で固定しない

## Workflow

### Phase 1: Inspect Repository
1. ルート構成を確認する
2. README、manifest、CI、テスト関連ファイルを確認する
3. 既存の `CLAUDE.md`、`.claude/rules/`、`docs/` を確認する
4. build / test / lint / typecheck / packaging 相当コマンド候補を抽出する

### Phase 2: Detect Missing Context
次の不足を洗い出す。

- 目的と成功条件
- スコープ / 非スコープ
- 高リスク領域
- 環境差分
- リリース条件
- 必要スキル

### Phase 3: Ask Targeted Questions
AskUserQuestion を使って、足りない情報だけを 2〜4 問ずつ聞く。

優先質問領域:
- プロジェクト目的
- 主要利用者 / 業務
- 本番環境との差
- 高リスク領域
- 完了判定

### Phase 4: Create / Refresh Documents
必要に応じて次を作成または更新する。

- `CLAUDE.md`
- `docs/PROJECT_BRIEF.md`
- `docs/SKILL_ROUTING.md`
- `docs/QUALITY_GATES.md`
- `docs/TEST_STRATEGY.md`
- `docs/DECISION_LOG.md`
- `docs/HIDDEN_CONTRACT_REGISTER.md`
- `docs/CROSS_MODULE_CONSISTENCY_MATRIX.md`

### Phase 5: Report Result
最後に次をまとめる。

```md
## Kickoff Summary
- Created / updated files:
- Key project risks:
- Selected mandatory skills:
- Missing information:
- Recommended next action:
```

## Rules

- 既存文書がある場合は無断で破壊せず、差分更新を優先する
- 不明な項目は `TBD` として残し、未確認で確定文にしない
- コマンドは実際の repo evidence があるものを優先し、なければ候補として示す
- 技術的高リスク領域がある場合はスキルルーティングに必ず反映する
