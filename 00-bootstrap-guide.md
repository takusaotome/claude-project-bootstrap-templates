# Claude Project Bootstrap Templates

作成日: 2026-03-21

## 1. 目的

このテンプレートパックは、新しいプロジェクトを始めるときに、AI エージェントが最初から次を理解できる状態を素早く作るためのものです。

- このプロジェクトは何を作るのか
- 何が品質ゲートなのか
- どのフェーズでどのスキルを使うのか
- どの文書を事実の一次情報として扱うのか
- 設計判断がどこに残っているのか

狙いは、セッションごとに同じ説明をやり直さなくてよい状態を作ることです。

## 2. 推奨構成

```text
your-project/
├── CLAUDE.md
├── FEATURE_BRIEF.md
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
    ├── CROSS_MODULE_CONSISTENCY_MATRIX.md
    └── PROJECT_KICKOFF_CHECKLIST.md
```

`docs/` はプロジェクトの一次情報、`.claude/` は Claude Code の実行時ルールやコマンドを置く場所です。

## 3. 最低限入れるべきもの

### 必須
1. `CLAUDE.md`
2. `docs/PROJECT_BRIEF.md`
3. `docs/SKILL_ROUTING.md`
4. `docs/QUALITY_GATES.md`
5. `docs/TEST_STRATEGY.md`

### 強く推奨
6. `docs/DECISION_LOG.md`
7. `docs/PROJECT_KICKOFF_CHECKLIST.md`
8. `FEATURE_BRIEF.md`

### オプション
9. `.claude/rules/testing-and-release.md`
10. `.claude/rules/backend-api.md`
11. `.claude/rules/db-and-migrations.md`

## 4. なぜこの分け方にするか

### `CLAUDE.md`
最上位のオーケストレーターです。
「最初に何を読むか」「どの資料を優先するか」「進捗をどう表現するか」を短く固定します。

### `docs/PROJECT_BRIEF.md`
プロジェクトの背景、スコープ、制約、アーキテクチャ、主要な業務ルールをまとめます。

### `docs/SKILL_ROUTING.md`
スキルの発火条件と成果物を定義します。
ここがないと、スキルが存在していても、いつ使うかが人依存になります。

### `docs/QUALITY_GATES.md`
「実装完了」「検証完了」「出荷可能」を分けます。
スキルを使っても、どこで止まるべきかが曖昧だと再発防止になりません。

### `docs/TEST_STRATEGY.md`
unit / integration / e2e / production parity の責務を分け、検証盲点を減らします。

### `docs/DECISION_LOG.md`
設計判断の蓄積です。
後からセッションが変わっても、なぜそうしたのかを辿れるようにします。

### `FEATURE_BRIEF.md`
新しい機能や改修を始めるたびに、対象範囲・受け入れ条件・リスク・使うスキルを整理します。

## 5. 推奨導入手順

### 15〜30分で最低限導入する流れ
1. `CLAUDE.md` を配置する
2. `docs/PROJECT_BRIEF.md` を埋める
3. `docs/SKILL_ROUTING.md` に利用可能スキルを記入する
4. `docs/QUALITY_GATES.md` に完了判定を埋める
5. `docs/TEST_STRATEGY.md` に標準検証コマンドと parity 観点を埋める
6. 最低 1 件の設計判断を `docs/DECISION_LOG.md` に記録する
7. `docs/PROJECT_KICKOFF_CHECKLIST.md` を使って不足を洗う
8. 最初の主要機能は `FEATURE_BRIEF.md` から始める

## 6. 運用のコツ

- `CLAUDE.md` は短く保つ
- 詳細ルールは `.claude/rules/` に寄せる
- 大きな仕様変更をしたら `docs/PROJECT_BRIEF.md` と `docs/DECISION_LOG.md` を更新する
- フェーズが変わったら `docs/QUALITY_GATES.md` の該当ゲートを更新する
- 新スキルを導入したら `docs/SKILL_ROUTING.md` の trigger / output / owner を更新する
- プレースホルダーを増減したら `placeholders.yml` と README を更新し、`python3 scripts/validate_templates.py` を実行する

## 7. このパックに含まれるファイル

- `CLAUDE.md.template.md`
- `docs/PROJECT_BRIEF.template.md`
- `docs/SKILL_ROUTING.template.md`
- `docs/QUALITY_GATES.template.md`
- `docs/TEST_STRATEGY.template.md`
- `docs/DECISION_LOG.template.md`
- `docs/HIDDEN_CONTRACT_REGISTER.template.md`
- `docs/CROSS_MODULE_CONSISTENCY_MATRIX.template.md`
- `docs/PROJECT_KICKOFF_CHECKLIST.template.md`
- `FEATURE_BRIEF.template.md`
- `.claude/rules/backend-api.md.template.md`
- `.claude/rules/db-and-migrations.md.template.md`
- `.claude/rules/testing-and-release.md.template.md`
- `.claude/commands/project-kickoff.md.template.md`
- `placeholders.yml`
- `scripts/validate_templates.py`

## 8. 導入後の最初のプロンプト例

```text
このリポジトリでは、まず CLAUDE.md に従って起動し、必要なら docs/PROJECT_BRIEF.md、docs/SKILL_ROUTING.md、docs/QUALITY_GATES.md、docs/TEST_STRATEGY.md、docs/DECISION_LOG.md を読んでから、現状のフェーズと次に使うべきスキルを提案してください。
```
