#!/usr/bin/env bash
set -euo pipefail

for file in README.md SUMMARY.md DESIGN.md coverage-matrix.md fundamentals/README.md; do
  test -s "$file" || { echo "必要な教材ファイルがありません: $file" >&2; exit 1; }
done

git diff --check
PYTHONPATH=src python3 -m compileall -q src
PYTHONPATH=src python3 -m unittest discover -s tests

echo "Pythonエラー学習コースの検証に成功しました。"
