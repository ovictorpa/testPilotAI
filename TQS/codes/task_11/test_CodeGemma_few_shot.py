from all_prefixes import *
import unittest

class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_character_string(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_multiple_character_string(self):
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])

    def test_string_with_special_characters(self):
        self.assertEqual(all_prefixes("!@#$%^&*"), ["!", "!@", "!@#$", "!@#$%^", "!@#$%^&", "!@#$%^&*"])

    def test_string_with_numbers(self):
        self.assertEqual(all_prefixes("12345"), ["1", "12", "123", "1234", "12345"])

if __name__ == "__main__":
    unittest.main()