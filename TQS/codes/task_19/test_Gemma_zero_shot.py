from check_Equality import *
import unittest

class TestSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_equal_ends_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaabbccdd"), 4)

    def test_unequal_ends_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcabcde"), 0)

    def test_long_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcabcdeffedcba"), 6)


if __name__ == '__main__':
    unittest.main()