import unittest
from typing import List

from mean_absolute_deviation import mean_absolute_deviation  # Replace with the actual path to your function

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation_normal(self):
        """Test calculation of MAD for a list of numbers."""
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_with_zero(self):
        """Test calculation of MAD with a list containing zero."""
        self.assertAlmostEqual(mean_absolute_deviation([0.0, 2.5, 3.0]), 1.5)

    def test_mean_absolute_deviation_with_outliers(self):
        """Test calculation of MAD with outliers (e.g., large values)."""
        self.assertAlmostEqual(mean_absolute_deviation([-10.0, -5.0, -2.5, 0.0, 2.5]), 7.8)

    def test_mean_absolute_deviation_with_negative_numbers(self):
        """Test calculation of MAD with negative numbers."""
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, 3.0]), 2.0)

    def test_mean_absolute_deviation_empty_list(self):
        """Test calculation of MAD with an empty list."""
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])

    def test_mean_absolute_deviation_all_same(self):
        """Test calculation of MAD when all numbers are the same."""
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 1.0, 1.0]), 0.0)

    def test_mean_absolute_deviation_large_list(self):
        """Test calculation of MAD for a large list of numbers."""
        large_list = [float(i) for i in range(-1000, 1000)]
        self.assertAlmostEqual(mean_absolute_deviation(large_list), sum(abs(x - mean_absolute_deviation(large_list)) for x in large_list) / len(large_list))

    def test_mean_absolute_deviation_non_numeric_values(self):
        """Test calculation of MAD with non-numeric values (should raise ValueError)."""
        with self.assertRaises(ValueError):
            mean_absolute_deviation([1, 2, '3', None])

    def test_mean_absolute_deviation_all_zero(self):
        """Test calculation of MAD when all numbers are zero."""
        self.assertAlmostEqual(mean_absolute_deviation([0.0, 0.0, 0.0]), 0.0)

if __name__ == '__main__':
    unittest.main()