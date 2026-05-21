from decimal_To_Binary import *
import unittest

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary_positive(self):
        self.assertEqual(decimal_To_Binary(5), 101)

    def test_decimal_to_binary_negative(self):
        self.assertEqual(decimal_To_Binary(-5), -101)

    def test_decimal_to_binary_zero(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_decimal_to_binary_large_number(self):
        self.assertEqual(decimal_To_Binary(4096), 100000000000)

    def test_decimal_to_binary_small_number(self):
        self.assertEqual(decimal_To_Binary(2), 10)

if __name__ == '__main__':
    unittest.main()