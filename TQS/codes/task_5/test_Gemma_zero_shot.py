from greatest_common_divisor import *
import unittest

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_gcd_of_3_and_5(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_gcd_of_25_and_15(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_of_0_and_1(self):
        self.assertEqual(greatest_common_divisor(0, 1), 1)

    def test_gcd_of_1_and_1(self):
        self.assertEqual(greatest_common_divisor(1, 1), 1)

    def test_gcd_of_1_and_0(self):
        self.assertEqual(greatest_common_divisor(1, 0), 1)


if __name__ == '__main__':
    unittest.main()