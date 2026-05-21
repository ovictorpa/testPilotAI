from check_Equality import *
import unittest

class TestCheckEquality(unittest.TestCase):  
    def test_empty_string(self):  # edge case
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
    
    def test_single_character_string(self):  # edge case
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)   # since there is no substring to compare with itself
    
    def test_no_substring_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefg"), 0)
    
    def test_single_substring_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 1)   # "aaa" is the only substring with equal ends.
    
    def test_multiple_substrings_with_one_equal_end(self):
        self.assertGreater(count_Substring_With_Equal_Ends("abbaabcde"), 1)   # "b" and "aba" have same ends.