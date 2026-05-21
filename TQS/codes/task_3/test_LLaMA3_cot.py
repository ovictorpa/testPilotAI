from is_happy import *
import unittest

class TestIsHappyFunction(unittest.TestCase):

    def test_short_string(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))

    def test_no_consecutive_letters(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("adb"))

    def test_repeated_letters(self):
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))

    def test_length_less_than_three(self):
        with self.assertRaises(ValueError):
            is_happy("abc")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            is_happy("")

    def test_longer_than_three_characters(self):
        # This case should also raise ValueError
        with self.assertRaises(ValueError):
            is_happy("abcdabc")

if __name__ == '__main__':
    unittest.main()