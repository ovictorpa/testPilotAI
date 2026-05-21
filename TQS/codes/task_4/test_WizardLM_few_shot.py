from remove_duplicates import *
import unittest
from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = Counter(numbers)
    return [n for n in numbers if c[n] == 1]

class TestRemoveDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 3, 2]), [1, 3, 2])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])

    def test_all_unique(self):
        self.assertEqual(remove_duplicates([5, 7, 9, 11, 13]), [5, 7, 9, 11, 13])

    def test_mixed(self):
        self.assertEqual(remove_duplicates([7, 2, 7, 5, 2, 3]), [2, 7, 5, 3])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_one_element(self):
        self.assertEqual(remove_duplicates([42]), [42])

if __name__ == '__main__':
    unittest.main()