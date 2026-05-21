from mean_absolute_deviation import *
import unittest
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_with_positive_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
    
    def test_mean_absolute_deviation_with_negative_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)
    
    def test_mean_absolute_deviation_with_mixed_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.5, 2.0, 3.5, -4.0]), 2.875)
    
    def test_mean_absolute_deviation_with_one_element(self):
        self.assertAlmostEqual(mean_absolute_deviation([5.0]), 0.0)
    
    def test_mean_absolute_deviation_with_no_elements(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])
    
    def test_mean_absolute_deviation_with_non_numeric_values(self):
        with self.assertRaises(TypeError):
            mean_absolute_deviation([1, '2', 3])
    
    def test_mean_absolute_deviation_with_all_zeroes(self):
        self.assertAlmostEqual(mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]), 0.0)
    
    def test_mean_absolute_deviation_with_large_numbers(self):
        large_numbers = [1e9, 2e9, 3e9, 4e9]
        self.assertAlmostEqual(mean_absolute_deviation(large_numbers), 1e9)
    
    def test_mean_absolute_deviation_with_small_numbers(self):
        small_numbers = [0.001, 0.002, 0.003, 0.004]
        self.assertAlmostEqual(mean_absolute_deviation(small_numbers), 0.0025)

if __name__ == '__main__':
    unittest.main()