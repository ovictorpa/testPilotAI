from freq_element import *
import unittest
from collections import Counter
from itertools import chain

def freq_element(nums):
    result = Counter(chain.from_iterable(nums))
    return result

class TestFreqElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_element([]), Counter())

    def test_single_list_with_unique_elements(self):
        self.assertEqual(freq_element([1, 2, 3]), Counter({1: 1, 2: 1, 3: 1}))

    def test_single_list_with_repeated_elements(self):
        self.assertEqual(freq_element([1, 1, 2, 2, 3]], Counter({1: 2, 2: 2, 3: 1}))

    def test_nested_lists(self):
        self.assertEqual(freq_element([[1, 2], [3, 4], [1, 2]]), Councer({1: 2, 2: 2, 3: 1, 4: 1}))

    def test_mixed_types(self):
        self.assertEqual(freq_element([1, 'a', (3, 4)]), Counter({1: 1, 'a': 1, (3, 4): 1}))

    def test_large_list(self):
        large_list = [i for i in range(1000)] * 2
        result = freq_element(large_list)
        self.assertEqual(result[1], 2000)  # There are 2000 occurrences of the number 1

    def test_with_none(self):
        self.assertIn(None, freq_element([1, None, 3]))

    def test_with_complex_objects(self):
        complex_objs = [[(1, 2), (3, 4)], [(5, 6)]]
        expected = Counter({(1, 2): 1, (3, 4): 1, (5, 6): 1})
        self.assertEqual(freq_element(complex_objs), expected)

    def test_with_duplicate_complex_objects(self):
        complex_objs = [[(1, 2)], [(1, 2)], [(3, 4), (3, 4)]]
        expected = Counter({(1, 2): 2, (3, 4): 2})
        self.assertEqual(freq_element(complex_objs), expected)

if __name__ == '__main__':
    unittest.main()