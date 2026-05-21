from check_Equality import *
import unittest

class TestEquality(unittest.TestCase):
    def test_check_Equality(self):
        self.assertTrue(check_Equality('aba'))  # True, since ord('a') == ord('a')
        self.assertFalse(check_Equality('abcde'))  # False, since ord('b') != ord('e')
        self.assertTrue(check_Equality('a'))  # True, since ord('a') == ord('a')
        self.assertFalse(check_Equality(''))  # False, since empty string has no characters to compare
    
class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_count_Substring_With_Equal_Ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends('aba'), 1)  # 'aba' is the only substring with equal ends
        self.assertEqual(count_Substring_With_Equal_Ends('abaca'), 2)  # 'aba', 'ca' are the two substrings with equal ends
        self.assertEqual(count_Substring_With_Equal_Ends('abcdea'), 0)  # no substring has equal ends
        self.assertEqual(count_Substring_With_Equal_Ends('aaabbbcccd'), 4)  # 'a', 'ab', 'b', and 'bc' are the four substrings with equal ends