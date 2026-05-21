from freq_count import *
import unittest
from collections import Counter

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_count([]), {})

    def test_unique_elements(self):
        list1 = ['apple', 'banana', 'cherry']
        self.assertEqual(freq_count(list1), {'apple': 1, 'banana': 1, 'cherry': 1})

    def test_duplicates(self):
        list1 = ['apple', 'banana', 'cherry', 'apple']
        self.assertEqual(freq_count(list1), {'apple': 2, 'banana': 1, 'cherry': 1})

    def test_invalid_elements(self):
        list1 = ['apple', None, 10.5]
        with self.assertRaises(TypeError):
            freq_count(list1)

    def test_mixed_data_types(self):
        list1 = [1, 'banana', True]
        self.assertEqual(freq_count(list1), {'banana': 1})