# 設計方針

Python版は、標準ライブラリの`unittest`だけで再現できる実行時不具合を扱います。可変の既定引数、辞書の浅い更新、`dict.get`、truthy判定、整数除算を選び、言語の便利な構文が業務上の契約を破る場面を小さなテストで観測します。

各題材は、テストが失敗するバグコミットと、同じテストを成功させる最小修正コミットを分離します。参考教材の段階的TDD手法を採用しますが、文章・コード・章名は複製しません。[1]

| 要素 | 方針 |
| --- | --- |
| テスト | Python標準の`unittest` |
| 実装 | `src/error_learning/`に完成コードを配置 |
| 実行 | `PYTHONPATH=src python3 -m unittest discover -s tests` |
| 検証 | `compileall`と全テスト |

[1] [Learn Go with Tests](https://github.com/quii/learn-go-with-tests)
