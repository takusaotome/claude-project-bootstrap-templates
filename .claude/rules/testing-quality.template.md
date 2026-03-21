# Testing and Quality Rules

- 新しい重要ロジックは、少なくとも unit test または integration test のどちらで守るかを明示する
- UI テストだけで成功を主張しない。必要に応じて persistence または副作用まで確認する
- 既知 defect は、可能なら regression test 候補として残す
- mock を使った場合は、何が未検証かを明示する
- 本番差分がある箇所は、別途 smoke / parity の要否を確認する
- 変更完了報告では、実装完了と検証完了を分けて報告する
