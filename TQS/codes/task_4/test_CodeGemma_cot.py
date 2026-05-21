from remove_duplicates import *
import unittest
from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] == 1]

class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_unique_elements(self):
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_duplicate_elements(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_mixed_elements(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2.5, 4]), [1, 2, 3, 4])

    def test_large_list(self):
        numbers = list(range(1000)) + [1] * 100
        self.assertEqual(len(remove_duplicates(numbers)), 1000)

if __name__ == '__main__':
    unittest.main()