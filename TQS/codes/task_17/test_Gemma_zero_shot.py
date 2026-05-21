from decimal_To_Binary import *
import unittest

class TestDecimalToBinary(unittest.TestCase):

    def test_DecimalToBinary_Zero(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_DecimalToBinary_One(self):
        self.assertEqual(decimal_ToBinary(1), 1)

    def test_DecimalToBinary_Two(self):
        self.assertEqual(decimal_ToBinary(2), 10)

    def test_DecimalToBinary_Three(self):
        self.assertEqual(decimal_ToBinary(3), 11)

    def test_DecimalToBinary_Ten(self):
        self.assertEqual(decimal_ToBinary(10), 1010)

    def test_DecimalToBinary_Negative(self):
        with self.assertRaises(ValueError):
            decimal_ToBinary(-1)


if __name__ == '__main__':
    unittest.main()