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
