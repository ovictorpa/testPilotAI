from remove_duplicates import *
import unittest
from typing import List

class TestRemoveDuplicates(unittest.TestCase):

    
    def test_remove_duplicates(self):
        self.assertEqual([1, 3, 4], remove_duplicates([1, 2, 3, 2, 4]))
        self.assertEqual([1, 2, 3], remove_duplicates([1, 2, 3, 2, 3]))
        self.assertEqual([], remove_duplicates([]))
        
if __name__ == '__main__':
    unittest.main()