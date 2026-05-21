from remove_duplicates import *
import unittest
from typing import List, Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    
    """
    From a list of integers, remove all elements that occur more than once.
    Keep the order of the elements left the same as in the input.
    """
    c = Counter(numbers)
    return [n for n in numbers if c[n] == 1]

class TestRemoveDuplicates(unittest.TestCase):
    
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([0, 1, 2, 2, 3, 3, 4, 5]), [0, 1, 4, 5])
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4, 5, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(remove_duplicates([1, 2, 2, 2, 3, 3, 3, 4, 4]), [1, 4])
        
if __name__ == '__main__':
    unittest.main()