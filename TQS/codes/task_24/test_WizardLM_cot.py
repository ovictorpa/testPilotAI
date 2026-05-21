from check_Equality import *
import unittest

def check_equality(subseq):
    return ord(subseq[0]) == ord(subseq[-1])

def count_substring_with_equal_ends(s):
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(1, n - i + 1):
            if check_equality(s[i:i + j]):
                result += 1
    return result

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_substring_with_equal_ends(""), 0)
    
    def test_single_character(self):
        self.assertEqual(count_substring_with_equal_ends("a"), 1)
        self.assertEqual(count_substring_with_equal_ends("A"), 1)
        self.assertEqual(count_substring_with_equal_ends("z"), 0)
    
    def test_two_characters(self):
        self.assertEqual(count_substring_with_equal_ends("ab"), 0)
        self.assertEqual(count_substring_with_equal_ends("aa"), 1)
        self.assertEqual(count_substring_with_equal_ends("Aa"), 0)
    
    def test_substring_with_equal_ends(self):
        self.assertEqual(count_substring_with_equal_ends("abcde"), 3)  # "ab", "bc", "cd"
        self.assertEqual(count_substring_with_equal_ends("Rosalind"), 5)  # "Ro", "sl", "si", "nd", "ld"
    
    def test_no_equal_ends(self):
        self.assertEqual(count_substring_with_equal_ends("abcd"), 0)
    
    def test_case_sensitivity(self):
        self.assertEqual(count_substring_with_equal_ends("abcDE"), 1)  # "aD"
        self.assertEqual(count_substring_with_equal_ends("abcde"), 0)
    
    def test_multiple_occurrences(self):
        self.assertEqual(count_substring_with_equal_ends("abccba"), 4)  # "a", "b", "c", "cb"
    
    def test_multi_byte_characters(self):
        self.assertEqual(count_substring_with_equal_ends("éŸ“å›½"), 2)  # "éŸ“" and "å›½"
    
    def test_non_alphabetic_characters(self):
        self.assertEqual(count_substring_with_equal_ends("Hello, World!"), 0)
        self.assertEqual(count_substring_with_equal_ends("12345"), 1)  # "1" and "5"
    
    def test_large_string_performance(self):
        # This is a performance test rather than correctness
        s = 'a' * 10000  # A string with 100,000 'a' characters
        self.assertTrue(count_substring_with_equal_ends(s) > 0)
        # Note: This function has a quadratic time complexity, so it will be slow for large n.

if __name__ == '__main__':
    unittest.main()