from greatest_common_divisor import *
import unittest

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, -15), 5)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 10), 10)
        self.assertEqual(greatest_common_divisor(10, 0), 10)

    def test_equal_numbers(self):
        self.assertEqual(greatest_common_divisor(5, 5), 5)

    def test_large_numbers(self):
        self.assertEqual(greatest_common_divisor(1000000007, 1000000009), 7)

if __name__ == '__main__':
    unittest.main()