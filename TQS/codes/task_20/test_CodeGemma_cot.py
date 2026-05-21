from freq_element import *
import unittest
from collections import Counter
from itertools import chain

def freq_element(nums):
  result = Counter(chain.from_iterable(nums))
  return result

class TestFreqElement(unittest.TestCase):

    def test_empty_list(self):
        nums = []
        expected = Counter()
        self.assertEqual(freq_element(nums), expected)

    def test_single_element(self):
        nums = [1]
        expected = Counter({1: 1})
        self.assertEqual(freq_element(nums), expected)

    def test_multiple_elements(self):
        nums = [1, 2, 2, 3]
        expected = Counter({1: 1, 2: 2, 3: 1})
        self.assertEqual(freq_element(nums), expected)

    def test_nested_lists(self):
        nums = [[1, 2], [2, 3], [1, 3]]
        expected = Counter({1: 2, 2: 2, 3: 2})
        self.assertEqual(freq_element(nums), expected)

    def test_large_dataset(self):
        nums = list(range(1000))
        expected = Counter({499: 2})
        self.assertEqual(freq_element(nums), expected)

if __name__ == '__main__':
    unittest.main()