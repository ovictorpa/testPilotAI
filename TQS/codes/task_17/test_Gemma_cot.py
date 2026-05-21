from decimal_To_Binary import *
import unittest

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary_positive(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(10), 1010)

    def test_decimal_to_binary_negative(self):
        with self.assertRaises(ValueError):
            decimal_To_Binary(-1)

    def test_decimal_to_binary_float(self):
        with self.assertRaises(ValueError):
            decimal_To_Binary(1.5)

    def test_decimal_to_binary_too_large(self):
        with self.assertRaises(ValueError):
            decimal_To_Binary(2**32)


if __name__ == '__main__':
    unittest.main()