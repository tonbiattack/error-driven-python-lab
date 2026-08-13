import unittest

from error_learning.discounts import discount_for


class DiscountsTest(unittest.TestCase):
    def test_p003_未登録の割引コードを拒否する(self) -> None:
        with self.assertRaisesRegex(KeyError, "UNKNOWN"):
            discount_for("UNKNOWN", {"WELCOME": 10})

    def test_p003_登録済みの割引コードの値を返す(self) -> None:
        self.assertEqual(discount_for("WELCOME", {"WELCOME": 10}), 10)


if __name__ == "__main__":
    unittest.main()
