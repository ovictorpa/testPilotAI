from mean_absolute_deviation import *
import unittest
from typing import List

class MeanAbsoluteDeviationTests(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])

    def test_single_element_list(self):
        self.assertEqual(mean_absolute_deviation([1]), 0)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            mean_absolute_deviation(['a', 'b'])

    def test_negative_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1, 2, -3, 4]), 1)

    def test_large_number_of_elements(self):
        numbers = [i for i in range(1000)]
        self.assertGreaterEqual(mean_absolute_deviation(numbers), 0)