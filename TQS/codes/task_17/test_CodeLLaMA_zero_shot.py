from decimal_To_Binary import *
TestCases:

class TestDecimalToBinary(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(0), 0)
        self.assertEqual(decimal_to_binary(1), 1)
        self.assertEqual(decimal_to_binary(2), 10)
        self.assertEqual(decimal_to_binary(3), 11)
        self.assertEqual(decimal_to_binary(4), 100)
        self.assertEqual(decimal_to_binary(5), 101)
        self.assertEqual(decimal_to_binary(6), 110)
        self.assertEqual(decimal_to_binary(7), 111)
        self.assertEqual(decimal_to_binary(8), 1000)
        self.assertEqual(decimal_to_binary(9), 1001)
        self.assertEqual(decimal_to_binary(10), 1010)