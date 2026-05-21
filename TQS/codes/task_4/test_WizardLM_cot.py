from remove_duplicates import *
import unittest
from typing import List
import collections

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates_basic(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_all_duplicates(self):
        self.assertEmpty(remove_duplicates([1, 1, 1]))

    def test_mixed_frequencies(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertEmpty(remove_duplicates([]))

    def test_single_element(self):
        self.assertEqual(remove_duplicates([7]), [7])

    def test_mixed_data_types(self):
        # Assuming non-integer types are ignored
        self.assertEqual(remove_duplicates(['1', 2, '3', 4]), [1, 2, 4])

    def test_large_numbers(self):
        large_list = [10**6 - 1, 10**6, 10**6 + 1]
        self.assertEqual(remove_duplicates(large_list), [10**6 - 1, 10**6 + 1])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplicates([-1, -2, -3, -2]), [-1, -3])

    def test_case_sensitivity(self):
        # Assuming this function only handles integers and is not case-sensitive
        self.assertEqual(remove_duplicates(['a', 'b', 'a', 'c']), ['a', 'b', 'c'])

    def test_case_insensitivity_with_integers(self):
        # Assuming we want to filter out non-integer types regardless of case
        self.assertEqual(remove_duplicates([1, '2', 3, '2']), [1, 3])

    def test_order_preservation(self):
        self.assertEqual(remove_duplicates([5, 4, 40, 40, 2]), [5, 40, 2])

if __name__ == '__main__':
    unittest.main()