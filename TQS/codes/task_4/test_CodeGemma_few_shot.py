from remove_duplicates import *
import unittest
from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] == 1]

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_remove_duplicates_with_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_with_single_element_list(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_remove_duplicates_with_duplicate_elements(self):
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])

    def test_remove_duplicates_with_mixed_data_types(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 'a', 'b']), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()