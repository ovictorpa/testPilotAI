from freq_element import *
import unittest
from collections import Counter
from itertools import chain

def freq_element(nums):
    result = Counter(chain.from_iterable(nums))
    return result

class TestFreqElementFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_element([]), {})

    def test_single_element_repeated_multiple_times(self):
        self.assertEqual(freq_element([1, 1, 1]), {1: 3})

    def test_multiple_elements_in_list(self):
        self.assertEqual(freq_element([1, 2, 3, 2, 3]), Counter({1: 1, 2: 2, 3: 2}))

    def test_duplicate_values_in_single_element(self):
        self.assertEqual(freq_element([1, 2, 2]), Counter({1: 1, 2: 2}))

    def test_all_elements_unique(self):
        self.assertEqual(freq_element([1, 2, 3, 4, 5]), Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1}))

    def test_single_value_list_with_negative_numbers(self):
        self.assertEqual(freq_element([-1, -1, -1]), {(-1): 3})

if __name__ == '__main__':
    unittest.main()