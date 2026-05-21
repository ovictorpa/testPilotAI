from freq_count import *
import unittest

from collections import Counter

def freq_count(list1):
    freq_count = Counter(list1)
    return freq_count


class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_count([]), Counter())

    def test_non_hashable(self):
        with self.assertRaises(TypeError):
            freq_count([lambda: 1, 2, 3])

    def test_basic_counting(self):
        list1 = [1, 2, 2, 3, 3]
        expected = Counter([1: 1, 2: 2, 3: 2])
        self.assertEqual(freq_count(list1), expected)

    def test_counting_multiple(self):
        list1 = [1, 1, 2, 2, 3, 3]
        expected = Counter([1: 2, 2: 2, 3: 2])
        self.assertEqual(freq_count(list1), expected)


if __name__ == '__main__':
    unittest.main()