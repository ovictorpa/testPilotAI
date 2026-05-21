from check_Equality import *
import unittest

class TestCountSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababa"), 4)

    def test_string_with_unequal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 0)


if __name__ == '__main__':
    unittest.main()