from freq_element import *
import unittest
from collections import Counter
from itertools import chain

def freq_element(nums):
    result = Counter(chain.from_iterable(nums))
    return result

class TestFreqElementFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(freq_element([]), "The function should return None for an empty list of lists.")

    def test_single_sublist(self):
        nums = [[1, 2, 3], [4, 5, 6]]
        expected_counter = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
        self.assertEqual(freq_element(nums), expected_counter, "The function should correctly count elements in a list with one sublist.")

    def test_mixed_types(self):
        nums = [[1, 'a'], [2, 3.5], [4, 'a', 3.5]]
        expected_counter = Counter({1: 1, 'a': 2, 2: 1, 3.5: 2})
        self.assertEqual(freq_element(nums), expected_counter, "The function should correctly count elements with mixed types.")

    def test_all_same(self):
        nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        expected_counter = Counter({1: 3, 2: 3, 3: 3})
        self.assertEqual(freq_element(nums), expected_counter, "The function should correctly handle all elements being the same.")

    def test_duplicates(self):
        nums = [[1, 2], [1, 2], [3, 4, 2]]
        expected_counter = Counter({1: 2, 2: 3, 3: 2, 4: 1})
        self.assertEqual(freq_element(nums), expected_counter, "The function should correctly handle elements that appear multiple times.")

    def test_empty_sublists(self):
        nums = [[], [3, 4], [5]]]
        expected_counter = Counter({3: 2, 4: 1, 5: 1})
        self.assertEqual(freq_element(nums), expected_counter, "The function should correctly handle sublists with zero length.")

    def test_nested_lists(self):
        nums = [[[1, 2], [3]], [[4], [5, 6]]]
        expected_counter = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
        self.assertEqual(freq_element(nums), expected_counter, "The function should correctly handle nested lists.")

    def test_case_insensitivity(self):
        nums = [['a', 'B'], ['b', 'A']]
        expected_counter = Counter({'a': 1, 'b': 1, 'B': 1})
        self.assertEqual(freq_element(nums), expected_counter, "The function should be case-insensitive.")

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            freq_element('not a list')

if __name__ == '__main__':
    unittest.main()