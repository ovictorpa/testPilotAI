from check_Equality import *
import unittest

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 4)

    def test_string_with_no_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 0)

    def test_string_with_mixed_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abbabc"), 3)

if __name__ == '__main__':
    unittest.main()