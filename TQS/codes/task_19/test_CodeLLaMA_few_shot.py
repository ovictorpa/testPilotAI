from check_Equality import *
import unittest

class TestCountSubstrings(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_substrings_with_equal_ends(''), 0)

    def test_single_char_string(self):
        self.assertEqual(count_substrings_with_equal_ends('a'), 1)

    def test_two_char_string(self):
        self.assertEqual(count_substrings_with_equal_ends('ab'), 2)

    def test_three_char_string(self):
        self.assertEqual(count_substrings_with_equal_ends('abc'), 3)

    def test_four_char_string(self):
        self.assertEqual(count_substrings_with_equal_ends('abcd'), 4)

    def test_five_char_string(self):
        self.assertEqual(count_substrings_with_equal_ends('abcde'), 5)

if __name__ == '__main__':
    unittest.main()