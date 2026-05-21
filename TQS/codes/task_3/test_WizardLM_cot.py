from is_happy import *
import unittest

class TestIsHappyFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_single_character(self):
        self.assertFalse(is_happy("a"))

    def test_less_than_three_characters(self):
        self.assertFalse(is_happy("ab"))

    def test_exactly_three_distinct_characters(self):
        self.assertTrue(is_happy("abc"))

    def test_repeated_characters(self):
        self.assertFalse(is_happy("aaa"))
        self.assertFalse(is_happy("abba"))

    def test_distinct_three_consecutive_characters(self):
        self.assertTrue(is_happy("xyz"))
        self.assertTrue(is_happy("abcdef"))

    def test_repeated_every_third_character(self):
        self.assertFalse(is_happy("aba"))
        self.assertFalse(is_happy("xyy"))

    def test_case_sensitivity(self):  # Assuming case sensitivity is desired
        self.assertTrue(is_happy("HeLlO"))
        self.assertTrue(is_happy("tEst123"))

    def test_non_alphabetical_string(self):  # Assuming the function only handles alphabetical strings
        with self.assertRaises(TypeError):
            is_happy("Hello123")

    def test_unicode_characters(self):
        self.assertTrue(is_happy("\u0068\u0065\u006C\u006F"))  # "hello" in Unicode
        self.assertFalse(is_happy("\u0068\u0068\u0068"))  # "hhh" (repeated characters)

    def test_long_string_with_distinct_blocks(self):
        self.assertTrue(is_happy("abcdefghijklmnopqrstuvwxyz"))

if __name__ == '__main__':
    unittest.main()