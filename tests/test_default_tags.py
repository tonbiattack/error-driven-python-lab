import unittest

from error_learning.default_tags import add_tag


class DefaultTagsTest(unittest.TestCase):
    def test_p001_呼び出しごとに新しいタグ一覧を返す(self) -> None:
        first = add_tag("python")
        second = add_tag("go")

        self.assertEqual(first, ["python"])
        self.assertEqual(second, ["go"])


if __name__ == "__main__":
    unittest.main()
