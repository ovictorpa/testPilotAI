from remove_Occ import *
import unittest

def remove_Occ(s, ch):
    """
    Remove all occurrences of a character from a string.

    Args:
        s (str): The input string.
        ch (str): The character to be removed.

    Returns:
        str: The modified string with the character removed.
    """

    # Check if the character exists in the string
    if not ch in s:
        return s  # No change needed

    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break

    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break

    return s  


class TestRemoveOcc(unittest.TestCase):

    def test_remove_occurance_from_empty_string(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_remove_occurance_not_found(self):
        self.assertEqual(remove_Occ("abc", "d"), "abc")

    def test_remove_all_occurrences_of_character_from_start(self):
        self.assertEqual(remove_Occ("aabbc", "a"), "bcc")

    def test_remove_all_occurrences_of_character_from_end(self):
        self.assertEqual(remove_Occ("ccbaa", "a"), "ccb")

    def test_remove_all_occurrences_of_character_from_middle(self):
        self.assertEqual(remove_Occ("abcbcaab", "b"), "abc")

if __name__ == '__main__':
    unittest.main()