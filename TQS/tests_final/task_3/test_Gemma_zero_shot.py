from TQS.tests_final.task_3.is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_happy(""), False)

    def test_string_less_than_3_characters(self):
        self.assertEqual(is_happy("a"), False)
        self.assertEqual(is_happy("aa"), False)

    def test_string_with_repeating_characters(self):
        self.assertEqual(is_happy("abb"), False)
        self.assertEqual(is_happy("aab"), False)

    def test_happy_string(self):
        self.assertEqual(is_happy("abcd"), True)
        self.assertEqual(is_happy("adb"), True)

    def test_string_with_consecutive_repeating_characters(self):
        self.assertEqual(is_happy("xyy"), False)


if __name__ == "__main__":
    unittest.main()