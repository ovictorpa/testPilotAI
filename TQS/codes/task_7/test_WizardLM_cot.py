from mean_absolute_deviation import *
import unittest
from typing import List

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
    
    def test_negative_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 3.0)
    
    def test_mixed_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 1.0, -3.0, 5.0]), 5.0)
    
    def test_zero_in_list(self):
        self.assertEqual(mean_absolute_deviation([0.0, 1.0, 2.0]), 1.5)
    
    def test_all_zeros(self):
        self.assertAlmostEqual(mean_absolute_deviation([0.0, 0.0, 0.0]), 0.0)
    
    def test_one_element(self):
        self.assertAlmostEqual(mean_absolute_deviation([3.0]), 0.0)
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])
    
    def test_duplicate_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([2.0, 2.0, 3.0]), 1.0)
    
    def test_large_dataset(self):
        large_data = [i + 1 for i in range(1000)]
        self.assertAlmostEqual(mean_absolute_deviation(large_data), mean(abs(x - mean(large_data)) for x in large_data))
    
    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            mean_absolute_deviation(['a', 'b', 2.0])

if __name__ == '__main__':
    unittest.main()