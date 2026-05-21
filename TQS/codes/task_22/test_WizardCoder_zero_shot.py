from freq_count import *
import unittest
from collections import Counter, defaultdict
from itertools import product

class TestFreqCount(unittest.TestCase):
    def test_freq_count_empty(self):
        self.assertEqual(Counter([]), freq_count([]))

    def test_freq_count_single_element(self):
        list1 = [1]
        self.assertDictEqual({1: 1}, freq_count(list1))

    def test_freq_count_repeated_elements(self):
        list1 = [1,2,3,4,5,6,7,8] * 2
        self.assertDictEqual({1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2}, freq_count(list1))

    def test_freq_count_duplicate_elements(self):
        list1 = [1,1,2,2,3,3,4] * 5
        self.assertDictEqual({1: 5, 2: 5, 3: 5, 4: 5}, freq_count(list1))

    def test_freq_count_mixed_elements(self):
        list1 = [1,2,'a','b',3.5,True] * 2
        self.assertDictEqual({'a': 2, 'b': 2, 1: 2, 2: 2, 3.5: 2, True: 2}, freq_count(list1))

    def test_freq_count_with_none(self):
        list1 = [None, None, 'a', False] * 2 + [0]
        self.assertDictEqual({'a': 2, False: 2, 0: 1, None: 2}, freq_count(list1))