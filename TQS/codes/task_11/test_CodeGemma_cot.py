import unittest

from all_prefixes import all_prefixes


class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_character_string(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_multi_character_string(self):
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])

    def test_non_ascii_characters(self):
        self.assertEqual(all_prefixes("ä½ å¥½"), ["ä½ ", "ä½ å¥½"])

    def test_leading_spaces(self):
        self.assertEqual(all_prefixes(" abc"), [" ", "a", "ab", "abc"])

    def test_trailing_spaces(self):
        self.assertEqual(all_prefixes("abc "), ["a", "ab", "abc"])

    def test_duplicate_characters(self):
        self.assertEqual(all_prefixes("aaabb"), ["a", "aa", "aaa", "aaaa", "aaaaa"])


if __name__ == "__main__":
    unittest.main()