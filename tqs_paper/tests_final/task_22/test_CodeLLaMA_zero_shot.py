from freq_count import *
import unittest
from collections import Counter

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        list1 = []
        expected = {}
        self.assertEqual(freq_count(list1), expected)

    def test_single_element(self):
        list1 = [1]
        expected = {1: 1}
        self.assertEqual(freq_count(list1), expected)

    def test_multiple_elements(self):
        list1 = [1, 2, 3, 2, 1]
        expected = {1: 2, 2: 2, 3: 1}
        self.assertEqual(freq_count(list1), expected)

if __name__ == '__main__':
    unittest.main()