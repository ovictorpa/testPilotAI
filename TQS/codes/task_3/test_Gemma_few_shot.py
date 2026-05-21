from is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):

    def test_happy_string(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("adb"))

    def test_unhappy_string_len_less_than_3(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))

    def test_unhappy_string_repeating_letters(self):
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))

    def test_unhappy_string_consecutive_repeating_letters(self):
        self.assertFalse(is_happy("abcdeee"))


if __name__ == '__main__':
    unittest.main()