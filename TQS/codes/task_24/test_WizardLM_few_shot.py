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

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_one_character_substring(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("b"), 1)

    def test_substring_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdcba"), 3)

    def test_no_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefg"), 0)

    def test_substring_with_one_equal_end(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abXc"), 1)

    def test_substring_with_internal_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 2)

    def test_substring_with_spaces(self):
        self.assertEqual(count_Substring_With_Equal_Ends("hello world"), 1)

    def test_substring_with_non_printable_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("\x01\x02\x03\x04"), 1)

    def test_large_substring(self):
        large_str = 'a' * 1000  # A large string with 'a' characters
        self.assertEqual(count_Substring_With_Equal_Ends(large_str), 1000)

    def test_substring_with_special_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("!@#$%^&*()"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("!abc!"), 1)

    def test_performance_with_large_substrings(self):
        large_str = 'a' * 1000  # A large string with 'a' characters
        large_substring = large_str[:500]
        self.assertEqual(count_Substring_With_Equal_Ends(large_substring), 499)

if __name__ == '__main__':
    unittest.main()