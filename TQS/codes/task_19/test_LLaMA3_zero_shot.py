from check_Equality import *
import unittest

def check_Equality(s):
    """
    Checks if the first and last characters of a string are equal.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the first and last characters are equal, False otherwise.
    """
    return ord(s[0]) == ord(s[-1])

def count_Substring_With_Equal_Ends(s):
    """
    Counts the number of substrings in a string where the first and last characters are equal.

    Args:
        s (str): The input string.

    Returns:
        int: The number of substrings with equal starts and ends.
    """
    result = 0
    n = len(s)

    for i in range(n):
        for j in range(1, n - i + 1):
            if check_Equality(s[i:i+j]):
                result += 1

    return result


class TestFunctions(unittest.TestCase):

    def test_check_equality(self):
        self.assertTrue(check_Equality("aaa"))
        self.assertFalse(check_Equality("abc"))

    def test_count_substring_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aa"), 3)
        self.assertEqual(count_Substring_With_Equal_Ends("abab"), 4)

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_single_character(self):
        self.assertEqual(count/Substring_With_Equal_Ends("a"), 1)


if __name__ == '__main__':
    unittest.main()