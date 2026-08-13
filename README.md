# エラーで学ぶ Python

Pythonの実行時不具合を、失敗する`unittest`から再現し、最小修正と回帰テストで学ぶ教材です。各章の`main`は成功状態で、失敗する状態はGit履歴に残します。

## 開始方法

```bash
git clone https://github.com/tonbiattack/error-driven-python-lab.git
cd error-driven-python-lab
PYTHONPATH=src python3 -m unittest discover -s tests
```

## 基礎コース

| # | テーマ | バグコミット |
| ---: | --- | --- |
| P001 | 可変の既定引数 | `8bb7288` |
| P002 | ネストした辞書の浅い更新 | `97e6035` |
| P003 | 未知の割引コード | `9518a28` |
| P004 | 空文字列と`None` | `ede5f2c` |
| P005 | 整数除算 | `63903ce` |

章ごとのRed → Green手順は[`fundamentals/README.md`](fundamentals/README.md)を参照してください。

## 検証

```bash
PYTHONPATH=src python3 -m compileall -q src
PYTHONPATH=src python3 -m unittest discover -s tests
```

## 文書

| 文書 | 内容 |
| --- | --- |
| [SUMMARY.md](SUMMARY.md) | コース目次 |
| [DESIGN.md](DESIGN.md) | Python固有の教材設計 |
| [coverage-matrix.md](coverage-matrix.md) | 実装済み・未着手テーマ |

## References

[1] [Learn Go with Tests](https://github.com/quii/learn-go-with-tests)

[2] [Python 3.12 documentation](https://docs.python.org/3.12/)
