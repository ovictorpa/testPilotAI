from decimal_To_Binary import *
import unittest

def decimal_To_Binary(N):
    # Your original function implementation here
    pass

class TestDecimalToBinary(unittest.TestCase):

    def test_binary_conversion(self):
        self.assertEqual(decimal_To_Binary(5), 101)

    def test_single_digit(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            decimal_To_Binary(-5)

    def test_zero(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_large_numbers(self):
        self.assertEqual(decimal_To_Binary(255), 11111111)
        self.assertEqual(decimal_To_Binary(1024), 10000000000)

if __name__ == '__main__':
    unittest.main()