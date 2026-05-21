from freq_element import *
import unittest
from collections import Counter
from itertools import chain

class TestFreqElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_element([]), {})

    def test_single_element(self):
        self.assertEqual(freq_element([1]), {'1': 1})

    def test_multiple_elements(self):
        self.assertEqual(freq_element([1, 2, 3, 2, 1]), {'1': 2, '2': 2, '3': 1})

    def test_iterable(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(freq_element(nums), Counter({'1': 1, '2': 1, '3': 1, '4': 1}))