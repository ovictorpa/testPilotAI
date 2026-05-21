from remove_Occ import *
import unittest

def remove_occ(s, ch):
    """
    Removes all occurrences of character 'ch' from string s.
    
    Args:
        s (str): input string to process
        ch (char): character to be removed
    Returns:
        str: modified string without the character 'ch'
    """
    for i in range(len(s)):
        if s[i] == ch:
            s = s[:i] + s[i+1:]
    
    for i in range(len(s)-1, 0, -1):
        if s[i] == ch:
            s = s[:i] + s[i+1:]
    return s

class TestRemoveOcc(unittest.TestCase):
    def test_remove_occ(self):
        # Test case 1
        self.assertEqual(remove_occ('hello', 'l'), 'heo')
        
        # Test case 2
        self.assertEqual(remove_occ('word', 'w'), 'ord')
        
        # Test case 3
        self.assertEqual(remove_occ('aba', 'a'), 'b')
        
        # Test case 4
        self.assertEqual(remove_occ('abcdefghijk', 'f'), 'abcdeghijk')