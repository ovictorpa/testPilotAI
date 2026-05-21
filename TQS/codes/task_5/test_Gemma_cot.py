from greatest_common_divisor import *
import unittest

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_negative_integers(self):
        self.assertEqual(greatest_common_divisor(-3, -5), 1)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_one(self):
        self.assertEqual(greatest_common_divisor(1, 1), 1)

    def test_large_integers(self):
        self.assertEqual(greatest_common_divisor(1000, 500), 100)

    def test_overflow(self):
        with self.assertRaises(ValueError):
            greatest_common_divisor(2**31, 2**31)


if __name__ == '__main__':
    unittest.main()