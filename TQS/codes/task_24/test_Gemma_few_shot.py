from check_Equality import *
import unittest

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_equal_ends_of_length_two(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 2)

    def test_unequal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 0)

    def test_long_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaabbccaa"), 3)


if __name__ == '__main__':
    unittest.main()