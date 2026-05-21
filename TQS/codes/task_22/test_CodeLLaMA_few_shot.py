from freq_count import *
import unittest
from collections import Counter

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_count([]), {})

    def test_single_element_list(self):
        self.assertEqual(freq_count([1]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertEqual(freq_count([1, 2, 3, 2, 1]), {1: 2, 2: 2, 3: 1})