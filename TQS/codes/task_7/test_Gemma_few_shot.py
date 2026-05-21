from mean_absolute_deviation import *
import unittest

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:

    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_single_element(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)

    def test_basic_case(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_large_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([100.0, 200.0, 300.0, 400.0]], 100.0), 100.0)

    def test_negative_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)


if __name__ == '__main__':
    unittest.main()