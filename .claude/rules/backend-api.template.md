---
paths:
  - "src/api/**/*"
  - "src/backend/**/*"
  - "app/controllers/**/*"
  - "app/services/**/*"
---

# Backend / API Rules

- 入力検証が必要な endpoint や service では、バリデーションの有無を確認する
- 認可が必要な操作では、opt-in ではなく明示的な保護を優先する
- 状態遷移がある処理では、不正遷移と二重実行を検討する
- 生 SQL や DB 方言依存を入れる場合は、移植性とテスト計画を先に示す
- 日時処理では timezone と naive / aware の混在リスクを確認する
- API 成功は、レスポンスだけでなく期待される永続化 / 副作用も含めて考える
