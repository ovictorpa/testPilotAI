from check_Equality import *
import unittest

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_two_equal_characters_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 3)

    def test_three_equal_characters_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 6)

    def test_string_with_different_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ab"), 0)

    def test_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 4)

if __name__ == '__main__':
    unittest.main()