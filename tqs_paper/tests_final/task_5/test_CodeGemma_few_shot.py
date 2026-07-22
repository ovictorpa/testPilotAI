from greatest_common_divisor import *
import unittest

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_gcd_of_two_positive_integers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(42, 21), 21)

    def test_gcd_of_zero_and_positive_integers(self):
        self.assertEqual(greatest_common_divisor(0, 10), 10)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_gcd_of_negative_integers(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(-25, 15), 5)

if __name__ == '__main__':
    unittest.main()