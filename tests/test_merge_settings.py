import unittest

from error_learning.merge_settings import merge_settings


class MergeSettingsTest(unittest.TestCase):
    def test_p002_ネストした部分更新で既存設定を保持する(self) -> None:
        current = {"theme": {"color": "blue", "font_size": 14}}
        patch = {"theme": {"font_size": 16}}

        self.assertEqual(
            merge_settings(current, patch),
            {"theme": {"color": "blue", "font_size": 16}},
        )


if __name__ == "__main__":
    unittest.main()
