from is_happy import *
import unittest

class TestIsHappy(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(is_happy(''))

    def test_one_letter_string(self):
        self.assertFalse(is_happy('a'))

    def test_two_letter_string(self):
        self.assertFalse(is_happy('ab'))

    def test_three_letter_string(self):
        self.assertTrue(is_happy('abc'))

    def test_four_letter_string(self):
        self.assertFalse(is_happy('abcd'))

    def test_five_letter_string(self):
        self.assertTrue(is_happy('aabbc'))

    def test_six_letter_string(self):
        self.assertFalse(is_happy('aabbbc'))

if __name__ == '__main__':
    unittest.main()