# Project Start Checklist

## 1. Bootstrap Files

- [ ] `CLAUDE.md` を配置した
- [ ] `.claude/project-context.md` を作成した
- [ ] `.claude/skill-routing.md` を作成した
- [ ] `.claude/quality-gates.md` を作成した
- [ ] `.claude/decision-log.md` を作成した

## 2. Project Basics

- [ ] プロジェクト目的を書いた
- [ ] スコープ / 非スコープを書いた
- [ ] 関係者と承認者を書いた
- [ ] 目標リリース時期を書いた
- [ ] 環境差分（local / CI / staging / prod）を書いた

## 3. Skill Setup

- [ ] このプロジェクトで使う既存スキルを列挙した
- [ ] 追加予定スキルを列挙した
- [ ] フェーズごとの first-choice skill を決めた
- [ ] 重要トリガー（hidden contract / prod parity / cross-module）を明文化した

## 4. Quality Gate Setup

- [ ] G0〜G4 の exit criteria を仮置きした
- [ ] Status vocabulary を確認した
- [ ] Standard verification commands を記入した
- [ ] Exception register の形式を決めた

## 5. Technical Context

- [ ] 主要ディレクトリの役割を書いた
- [ ] 主要コマンドを書いた
- [ ] 主要な業務ルールを書いた
- [ ] 既知の危険領域を書いた
- [ ] 本番差分を書いた

## 6. First-session Readiness

- [ ] AI が最初に読むべき文書を決めた
- [ ] source of truth の優先順位を決めた
- [ ] 最新判断を `decision-log.md` に記録した
- [ ] 最初の機能または改修の `FEATURE_BRIEF.md` を作った

## 7. Human Review

- [ ] `CLAUDE.md` が長すぎないか確認した
- [ ] 役割やルールの矛盾がないか確認した
- [ ] 今回のプロジェクト特有の禁止事項を確認した

## 8. First Prompt Example

```text
このプロジェクトの bootstrap 文書を読んで、
1) 現在の phase
2) active gate
3) 直近で使うべきスキル
4) 最初に埋めるべき不足情報
を整理してください。
```
