from check_Equality import *
import unittest

def check_Equality(s): 

    return (ord(s[0]) == ord(s[len(s) - 1])); 

def count_Substring_With_Equal_Ends(s): 

    result = 0; 

    n = len(s); 

    for i in range(n):

        for j in range(1,n-i+1): 

            if (check_Equality(s[i:i+j])): 

                result+=1; 

    return result; 

class TestCountSubstringWithEqualEnds(unittest.TestCase):
    def test_count_substring_with_equal_ends_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_count_substring_with_equal_ends_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_count_substring_with_equal_ends_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abba"), 4)

    def test_count_substring_with_equal_ends_string_without_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababa"), 2)

if __name__ == '__main__':
    unittest.main()