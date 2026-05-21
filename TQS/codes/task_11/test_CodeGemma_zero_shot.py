import unittest

from all_prefixes import all_prefixes


class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_character_string(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_multiple_character_string(self):
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])

    def test_string_with_spaces(self):
        self.assertEqual(all_prefixes("hello world"), ["h", "he", "hel", "hell", "hello ", "hello w", "hello wo", "hello wor", "hello worl", "hello world"])


if __name__ == "__main__":
    unittest.main()