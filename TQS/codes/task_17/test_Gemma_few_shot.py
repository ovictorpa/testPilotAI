from decimal_To_Binary import *
import unittest

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_To_Binary_basic(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_decimal_To_Binary_one(self):
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_decimal_To_Binary_ten(self):
        self.assertEqual(decimal_To_Binary(10), 1010)

    def test_decimal_To_Binary_twelve(self):
        self.assertEqual(decimal_To_Binary(12), 1100)

    def test_decimal_To_Binary_negative(self):
        with self.assertRaises(ValueError):
            decimal_To_Binary(-1)

if __name__ == '__main__':
    unittest.main()