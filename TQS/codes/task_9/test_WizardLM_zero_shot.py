from truncate_number import *
import unittest
from math import copysign

def truncate_number(number: float) -> float:
    """Return the decimal part of the number."""
    return number % 1.0

class TestTruncateNumber(unittest.TestCase):
    def test_positive_decimal(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(98.1234), 0.1234)
        self.assertEqual(truncate_number(123.456789), 0.456789)

    def test_positive_integer(self):
        self.assertEqual(truncate_number(5), 0.0)
        self.assertEqual(truncate_number(1), 0.0)

    def test_zero(self):
        self.assertAlmostEqual(truncate_number(0.0), 0.0, places=10)
        self.assertAlmostEqual(truncate_number(-0.0), 0.0, places=10)

    def test_negative_decimal(self):
        # The function should treat negative numbers as positive for the truncation operation.
        self.assertEqual(truncate_number(-3.5), 0.5)
        self.assertEqual(truncate_number(-98.1234), -0.1234)
        self.assertEqual(truncate_number(-123.456789), -0.456789)

    def test_large_numbers(self):
        large_positive = 1e308
        small_negative = -1e-308
        self.assertEqual(truncate_number(large_positive), 0.0)
        self.assertAlmostEqual(truncate_number(small_negative), 0.0, places=10)

    def test_edge_cases(self):
        # Test with the smallest non-zero positive and negative floats
        min_positive_float = float('1e-378')
        max_negative_float = -float('1e-379')
        self.assertAlmostEqual(truncate_number(min_positive_float), 0.0, places=10)
        self.assertEqual(truncate_number(max_negative_float), -0.0)

    def test_exact_integers(self):
        integer_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for value in integer_values:
            self.assertEqual(truncate_number(value), 0.0)

if __name__ == '__main__':
    unittest.main()