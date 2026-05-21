from check_Equality import *
import unittest
from your_module import count_Substring_With_Equal Ends  # Import the function from the module where it is defined

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_count_empty_string(self):
        self.assertEqual(count_Substring_With_Equal Ends(""), 0)

    def test_single_character_substring(self):
        self.assertEqual(count_Substring_With_Equal Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal Ends("A"), 1) # Test for uppercase 'a'

    def test_no_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal Ends("hello"), 0)

    def test_equal_ends_in_small_substring(self):
        self.assertEqual(count_Substring_With_Equal Ends("aaa"), 3)
        self.assertEqual(count_Substring_With_Equal Ends("aba"), 1) # Test for different cases

    def test_equal_ends_in_longer_substring(self):
        self.assertEqual(count_Substring_With_Equal Ends("ababcabcba"), 11)

    def test_whitespace_in_string(self):
        self.assertEqual(count_Substring_With_Equal Ends("ab a b c"), 1)
        # Test for spaces in string

    def test_equal_ends_with_spaces(self):
        self.assertEqual(count_Substring_With_Equal Ends("a b b a "), 2)

if __name__ == '__main__':
    unittest.main()