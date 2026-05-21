from check_Equality import *
import unittest

def check_Equality(s):
    return ord(s[0]) == ord(s[-1])

def count_Substring_With_Equal_Ends(s):
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(1, n - i + 1):
            if check_Equality(s[i:i+j]):
                result += 1
    return result

class TestCountSubstringsWithEqualEnds(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("A"), 1)

    def test_equal_ending_substring(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 2)  # "ab" and "cd"

    def test_no_equal_ending_substring(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 0)

    def test_substrings_with_equal_ending_case_insensitive(self):
        self.assertEqual(count_Substring_With_Equal_Ends("HeLLo"), 3)  # "Hell", "Llo", "O"

    def test_longest_substring_at_start(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 1)  # "aaa" itself

    def test_multiple_equal_ending_substrings(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababab"), 4)  # "aba", "bab", "aba", "ab"

    def test_with_spaces(self):
        self.assertEqual(count_Substring_With_Equal_Ends("Hello World"), 2)  # "Hello" and "World"

    def test_mixed_case_preserves_case(self):
        self.assertEqual(count_Substring_With_Equal_Ends("HeLlO wOrLd"), 3)  # "HeLlO", "LlO", "rld" (case-sensitive)

    def test_performance_with_large_strings(self):
        large_str = 'a' * 1000
        self.assertEqual(count_Substring_With_Equal_Ends(large_str), 1000)  # All substrings end with 'a'

    def test_non_overlapping_substrings(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababbbab"), 4)  # "abab", "babba", "bbab", "b"

if __name__ == '__main__':
    unittest.main()