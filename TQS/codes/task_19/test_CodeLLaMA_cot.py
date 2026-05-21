from check_Equality import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_count_Substring_With_Equal_Ends(self):
        # Test case 1: Empty string
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

        # Test case 2: String with only one character
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

        # Test case 3: String with multiple characters
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefg"), 7)

        # Test case 4: String with repeated characters
        self.assertEqual(count_Substring_With_Equal_Ends("aaaaa"), 5)

        # Test case 5: String with special characters
        self.assertEqual(count_Substring_With_Equal_Ends("abcd$%^&*()_+"), 7)

def check_Equality(s):
    return (ord(s[0]) == ord(s[-1]))

def count_Substring_With_Equal_Ends(s):
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(1,n-i+1):
            if (check_Equality(s[i:i+j])):
                result+=1
    return result