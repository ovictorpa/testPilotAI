from check_Equality import *
import unittest
from check_substring import count_Substring_With_Equal_Ends, check_Equality

class TestCountSubstring(unittest.TestCase):
    def test_empty_str(self):
        self.assertRaises(TypeError, count_Substring_With_Equal_Ends, "")
        
    def test_less_than_two_chars(self):
        self.assertRaises(ValueError, count_Substring_With_Equal_Ends, "h")
        
    def test_none_input(self):
        self.assertRaises(TypeError, count_Substring_With_Equal_Ends, None)
        
    def test_bool_input(self):
        self.assertRaises(TypeError, count_Substring_With_Equal_Ends, False)
        
    def test_single_char_input(self):
        s = "h"
        self.assertEqual(count_Substring_With_Equal_Ends(s), 0)
        
    def test_equal_ends(self):
        s = "abccba"
        self.assertEqual(count_Substring_With_Equal_Ends(s), 1)
        
    def test_unequal_ends(self):
        s = "abcde"
        self.assertEqual(count_Substring_With_Equal_Ends(s), 0)
        
    def test_unequal_length(self):
        s = "abccd"
        self.assertEqual(count_Substring_With_Equal_Ends(s), 2) # Should return the count of substrings with equal ends, not the number of substrings.
        
    def test_unequal_substrings(self):
        s = "abcdd"
        self.assertEqual(count_Substring_With_Equal_Ends(s), 1)