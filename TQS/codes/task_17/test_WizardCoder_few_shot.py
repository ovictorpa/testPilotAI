from decimal_To_Binary import *
import unittest
class TestDecimalToBinary(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_To_Binary(5), 101) # 2 in binary is 101 (base 2)
        self.assertEqual(decimal_To_Binary(6), 110) # 3 in binary is 110 (base 2)
        self.assertEqual(decimal_To_Binary(9), 1001) # 3 in binary is 1001 (base 2)
        self.assertEqual(decimal_To_Binary(16), 1000000) # 8 in binary is 100000 (base 2)
        self.assertEqual(decimal_To_Binary(15), 11111) # 7 in binary is 11111 (base 2)
        
if __name__ == '__main__':
    unittest.main()