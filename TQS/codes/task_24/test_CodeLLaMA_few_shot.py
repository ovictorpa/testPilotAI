from check_Equality import *
def check_Equality(s):
    """
    Check if the first and last characters of a string are equal.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the first and last characters of the string are equal, False otherwise.
    """
    return ord(s[0]) == ord(s[-1])

def count_Substring_With_Equal_Ends(s):
    """
    Count the number of substrings in a string where the first and last characters are equal.

    Args:
        s (str): The input string.

    Returns:
        int: The number of substrings in the string where the first and last characters are equal.
    """
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(1, n - i + 1):
            if check_Equality(s[i:i+j]):
                result += 1
    return result

# Test cases
class TestCheckEquality(unittest.TestCase):
    def test_check_equality_empty_string(self):
        self.assertFalse(check_Equality(''))

    def test_check_equality_single_char_string(self):
        self.assertTrue(check_Equality('a'))
        self.assertFalse(check_Equality('ab'))

    def test_check_equality_multiple_char_string(self):
        self.assertTrue(check_Equality('aba'))
        self.assertFalse(check_Equality('abab'))

class TestCountSubstringsWithEqualEnds(unittest.TestCase):
    def test_count_substrings_with_equal_ends_empty_string(self):
        self.assertEqual(0, count_Substring_With_Equal_Ends(''))

    def test_count_substrings_with_equal_ends_single_char_string(self):
        self.assertEqual(1, count_Substring_With_Equal_Ends('a'))

    def test_count_substrings_with_equal_ends_multiple_char_string(self):
        self.assertEqual(2, count_Substring_With_Equal_Ends('abab'))

if __name__ == '__main__':
    unittest.main()