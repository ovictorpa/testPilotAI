from TQS.tests_final.task_3.is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):

    def test_short_string(self):
        self.assertFalse(is_happy("a"))
        self.assertFalse(is_happy("aa"))

    def test_distinct_letters(self):
        self.assertTrue(is_happy("abcd"))
        self.assertTrue(is_happy("adb"))

    def test_non_distinct_letters(self):
        self.assertFalse(is_happy("aabb"))
        self.assertFalse(is_happy("xyy"))

if __name__ == '__main__':
    unittest.main()