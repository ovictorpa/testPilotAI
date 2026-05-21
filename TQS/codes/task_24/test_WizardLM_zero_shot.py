from check_Equality import *
import unittest

def check_Equality(s):
    return ord(s[0]) == ord(s[-1]) if s else True  # Handle empty string case

def count_Substring_With_Equal_Ends(s):
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(1, n - i + 1):
            if check_Equality(s[i:i+j]):
                result += 1
    return result

class TestStringMethods(unittest.TestCase):

    def test_check_Equality_with_equal_chars(self):
        self.assertTrue(check_Equality("aabbcc"))  # All characters are equal
        self.assertTrue(check_Equality("Hi"))  # Only two characters, equal
        self.assertFalse(check_Equality("HelloWorld!"))  # First and last characters are not equal
        self.assertTrue(check_Equality("abAB"))  # Case-insensitive equality
        self.assertFalse(check_Equality(""))  # Empty string should return True

    def test_count_Substring_With_Equal_Ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 3)  # All substrings end with 'd'
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 5)  # All substrings end with 'e'
        self.assertEqual(count_Substring_With_Equal_Ends("abXcd"), 2)  # Substrings "ab" and "cd" end with different characters
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)  # Only one substring, the whole string
        self.assertEqual(count_Substring_With_Equal_Ends(""), 1)  # Empty string should return count of 1 for the empty substring
        self.assertEqual(count_Substring_With_Equal_Ends("aabbcc"), 10)  # All possible substrings end with 'c'
        self.assertEqual(count_Substring_With_Equal_Ends("Hi there!"), 2)  # Substrings "Hi" and "there!" end with different characters
        self.assertEqual(count_Substring_With_Equal_Ends("abAB"), 9)  # All possible substrings end with 'B' or 'b' (case-insensitive)

if __name__ == '__main__':
    unittest.main()