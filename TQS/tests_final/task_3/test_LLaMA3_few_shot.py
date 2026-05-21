import unittest
from TQS.tests_final.task_3.is_happy import is_happy  # replace 'your_module' with the actual name of your module

class TestIsHappy(unittest.TestCase):

    def test_short_string(self):
        self.assertFalse(is_happy("a"))

    def test_two_repeated_letters(self):
        self.assertFalse(is_happy("aa"))

    def test_distinct_three_letters(self):
        self.assertTrue(is_happy("abc"))

    def test_two_consecutive_repeats(self):
        self.assertFalse(is_happy("aab"))

    def test_three_consecutive_repeats(self):
        self.assertFalse(is_happy("aaa"))

    def test_distinct_four_letters(self):
        self.assertTrue(is_happy("abcd"))

    def test_no_repeats_in_first_two(self):
        self.assertTrue(is_happy("abxy"))  # note that the last character is not tested here, as it's not in the group of three

    def test_one_consecutive_repeat(self):
        self.assertFalse(is_happy("aabbxy"))  

    def test_all_distinct_letters(self):
        self.assertTrue(is_happy("xyz"))

if __name__ == '__main__':
    unittest.main()