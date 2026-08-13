# 基礎Pythonエラーコース

各節は、バグ再現コミットでRedを観測し、`main`へ戻ってGreenを確認する独立した章です。

| # | テーマ | バグコミット | 完成実装 |
| ---: | --- | --- | --- |
| P001 | 可変の既定引数 | `8bb7288` | `default_tags.py` |
| P002 | ネストした辞書の浅い更新 | `97e6035` | `merge_settings.py` |
| P003 | `dict.get`による未知コードの見逃し | `9518a28` | `discounts.py` |
| P004 | 空文字列と`None`の取り違え | `ede5f2c` | `greeting.py` |
| P005 | 整数除算による平均値の切り捨て | `63903ce` | `average.py` |

## P001: 可変の既定引数

```bash
git checkout 8bb7288
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_default_tags.py'
git checkout main
```

`tags=[]`は関数定義時に一度だけ作られるため、呼び出し間で状態が共有されます。`None`を既定値にし、関数内で新しいリストを作ります。

## P002: ネストした辞書の浅い更新

```bash
git checkout 97e6035
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_merge_settings.py'
git checkout main
```

`current | patch`は最上位だけを更新します。ネストした設定を守る要件では、対象の辞書を再帰的にマージします。

## P003: 未知の割引コード

```bash
git checkout 9518a28
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_discounts.py'
git checkout main
```

`dict.get(code, 0)`は未知のコードを有効な割引なしとして扱います。契約が「未知コードは拒否」であれば、添字アクセスによる`KeyError`を使います。

## P004: 空文字列とNone

```bash
git checkout ede5f2c
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_greeting.py'
git checkout main
```

`name or "guest"`は空文字列も既定値へ置き換えます。未指定だけを判定するなら`name is None`を使います。

## P005: 整数除算

```bash
git checkout 63903ce
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_average.py'
git checkout main
```

`//`は端数を切り捨てます。平均値の端数を保持する契約では`/`を使います。

## 全章を実行する

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

## References

[1] [Learn Go with Tests](https://github.com/quii/learn-go-with-tests)

[2] [Python 3.12 documentation](https://docs.python.org/3.12/)
