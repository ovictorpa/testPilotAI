from check_Equality import *
import unittest

class TestEquality(unittest.TestCase):
    def test_count_substrings_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("abbaca"), 2) # "a", "ba"
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefgfedc"), 3) # "abcd", "bcde", "cdef"
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 2) # "aa", ""
        self.assertEqual(count_Substring_With_Equal_Ends("aabbccdd"), 0)