from check_Equality import *
import unittest

def check_Equality(s):
    return (ord(s[0]) == ord(s[-1]))

def count_Substring_With_Equal_Ends(s):
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(1, n - i + 1):
            if check_Equality(s[i:i+j]):
                result += 1
    return result

class TestCountSubstrings(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("z"), 1)

    def test_strings_with_equal_characters_at_both_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 2)
        self.assertEqual(count_Substring_With_Equal_Ends("Amani"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("12345"), 1)

    def test_strings_without_equal_characters_at_both_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("HelloWorld"), 0)

    def test_substring_with_equal_characters_at_both_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abXcd"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("abcabc"), 3)

    def test_mixed_case_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("HelloWorld"), 0)

    def test_non_ascii_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("Hola Mundo"), 1)

    def test_leading_trailing_whitespace(self):
        self.assertEqual(count_Substring_With_Equal_Ends("   abXcd   "), 0)
        self.assertEqual(count_Substring_With_Equal_Ends(" abXcd "), 1)

    def test_performance_with_long_strings(self):
        # This is a performance test to ensure that the function scales reasonably well.
        long_str = 'a' * 10000
        self.assertEqual(count_Substring_With_Equal_Ends(long_str), 1)

    def test_strings_with_repeated_characters_at_both_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aaa"), 2)

if __name__ == '__main__':
    unittest.main()