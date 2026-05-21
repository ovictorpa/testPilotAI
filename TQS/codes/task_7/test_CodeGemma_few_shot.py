from mean_absolute_deviation import *
import unittest

from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), float('nan'))

    def test_single_element_list(self):
        self.assertEqual(mean_absolute_deviation([1]), 0)

    def test_sorted_list(self):
        self.assertEqual(mean_absolute_deviation([1, 2, 3, 4]), 1)

    def test_unsorted_list(self):
        self.assertEqual(mean_absolute_deviation([4, 2, 3, 1]), 1)

    def test_large_list(self):
        numbers = list(range(100))
        self.assertAlmostEqual(mean_absolute_deviation(numbers), 49.5, places=2)

if __name__ == '__main__':
    unittest.main()