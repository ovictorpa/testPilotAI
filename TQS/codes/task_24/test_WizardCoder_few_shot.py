from check_Equality import *
import unittest

def check_Equality(s):
    return ord(s[0]) == ord(s[len(s)-1])

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_empty_input(self):
        self.assertRaises(Exception, count_Substring_With_Equal_Ends(""))
        
    def test_single_char_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)
        
    def test_simple_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 2)
        
    def test_complex_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdedefgfhijkkkjbba"), 4)
        
    def test_check_Equality_function(self):
        self.assertTrue(check_Equality("aa"))
        self.assertFalse(check_Equality("abc"))
        self.assertTrue(check_Equality("aba"))