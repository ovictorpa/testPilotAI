from is_happy import *
import unittest

def is_happy(s):
    """
    Check if the string `s` is happy. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    """
    if len(s) < 3:
        return False
    
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
    return True

class TestIsHappy(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(is_happy(""))  # Empty string should not be happy
    def test_single_char(self):
        self.assertFalse(is_happy("a"))  # Single character string should not be happy
    def test_double_char(self):
        self.assertFalse(is_happy("aa"))  # Double characters should not be happy
    def test_triple_char(self):
        self.assertFalse(is_happy("aaa"))  # Triple characters with the same letter should not be happy
    def test_three_unique_chars(self):
        self.assertTrue(is_happy("abc"))  # Three unique characters should be happy
    def test_repeating_sequence(self):
        self.assertFalse(is_happy("abcd"))  # Repeating sequence should not be happy
    def test_non_repeating_sequence(self):
        self.assertTrue(is_happy("xyz"))  # Non-repeating sequence should be happy
    def test_mixed_case_unique(self):
        self.assertTrue(is_happy("aBc"))  # Mixed case, all unique characters should be happy
    def test_mixed_with_repeats(self):
        self.assertFalse(is_happy("aabbcc"))  # Not all unique characters should not be happy
    def test_longer_string_unique(self):
        self.assertTrue(is_happy("abcdefghijklmnopqrstuvwxyz"))  # All unique characters should be happy
    def test_alternating_case(self):
        self.assertFalse(is_happy("aBcDdEeFfGgHeEeFf"))  # Alternating case, not all unique should not be happy
    def test_trailing_whitespace(self):
        self.assertTrue(is_happy("abc "))  # Trailing whitespace and unique characters should be happy
    def test_leading_whitespace(self):
        self.assertTrue(is_happy(" abc"))  # Leading whitespace and unique characters should be happy
    def test_internal_whitespace(self):
        self.assertFalse(is_happy("a b c"))  # Internal whitespace and not all unique should not be happy
    def test_uppercase_sequence(self):
        self.assertTrue(is_happy("ABC"))  # All uppercase, unique characters should be happy
    def test_special_characters(self):
        self.assertFalse(is_happy("a!b@c#d$e%f&g*h"))  # Special characters should not be happy
    def test_empty_substring_in_middle(self):
        self.assertTrue(is_happy("abcdefgh "))  # Empty substring in the middle, rest unique should be happy

if __name__ == '__main__':
    unittest.main()