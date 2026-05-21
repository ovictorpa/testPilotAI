from truncate_number import *
import unittest
from typing import List

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into an integer part 
    (largest integer smaller than given number) and decimals (leftover part always smaller than 1). 
    Return the decimal part of the number.
    
    :param number: The input float number.
    :return: The decimal part of the input number as a float.
    """
    return number % 1.0

class TestTruncateNumber(unittest.TestCase):
    def test_positive_decimal(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
    
    def test_positive_no_decimal(self):
        self.assertEqual(truncate_number(4.), 0.)
    
    def test_negative_decimal(self):
        self.assertAlmostEqual(truncate_number(-3.5), -0.5)
    
    def test_positive_integer_part(self):
        self.assertEqual(truncate_number(6), 0.)
    
    def test_negative_integer_part(self):
        self.assertEqual(truncate_number(-6), -1.)  # Assuming a design change to return -1 for negative integers
    
    def test_zero(self):
        self.assertEqual(truncate_number(0.), 0.)
    
    def test_float_with_no_decimal_places(self):
        self.assertAlmostEqual(truncate_number(5.0), 0.)
    
    def test_large_positive_number(self):
        self.assertAlmostEqual(truncate_number(123456789.123456789), 0.123456789)
    
    def test_small_decimal_value(self):
        self.assertAlmostEqual(truncate_number(0.00000001), 1e-10)
    
    def test_non_integer_float_values(self):
        test_cases = [
            2.99, 0.05, -3.14159, 1.75825, float('inf'), float('-inf')
        ]
        expected_results = [
            0.0099999999, 0.000500000, -0.1415926535, 0.75825, float('inf'), float('-inf')
        ]
        for i, expected in enumerate(expected_results):
            self.assertAlmostEqual(truncate_number(test_cases[i]), expected)
    
    def test_string_input(self):
        self.assertEqual(truncate_number(str(3.5)), 0.5)

# Additional test for handling negative integers, if the behavior is to return -1 as per the comment in the test case:
def truncate_number_with_negative_integers(number: float) -> float:
    """
    Similar to `truncate_number`, but also handles negative integers by returning -1.
    
    :param number: The input float number.
    :return: The decimal part of the input number as a float or -1 for negative integers.
    """
    return number % 1.0 if number >= 0 else -1

class TestTruncateNumberWithNegativeIntegers(unittest.TestCase):
    def test_negative_integer_part_with_negative_integers(self):
        self.assertEqual(truncate_number_with_negative_integers(-6), -1.)

if __name__ == '__main__':
    unittest.main()