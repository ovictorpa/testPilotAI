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
        self.assertEqual(freq_element([1, 2, 3, 1, 2]), Counter({1: 2, 2: 2, 3: 1}))

    def test_string_elements(self):
        self.assertEqual(freq_element(['a', 'b', 'c', 'a', 'b']), Counter({'a': 2, 'b': 2, 'c': 1}))

    def test_mixed_types(self):
        self.assertEqual(freq_element([1, 'a', 3.14, 1, 'a']), Counter({1: 2, 'a': 2, '3.14': 1}))


if __name__ == '__main__':
    unittest.main()