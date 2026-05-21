from is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_string_less_than_3_characters(self):
        self.assertFalse(is_happy("a"))

    def test_string_with_repeating_characters(self):
        self.assertFalse(is_happy("aa"))

    def test_happy_string(self):
        self.assertTrue(is_happy("abcd"))

    def test_happy_string_with_repeating_characters_but_not_consecutive(self):
        self.assertTrue(is_happy("adb"))

    def test_unhappy_string_with_consecutive_repeating_characters(self):
        self.assertFalse(is_happy("xyy"))


if __name__ == '__main__':
    unittest.main()