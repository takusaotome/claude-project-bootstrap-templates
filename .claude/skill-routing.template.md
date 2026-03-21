# Skill Routing Matrix

この文書は、どのフェーズでどのスキルを使うかを定義する。
AI エージェントは、主要タスクの開始前に必ずこの表を参照すること。

## 1. Skill Inventory

### 既存スキル
- `project-plan-creator`
- `project-manager`
- `project-completeness-scorer`
- `business-analyst`
- `tdd-developer`
- `design-implementation-reviewer`
- `critical-code-reviewer`
- `qa-bug-analyzer`
- `migration-validation-explorer`

### 追加予定スキル
- `completion-quality-gate-designer`
- `hidden-contract-investigator`
- `safe-by-default-architect`
- `cross-module-consistency-auditor`
- `production-parity-test-designer`

## 2. Phase-to-Skill Matrix

| Phase | Trigger / signal | Primary skills | Secondary skills | Required outputs |
|---|---|---|---|---|
| Project kickoff | プロジェクト開始、計画未作成、役割不明 | `project-plan-creator`, `project-manager`, `completion-quality-gate-designer` | `business-analyst` | 計画、RACI、quality gates |
| Requirement clarification | 要件が曖昧、業務ルール不明、既存仕様依存あり | `business-analyst`, `hidden-contract-investigator` | `project-manager` | 要件整理、暗黙契約一覧、未決事項 |
| Architecture / design | 危険領域設計、標準化不足、禁止事項を定めたい | `safe-by-default-architect`, `hidden-contract-investigator` | `project-completeness-scorer` | 設計方針、安全側標準、契約確認 |
| Implementation start | 実装着手、重要ロジック、リファクタ | `tdd-developer`, `design-implementation-reviewer` | `cross-module-consistency-auditor` | 実装計画、テスト方針、影響範囲 |
| Large / cross-cutting change | 2 モジュール以上、複数フロー、コピペ懸念 | `cross-module-consistency-auditor` | `design-implementation-reviewer` | 変更波及一覧、整合性チェック |
| Test design | test blind spot がありそう、本番差分あり | `production-parity-test-designer` | `migration-validation-explorer`, `tdd-developer` | test tier matrix、smoke 案、regression backlog |
| Bug trend review | バグ票が一定数ある、傾向を掴みたい | `qa-bug-analyzer` | `project-manager` | 品質傾向、ホットスポット、改善優先度 |
| Pre-merge critical review | 重要 PR、終盤、設計負債懸念 | `design-implementation-reviewer`, `critical-code-reviewer` | `cross-module-consistency-auditor` | 重大指摘、修正優先度 |
| Release readiness | リリース判定、残課題整理、完成度確認 | `project-completeness-scorer`, `completion-quality-gate-designer`, `critical-code-reviewer` | `qa-bug-analyzer` | readiness 判定、未了項目、例外台帳 |
| Data migration / environment change | データ移行、本番切替、環境差分 | `migration-validation-explorer`, `production-parity-test-designer` | `hidden-contract-investigator` | 検証観点、smoke、ロールバック確認 |

## 3. Trigger Heuristics

### `hidden-contract-investigator`
使う条件:
- 既存関数 / utility / API / DB schema を流用する
- 名前だけでは戻り値や副作用が読めない
- 既存資産の契約違反が致命傷になりうる

期待成果物:
- Hidden Contract Register
- Risky Assumption List
- Integration Notes

### `safe-by-default-architect`
使う条件:
- 認可、ファイル I/O、状態遷移、生 SQL、日時、外部連携が絡む
- 「禁止したい実装」が先に見えている
- 安全側標準を設計したい

期待成果物:
- Safe-by-default Rules
- Approved Patterns / Forbidden Patterns
- Design Guardrails

### `cross-module-consistency-auditor`
使う条件:
- 変更対象が複数モジュール・複数フローに跨る
- コピペ展開がある
- 集計や状態遷移ルールの一貫性が重要

期待成果物:
- Impact Map
- Consistency Checklist
- Propagation Checklist

### `production-parity-test-designer`
使う条件:
- 開発 / CI / 本番で DB・OS・依存関係・timezone 差がある
- UI 成功だけでは真の成功が言えない
- packaging / import / runtime まで見たい

期待成果物:
- Production Gap Inventory
- Test Tier Allocation Matrix
- PR Smoke Suite
- Adversarial Regression Backlog

### `completion-quality-gate-designer`
使う条件:
- 完了判定の語彙が曖昧
- テスト報告、完成報告、リリース判定の整合が弱い
- 例外運用を整理したい

期待成果物:
- Gate Matrix
- Definition of Done
- Exception Register
- Evidence Ownership Matrix

## 4. Work Item Routing Rules

新しい作業を受けたら、次の順に判断すること。

1. これは今どのフェーズの仕事か
2. どの品質ゲートに紐づく仕事か
3. hidden contract はあるか
4. safe-by-default を先に決めるべき危険領域か
5. 変更は単一モジュールか、横断変更か
6. 本番差分を見落としやすいか
7. マージ前 / リリース前の批判的レビューが必要か

## 5. Reporting Convention

主要タスクの開始時に、次の形式で先に宣言すること。

```text
Phase:
Active gate:
Selected skills:
Why these skills:
Primary risks:
Expected outputs:
```

主要タスクの終了時に、次の形式で締めること。

```text
What changed:
What was verified:
Current status: Implemented / Verified / Accepted / Released
Open risks:
Recommended next skill:
```
