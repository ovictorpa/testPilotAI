from decimal_To_Binary import *
import unittest  # import the unit test module

class TestDecimalToBinary(unittest.TestCase):  # create a class for testing functions
    def setUp(self):
        self.decimal_to_binary = decimal_To_Binary  # assign function to variable for easy access

    
    def test_positive_integer(self):
        self.assertEqual(self.decimal_to_binary(56), "1111100")   # Test case 1. 

    def test_zero(self):
        self.assertEqual(self.decimal_to_binary(0), "0" or None)   # Test case 2.

    def test_negative_number(self):
        self.assertRaises(ValueError, self.decimal_to_binary(-56))   # Test case 3.

    def test_float(self):
        self.assertRaises(TypeError, self.decimal_to_binary(12.5))   # Test case 4.

    def test_large_positive_integer(self):
        self.assertEqual(self.decimal_to_binary(10**200), "1"+"0"*(99) + "1")   # Test case 7.

    def test_small_positive_number(self):
        self.assertRaises(ValueError, self.decimal_to_binary(0.001))   # Test case 8.

    def test_large_negative_integer(self):
        self.assertEqual(self.decimal_to_binary(-1*10**200), None)   # Test case 9.

    def test_invalid_input(self):
        self.assertRaises(ValueError, self.decimal_to_binary("Hello"))   # Test case 6.

# Run the tests and output the result