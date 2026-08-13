import unittest

from error_learning.greeting import build_greeting


class GreetingTest(unittest.TestCase):
    def test_p004_空文字列は未指定として扱わない(self) -> None:
        self.assertEqual(build_greeting(""), "Hello, !")

    def test_p004_noneの場合だけ既定の名前を使う(self) -> None:
        self.assertEqual(build_greeting(None), "Hello, guest!")


if __name__ == "__main__":
    unittest.main()
