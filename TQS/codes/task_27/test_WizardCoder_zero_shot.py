import unittest
from remove_multiple_spaces import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    
    def test_remove_multiple_spaces(self):
        # Test case 1: multiple spaces to one space
        text1 = "   Hello     World"
        self.assertEqual("Hello World", remove_multiple_spaces(text1))
        
        # Test case 2: empty input
        text2 = ""
        self.assertEqual("", remove_multiple_spaces(text2))
        
        # Test case 3: only one space
        text3 = " "Hello World"
        self.assertEqual(text3, remove_multiple_spaces(text3))
        
        # Test case 4: single character input
        text4 = "H"
        self.assertEqual("H", remove_multiple_spaces(text4)
        
        # Test case 5: only spaces
        text5 = "   "
        self.assertEqual(" ", remove_multiple_spaces(text5)