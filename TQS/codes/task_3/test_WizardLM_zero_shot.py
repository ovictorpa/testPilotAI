from is_happy import *
import unittest

def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
    return True

class TestIsHappy(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(is_happy(""))  # Empty string should not be happy

    def test_single_character_string(self):
        self.assertFalse(is_happy("a"))  # Single character string should not be happy

    def test_two_characters_string(self):
        self.assertFalse(is_happy("aa"))  # Two identical characters should not be happy

    def test_three_distinct_characters(self):
        self.assertTrue(is_happy("abc"))  # Three distinct characters should be happy

    def test_repeating_characters(self):
        self.assertFalse(is_happy("aabb"))  # Repeating characters should not be happy

    def test_identical_characters_at_end(self):
        self.assertTrue(is_happy("adb"))  # Characters different and identical at the end

    def test_alternating_characters(self):
        self.assertTrue(is_happy("xyx"))  # Alternating characters should be happy

    def test_non_distinct_consecutive_characters(self):
        self.assertFalse(is_happy("xyy"))  # Two 'y's in a row, not distinct

    def test_longer_string_with_distinct_characters(self):
        self.assertTrue(is_happy("abcdabcde"))  # Longer string with distinct characters

    def test_mixed_case_characters(self):
        self.assertTrue(is_happy("AbCdEfGhIjKlMnOpQrStTvWxYz"))  # Mixed case should be happy

    def test_non_alphabetic_characters(self):
        self.assertTrue(is_happy("123abc"))  # Non-alphabetic characters followed by alphabetic should be happy

    def test_all_spaces(self):
        self.assertFalse(is_happy("   "))  # All spaces should not be happy

    def test_leading_trailing_spaces(self):
        self.assertTrue(is_happy(" abc  "))  # Leading and trailing spaces with distinct characters in between

    def test_repeating_characters_in_middle(self):
        self.assertFalse(is_happy("aabc"))  # Repeating character in the middle should not be happy

    def test_repeating_characters_at_end(self):
        self.assertTrue(is_happy("abcab"))  # Repeating characters at the end should be happy

    def test_repeating_characters_edge_case(self):
        self.assertFalse(is_happy("aabbcc"))  # Repeating characters that span the length requirement

if __name__ == '__main__':
    unittest.main()