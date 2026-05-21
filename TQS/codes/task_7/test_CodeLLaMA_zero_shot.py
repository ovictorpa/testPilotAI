from mean_absolute_deviation import *
import unittest
from typing import List
from math import isclose

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mad_one_element(self):
        numbers = [1.0]
        mad = mean_absolute_deviation(numbers)
        self.assertEqual(mad, 0.0)

    def test_mad_two_elements(self):
        numbers = [1.0, 2.0]
        mad = mean_absolute_deviation(numbers)
        self.assertTrue(isclose(mad, 0.5))

    def test_mad_three_elements(self):
        numbers = [1.0, 2.0, 3.0]
        mad = mean_absolute_deviation(numbers)
        self.assertTrue(isclose(mad, 1.0))

    def test_mad_four_elements(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        mad = mean_absolute_deviation(numbers)
        self.assertTrue(isclose(mad, 1.0))

    def test_mad_five_elements(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        mad = mean_absolute_deviation(numbers)
        self.assertTrue(isclose(mad, 1.0))

    def test_mad_ten_elements(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        mad = mean_absolute_deviation(numbers)
        self.assertTrue(isclose(mad, 5.0))

if __name__ == "__main__":
    unittest.main()