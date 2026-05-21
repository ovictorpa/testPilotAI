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

    def test_sorted_numbers(self):
        self.assertEqual(mean_absolute_deviation([1, 2, 3, 4]), 1)

    def test_descending_sorted_numbers(self):
        self.assertEqual(mean_absolute_deviation([4, 3, 2, 1]), 1)

    def test_zero_mean(self):
        self.assertEqual(mean_absolute_deviation([0, 0, 0]), 0)

    def test_large_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1000000, 1000001, 1000002]), 1)

if __name__ == '__main__':
    unittest.main()