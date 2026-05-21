from TQS.tests_final.task_3.is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_happy(""))

    def test_string_less_than_3_characters(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("ab"))

    def test_distinct_letters(self):
        self.assertTrue(is_happy("abc"))
        self.assertTrue(is_happy("def"))

    def test_non_distinct_letters(self):
        self.assertFalse(is_happy("aab"))
        self.assertFalse(is_happy("abb"))

    def test_long_string_with_distinct_letters(self):
        self.assertTrue(is_happy("abcdefghijklmnopqrstuvwxyz"))

    def test_long_string_with_non_distinct_letters(self):
        self.assertFalse(is_happy("aaabbccddeee"))

if __name__ == '__main__':
    unittest.main()