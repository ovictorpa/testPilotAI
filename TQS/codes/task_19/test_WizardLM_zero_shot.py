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

class TestStringMethods(unittest.TestCase):
    def test_check_Equality_True(self):
        self.assertTrue(check_Equality("aabb"))
    
    def test_check_Equality_False(self):
        self.assertFalse(check_Equality("abcde"))
    
    def test_check_Equality_With_Spaces(self):
        self.assertTrue(check_Equality("Aa "))
    
    def test_check_Equality_With_Non_Alphanumeric_Characters(self):
        self.assertTrue(check_Equality("!@#"))
    
    def test_count_Substring_With_Equal_Ends(self):
        # Test cases for count_Substring_With_Equal_Ends
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 1)  # Only 'e' has equal ending with itself
        self.assertEqual(count_Substring_With_Equal_Ends("aabbcc"), 3)  # 'aa', 'bb', 'cc'
        self.assertEqual(count_Substring_With_Equal_Ends("abcdabcd"), 6)  # All substrings except 'bd'
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 1)
        self.assertEqual(count_Substring_With_Equal_Ends("ab"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 0)
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 4)  # 'ab', 'ba' twice
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
    
    def test_edge_cases(self):
        # Edge case scenarios
        self.assertEqual(count_Substring_With_Equal_Ends("aA1!"), 1)  # 'A!' ends with '!'
        self.assertEqual(count_Substring_With_Equal_Ends("a\nb"), 0)  # Line feed character in the middle
        self.assertEqual(count_Substring_With_Equal_Ends("\n"), 0)  # Only newline character
        self.assertEqual(count_Substring_With_Equal_Ends(" "), 0)  # Only space character
    
    def test_performance(self):
        # Test performance with a large string
        large_str = 'a' * 1000  # A string with 1000 'a' characters
        self.assertEqual(count_Substring_With_Equal_Ends(large_str), 999)  # All but the first and last character

if __name__ == '__main__':
    unittest.main()