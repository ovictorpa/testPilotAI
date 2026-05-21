from freq_element import *
import unittest
from collections import Counter
from itertools import chain

def freq_element(nums):
    result = Counter(chain.from_iterable(nums))
    return result

class TestFreqElementFunction(unittest.TestCase):
    def test_basic_functionality(self):
        nums = [[1, 2, 3], [4, 2, 2], [3, 4]]
        expected = Counter({1: 1, 2: 3, 3: 2, 4: 2})
        self.assertEqual(freq_element(nums), expected)
    
    def test_empty_lists(self):
        nums = [[], [1]]
        self.assertEqual(freq_element(nums), Counter({0: 1, 1: 1}))
    
    def test_all_elements_unique(self):
        nums = [[5, 6, 7], [8, 9, 10]]
        expected = Counter({5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3})
        self.assertEqual(freq_element(nums), expected)
    
    def test_duplicate_elements(self):
        nums = [[1, 1, 2], [2, 2, 2]]
        expected = Counter({1: 3, 2: 4})
        self.assertEqual(freq_element(nums), expected)
    
    def test_single_inner_list(self):
        nums = [[3, 5, 7]]
        expected = Counter({3: 3, 5: 3, 7: 3})
        self.assertEqual(freq_element(nums), expected)
    
    def test_mixed_types(self):
        nums = [[1, '2', 3], ['a', 4.5, 1]]
        expected = Counter({1: 2, '2': 1, 3: 1, 'a': 1, 4.5: 1})
        self.assertEqual(freq_element(nums), expected)
    
    def test_large_numbers(self):
        large_list = [i for i in range(1000000)]
        nums = [[large_list[:500000], large_list[500000:]]]
        expected = Counter({0: 500000, 1: 5e7})
        self.assertEqual(freq_element(nums), expected)
    
    def test_empty_input_list(self):
        self.assertEqual(freq_element([]), Counter())
    
    def test_non_list_elements(self):
        nums = [1, [2, 3], '4', 5]
        with self.assertRaises(TypeError):
            freq_element(nums)
    
    def test_nested_lists(self):
        nums = [[[1]], [[2, [3]]]]
        expected = Counter({1: 1, 2: 1, 3: 1})
        self.assertEqual(freq_element(nums), expected)
    
    def test_all_zeroes(self):
        nums = [[0, 0, 0], [0, 0, 0]]
        expected = Counter({0: 6})
        self.assertEqual(freq_element(nums), expected)

if __name__ == '__main__':
    unittest.main()