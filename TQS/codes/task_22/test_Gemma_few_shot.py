from freq_count import *
import unittest

from collections import Counter

def freq_count(list1):
    return Counter(list1)


class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_count([]), Counter())

    def test_single_element(self):
        self.assertEqual(freq_count([1]), Counter({1: 1}))

    def test_multiple_elements(self):
        self.assertEqual(freq_count([1, 2, 3, 1]), Counter({1: 2, 2: 1, 3: 1}))

    def test_string(self):
        self.assertEqual(freq_count('aaabbcc'), Counter({'a': 3, 'b': 3, 'c': 2}))

if __name__ == '__main__':
    unittest.main()