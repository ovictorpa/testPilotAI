from decimal_To_Binary import *
import unittest

class TestDecimalToBinary(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(decimal_To_Binary(8), 1000)
        self.assertEqual(decimal_To_Binary(16), 10000)

    def test_zero(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            decimal_To_Binary(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary("a")

    def test_large_number(self):
        self.assertEqual(decimal_To_Binary(2**31 - 1), 1111111111111111111111111111111)

    def test_edge_case(self):
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)

if __name__ == '__main__':
    unittest.main()