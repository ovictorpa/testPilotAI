from mean_absolute_deviation import *
import unittest
from typing import List

class TestMeanAbsoluteDeviation(unittest.TestCase):
    
    def test_mean_absolute_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0) # Test case for a list of numbers that should result in mean deviation of 1.0
        
    def test_mean_absolute_deviation_empty(self):
        self.assertRaises(ValueError, mean_absolute_deviation, []) # Test case for an empty input list which should raise a ValueError exception
        
    def test_mean_absolute_deviation_negative(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, -2.0, 3.0, 4.0]), 1.5) # Test case for a list of numbers that have negative values
        
    def test_mean_absolute_deviation_float(self):
        self.assertAlmostEqual(mean_absolute_deviation([2.0, 2.1, 3.0, 4.0]), 0.4) # Test case for a list of numbers that have decimal values
        
    def test_mean_absolute_deviation_non_numeric(self):
        self.assertRaises(TypeError, mean_absolute_deviation, ["1", "2", "3"]) # Test case for a list of non-numeric values which should raise a TypeError exception
        
    def test_mean_absolute_deviation_one_element(self):
        self.assertAlmostEqual(mean_absolute_deviation([4]), 0) # Test case for a list with only one element, which should result in mean deviation of 0
        
if __name__ == '__main__':
    unittest.main()