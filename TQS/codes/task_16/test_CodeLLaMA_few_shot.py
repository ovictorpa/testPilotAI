from remove_Occ import *
import unittest
class TestRemoveOcc(unittest.TestCase):
    def test_remove_occ(self):
        self.assertEqual(remove_occ('hello', 'l'), 'heo')
        self.assertEqual(remove_occ('hello', 'h'), 'ello')
        self.assertEqual(remove_occ('hello', 'z'), 'hello')

# Note: The above test cases are just examples, you can add more test cases to check different scenarios.

# Also, you may want to add a docstring to the function to describe its purpose and parameters.
def remove_occ(s, ch):
    """
    Remove all occurrences of character 'ch' from string 's'.

    Parameters:
        s (str): The input string.
        ch (str): The character to be removed.

    Returns:
        str: The resulting string after removing all occurrences of character 'ch'.
    """
    # Iterate through the string and remove the character
    for i in range(len(s)):
        if s[i] == ch:
            s = s[0 : i] + s[i + 1:]
            break

    # Remove the character from the end of the string as well
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ch:
            s = s[0 : i] + s[i + 1:]
            break

    return s