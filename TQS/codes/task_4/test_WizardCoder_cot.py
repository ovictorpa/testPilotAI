from remove_duplicates import *
import unittest
from typing import List

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4]) # Removes duplicates and keeps the original order.
        self.assertEqual(remove_duplicates([1, 1, 2, 3, 3, 4]), [2, 4]) # Only removes duplicates, not all elements.
        self.assertEqual(remove_duplicates([5, 6, 7, 8, 9]), [5, 6, 7, 8, 9]) # List with no duplicates.
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]) # List without duplicates has the same order as input.
        self.assertEqual(remove_duplicates([]), []) # Empty list is empty after removing duplicates.

    def test_remove_duplicates_edge_cases(self):
        # List with all elements being duplicate.
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), []) 
        # Negative integers and zero are kept in the output list.
        self.assertEqual(remove_duplicates([-5, -4, 0, 0, 3, 3]), [-5, -4, 0, 3])
        # List with all elements being different has the same order as input.
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        # List with a mix of duplicates and non-duplicates.
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()