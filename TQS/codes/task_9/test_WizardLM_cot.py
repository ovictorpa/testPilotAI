from truncate_number import *
import unittest
from math import floor

def truncate_number(number: float) -> float:
    """Given a positive floating point number, return the decimal part of the number."""
    return number - floor(number)

class TestTruncateNumber(unittest.TestCase):
    def test_positive_greater_than_one(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
    
    def test_exactly_one(self):
        self.assertAlmostEqual(truncate_number(1.0), 0.0)
    
    def test_positive_less_than_one(self):
        self.assertAlmostEqual(truncate_number(0.75), 0.25)
    
    def test_equals_integer(self):
        self.assertAlmostEqual(truncate_number(4.0), 0.0)
    
    def test_close_to_zero(self):
        self.assertAlmostEqual(truncate_number(3.9999), 0.9999)
    
    def test_repeating_decimal(self):
        self.assertAlmostEqual(truncate_number(1./3.), 0.3333)
    
    def test_large_numbers(self):
        large_num = 1e10
        self.assertAlmostEqual(truncate_number(large_num), large_num % 1)
    
    def test_small_numbers_close_to_zero(self):
        small_num = 1e-10
        self.assertAlmostEqual(truncate_number(small_num), small_num % 1)
    
    def test_negative_numbers(self):
        negative_num = -3.5
        self.assertAlmostEqual(truncate_number(negative_num), -0.5)
    
    def test_special_floats(self):
        self.assertAlmostEqual(truncate_number(float('nan')), float('nan'))
        self.assertAlmostEqual(truncate_number(float('inf')), 0.0)
        self.assertAlmostEqual(truncate_number(-float('inf')), -0.0)

if __name__ == '__main__':
    unittest.main()