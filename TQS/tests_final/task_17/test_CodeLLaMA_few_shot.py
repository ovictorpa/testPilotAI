import unittest
from decimal_To_Binary import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_To_Binary(0), 0)
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(3), 11)
        self.assertEqual(decimal_To_Binary(4), 100)
        self.assertEqual(decimal_To_Binary(5), 101)
        self.assertEqual(decimal_To_Binary(6), 110)
        self.assertEqual(decimal_To_Binary(7), 111)
        self.assertEqual(decimal_To_Binary(8), 1000)
        self.assertEqual(decimal_To_Binary(9), 1001)
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(11), 1011)
        self.assertEqual(decimal_To_Binary(12), 1100)
        self.assertEqual(decimal_To_Binary(13), 1101)
        self.assertEqual(decimal_To_Binary(14), 1110)
        self.assertEqual(decimal_To_Binary(15), 1111)

if __name__ == '__main__':
    unittest.main()