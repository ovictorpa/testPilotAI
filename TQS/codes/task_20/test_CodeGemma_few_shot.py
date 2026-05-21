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

    def test_single_element(self):
        self.assertEqual(freq_element([1]), Counter({1: 1}))

    def test_multiple_elements(self):
        self.assertEqual(freq_element([1, 2, 2, 3]), Counter({1: 1, 2: 2, 3: 1}))

    def test_non_integer_elements(self):
        self.assertEqual(freq_element(['a', 'b', 'c', 'a']), Counter({'a': 2, 'b': 1, 'c': 1}))

if __name__ == '__main__':
    unittest.main()