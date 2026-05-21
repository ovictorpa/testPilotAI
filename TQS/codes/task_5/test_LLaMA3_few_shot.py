from greatest_common_divisor import *
import unittest

class TestGCD(unittest.TestCase):

    def test_gcd_with_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(48, 18), 6)

    def test_gcd_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            greatest_common_divisor(4, 0)
        self.assertEqual(greatest_common_divisor(10, 0), 10)

    def test_gcd_with_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-3, -5), 1)
        self.assertEqual(greatest_common_divisor(-48, -18), 6)

    def test_gcd_with_large_numbers(self):
        self.assertEqual(greatest_common_divisor(10**6, 7*10**6), 7*10**6 // 7)

if __name__ == '__main__':
    unittest.main()