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
├── PROJECT_START_CHECKLIST.md
├── FEATURE_BRIEF.md
└── .claude/
    ├── project-context.md
    ├── skill-routing.md
    ├── quality-gates.md
    ├── decision-log.md
    └── rules/
        ├── testing-quality.md
        └── backend-api.md
```

## 3. 最低限入れるべきもの

### 必須
1. `CLAUDE.md`
2. `.claude/project-context.md`
3. `.claude/skill-routing.md`
4. `.claude/quality-gates.md`

### 強く推奨
5. `.claude/decision-log.md`
6. `PROJECT_START_CHECKLIST.md`
7. `FEATURE_BRIEF.md`

### オプション
8. `.claude/rules/testing-quality.md`
9. `.claude/rules/backend-api.md`

## 4. なぜこの分け方にするか

### `CLAUDE.md`
最上位のオーケストレーターです。
「最初に何を読むか」「どの資料を優先するか」「進捗をどう表現するか」を短く固定します。

### `project-context.md`
プロジェクトの背景、スコープ、制約、アーキテクチャ、主要な業務ルールをまとめます。

### `skill-routing.md`
スキルの発火条件と成果物を定義します。
ここがないと、スキルが存在していても、いつ使うかが人依存になります。

### `quality-gates.md`
「実装完了」「検証完了」「出荷可能」を分けます。
スキルを使っても、どこで止まるべきかが曖昧だと再発防止になりません。

### `decision-log.md`
設計判断の蓄積です。
後からセッションが変わっても、なぜそうしたのかを辿れるようにします。

### `FEATURE_BRIEF.md`
新しい機能や改修を始めるたびに、対象範囲・受け入れ条件・リスク・使うスキルを整理します。

## 5. 推奨導入手順

### 15〜30分で最低限導入する流れ
1. `CLAUDE.md` を配置する
2. `.claude/project-context.md` を埋める
3. `.claude/skill-routing.md` に利用可能スキルを記入する
4. `.claude/quality-gates.md` に G0〜G4 を埋める
5. 最低 3 件の設計判断を `.claude/decision-log.md` に記録する
6. `PROJECT_START_CHECKLIST.md` を使って不足を洗う
7. 最初の主要機能は `FEATURE_BRIEF.md` から始める

## 6. 運用のコツ

- `CLAUDE.md` は短く保つ
- 詳細ルールは `.claude/rules/` に寄せる
- 大きな仕様変更をしたら `project-context.md` と `decision-log.md` を更新する
- フェーズが変わったら `quality-gates.md` の active gate を更新する
- 新スキルを導入したら `skill-routing.md` の trigger / output / owner を更新する

## 7. このパックに含まれるファイル

- `CLAUDE.md.template.md`
- `.claude/project-context.template.md`
- `.claude/skill-routing.template.md`
- `.claude/quality-gates.template.md`
- `.claude/decision-log.template.md`
- `PROJECT_START_CHECKLIST.template.md`
- `FEATURE_BRIEF.template.md`
- `.claude/rules/testing-quality.template.md`
- `.claude/rules/backend-api.template.md`

## 8. 導入後の最初のプロンプト例

```text
このリポジトリでは、まず CLAUDE.md に従って起動し、必要なら .claude/project-context.md、.claude/skill-routing.md、.claude/quality-gates.md、.claude/decision-log.md を読んでから、現状のフェーズと次に使うべきスキルを提案してください。
```
