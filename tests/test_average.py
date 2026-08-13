import unittest

from error_learning.average import average


class AverageTest(unittest.TestCase):
    def test_p005_端数を含む平均値を返す(self) -> None:
        self.assertEqual(average([2, 3]), 2.5)

    def test_p005_整数になる平均値も返す(self) -> None:
        self.assertEqual(average([2, 4]), 3.0)


if __name__ == "__main__":
    unittest.main()
