# Quality Gates

## 1. Status Vocabulary

このプロジェクトでは、進捗語彙を次のように固定する。

- `Implemented`: 実装は終わった
- `Verified`: 標準検証が終わった
- `Accepted`: 承認者が受け入れた
- `Released`: 本番反映済み
- `Exception-approved`: 未了項目つきで例外承認された

## 2. Active Gate

- Current active gate: `[G0 / G1 / G2 / G3 / G4]`
- Last updated by:
- Last updated at:

## 3. Gate Matrix

### G0 — Project Ready

**Goal**
- 目的、スコープ、関係者、制約、初期リスクを整理する

**Entry criteria**
- 企画または要求が存在する

**Exit criteria**
- `project-context.md` が埋まっている
- `skill-routing.md` が埋まっている
- `quality-gates.md` が初期化されている
- 最初の重要リスクが列挙されている

**Recommended skills**
- `project-plan-creator`
- `project-manager`
- `completion-quality-gate-designer`

**Evidence**
- Project context
- 初期計画
- 初期リスク一覧

### G1 — Design Ready

**Goal**
- 設計方針、境界、責務、安全側標準を固める

**Entry criteria**
- G0 通過
- 要件と業務ルールが主要部分で整理済み

**Exit criteria**
- 主要コンポーネントの責務が明確
- 危険領域の safe-by-default 方針が明確
- 既存資産の hidden contract が確認済み
- 変更影響が大きい箇所の整合性観点が定義済み

**Recommended skills**
- `safe-by-default-architect`
- `hidden-contract-investigator`
- `cross-module-consistency-auditor`

**Evidence**
- 設計メモ
- 契約確認メモ
- 影響範囲一覧

### G2 — Implementation Ready

**Goal**
- 実装が統合前に壊れにくい状態で揃っている

**Entry criteria**
- G1 通過
- 実装単位と担当が明確

**Exit criteria**
- 実装対象コードが揃っている
- 最低限の unit / integration test が追加されている
- 横断変更の propagation checklist が更新済み
- 重要変更は design-implementation review 済み

**Recommended skills**
- `tdd-developer`
- `design-implementation-reviewer`
- `cross-module-consistency-auditor`

**Evidence**
- 変更一覧
- テスト追加一覧
- レビュー結果

### G3 — Verification Ready

**Goal**
- 本番前に見るべき失敗が見える状態になっている

**Entry criteria**
- G2 通過
- テスト実行環境が揃っている

**Exit criteria**
- Production gap inventory がある
- 必須 smoke / parity test が通っている
- E2E は UI だけでなく persistence も確認している
- 既知制約と未了項目が台帳化されている

**Recommended skills**
- `production-parity-test-designer`
- `qa-bug-analyzer`
- `migration-validation-explorer`

**Evidence**
- test tier matrix
- smoke 実行結果
- 既知制約一覧

### G4 — Release Ready

**Goal**
- 出荷可否を判断できるだけの証跡が揃っている

**Entry criteria**
- G3 通過
- リリース対象と対象外が明確

**Exit criteria**
- 完了 / 検証 / 承認 / 出荷の状態が明確
- 重大レビュー指摘の扱いが整理済み
- 未了項目は例外承認または解消済み
- リリース後の監視 / ロールバック確認項目がある

**Recommended skills**
- `project-completeness-scorer`
- `completion-quality-gate-designer`
- `critical-code-reviewer`

**Evidence**
- readiness summary
- exception register
- final review summary

## 4. Exception Register

| Item | Why not done | Risk | Compensating control | Due date | Owner | Approver |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 5. Standard Verification Commands

- Lint:
- Unit:
- Integration:
- E2E:
- Smoke / parity:
- Packaging / build:

## 6. Gate Review Notes

| Date | Gate | Result | Notes | Next action |
|---|---|---|---|---|
|  |  |  |  |  |
