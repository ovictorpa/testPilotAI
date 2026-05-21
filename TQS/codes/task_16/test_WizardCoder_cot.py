import unittest
from remove_Occ import remove_Occ

class TestRemove(unittest.TestCase):
    
    def test_remove_occurrence(self):
        # Test Case 1: Character not present in string.
        self.assertEqual(remove_Occ('hello', 'x'), 'hello')
        
        # Test Case 2: Character is present only once.
        self.assertEqual(remove_Occ('xxhelloxxx', 'x'), 'hell')
        
        # Test Case 3: Character is present only once at the start of string.
        self.assertEqual(remove_Occ('xhello', 'x'), 'hello')
        
        # Test Case 4: Character is present only once at the end of string.
        self.assertEqual(remove_Occ('hellox', 'x'), 'helo')
        
        # Test Case 5: Character is present multiple times, both instances should be removed.
        self.assertEqual(remove_Occ('xxhelloworldxxx', 'x'), 'hellowrd')
        
        # Test Case 6: Character is present only once at the start and end of string.
        self.assertEqual(remove_Occ('xxxxhelloxxxx', 'x'), 'hell')