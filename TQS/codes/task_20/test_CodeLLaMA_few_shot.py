from freq_element import *
import unittest
from collections import Counter
from itertools import chain

class TestFreqElement(unittest.TestCase):
    def test_single_list(self):
        nums = [[1, 2, 3], [4, 5, 6]]
        result = freq_element(nums)
        self.assertEqual(result, Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}))

    def test_empty_list(self):
        nums = []
        result = freq_element(nums)
        self.assertEqual(result, Counter({}))

    def test_nested_lists(self):
        nums = [[[1], [2]], [[3], [4]]]
        result = freq_element(nums)
        self.assertEqual(result, Counter({1: 1, 2: 1, 3: 1, 4: 1}))