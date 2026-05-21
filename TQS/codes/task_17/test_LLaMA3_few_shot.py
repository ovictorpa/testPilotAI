from decimal_To_Binary import *
import unittest

def decimal_To_Binary(N):
    # Your existing implementation here...
    B_Number = 0
    cnt = 0
    while (N != 0): 
        rem = N % 2
        c = pow(10,cnt)  
        B_Number += rem*c  
        N //= 2 
        cnt += 1
    return B_Number

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary_zero(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_decimal_to_binary_one(self):
        self.assertEqual(decimal_To_Binary(1), 1)

    def test_decimal_to_binary_multiple_of_two(self):
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(4), 100)
        self.assertEqual(decimal_To_Binary(8), 1000)

    def test_decimal_to_binary_not_multiple_of_two(self):
        self.assertEqual(decimal_To_Binary(3), 11)
        self.assertEqual(decimal_To_Binary(5), 101)

    def test_decimal_to_binary_large_number(self):
        self.assertEqual(decimal_To_Binary(10), 1010)
        self.assertEqual(decimal_To_Binary(20), 10100)

if __name__ == '__main__':
    unittest.main()