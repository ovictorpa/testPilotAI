from freq_count import *
import unittest

from collections import Counter

def freq_count(list1):
    freq_count = Counter(list1)
    return freq_count


class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_count([]), Counter())

    def test_single_element(self):
        self.assertEqual(freq_count([1]), Counter({1: 1}))

    def test_multiple_elements(self):
        self.assertEqual(freq_count([1, 2, 2, 3]), Counter({1: 1, 2: 2, 3: 1}))

    def test_string_elements(self):
        self.assertEqual(freq_count(['a', 'b', 'c', 'a']), Counter({'a': 2, 'b': 1, 'c': 1}))

if __name__ == '__main__':
    unittest.main()