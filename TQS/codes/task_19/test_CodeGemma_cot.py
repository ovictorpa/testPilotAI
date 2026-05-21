from check_Equality import *
import unittest

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_palindrome_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 4)

    def test_non_palindrome_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcabc"), 3)

    def test_long_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefghijklmnopqrstuv"), 1)

if __name__ == '__main__':
    unittest.main()