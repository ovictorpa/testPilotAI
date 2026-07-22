from is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):

    def test_short_string(self):
        self.assertFalse(is_happy("a"))

    def test_duplicate_letters(self):
        self.assertFalse(is_happy("aa"))

    def test_distinct_letters(self):
        self.assertTrue(is_happy("abcd"))

    def test_consecutive_duplicates(self):
        self.assertFalse(is_happy("aabb"))

    def test_different_first_and_last(self):
        self.assertTrue(is_happy("adb"))

    def test_duplicate_middle_letters(self):
        self.assertFalse(is_happy("xyy"))

if __name__ == '__main__':
    unittest.main()