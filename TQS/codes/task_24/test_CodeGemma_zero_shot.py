from check_Equality import *
import unittest

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_palindrome_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 6)

    def test_string_with_different_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 0)

    def test_string_with_equal_ends_at_different_positions(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abaa"), 3)

if __name__ == '__main__':
    unittest.main()