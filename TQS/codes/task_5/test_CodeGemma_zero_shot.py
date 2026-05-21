from greatest_common_divisor import *
import unittest

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_gcd_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(-25, 15), 5)

    def test_gcd_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(25, 0), 25)

    def test_gcd_equal_numbers(self):
        self.assertEqual(greatest_common_divisor(5, 5), 5)

    def test_gcd_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            greatest_common_divisor(5, 0)


if __name__ == '__main__':
    unittest.main()