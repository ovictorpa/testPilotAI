import unittest
from decimal_To_Binary import decimal_To_Binary  # Assuming this is the name of the file where your function is defined

class TestDecimalToBinary(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(decimal_To_Binary(0), '0')  # The function should return '0' for input 0

    def test_positive_numbers(self):
        self.assertEqual(decimal_To_Binary(1), '1')
        self.assertEqual(decimal_To_Binary(2), '10')
        self.assertEqual(decimal_To_Binary(3), '11')
        self.assertEqual(decimal_To_Binary(4), '100')
        self.assertEqual(decimal_To_Binary(5), '101')
        self.assertEqual(decimal_To_Binary(8), '1000')  # And so on...

    def test_negative_numbers(self):
        self.assertEqual(decimal_To_Binary(-1), '1111111' )  # Two's complement for -1
        self.assertEqual(decimal_To_Binary(-2), '1111110' )
        self.assertEqual(decimal_To_Binary(-3), '1111101' )
        self.assertEqual(decimal_To_Binary(-4), '111100' )
        # And so on... For negative numbers, we use two's complement representation

    def test_large_positive_numbers(self):
        self.assertEqual(decimal_To_Binary(255), '1111111' )  # Max value for a single byte
        self.assertEqual(decimal_To_Binary(256), '1000000' )  # Overflow into bytes
        self.assertEqual(decimal_To_Binary(1023), '1111111 1111111' )  # Max value for a two-byte unsigned int
        # ... continue testing with larger numbers as needed

    def test_large_negative_numbers(self):
        self.assertEqual(decimal_To_Binary(-256), '11111111 1111111' )  # Two's complement for -256, into two bytes
        # ... continue testing with larger negative numbers as needed

    def test_non_integer_values(self):
        self.assertEqual(decimal_To_Binary(0.5), '0.100...' )  # This is a special case and might not be handled correctly by the current implementation
        self.assertEqual(decimal_To_Binary(-0.5), '1.111...111' )  # This is also a special case for two's complement

    def test_bitwise_operators(self):
        self.assertEqual(decimal_To_Binary(1 | 2), '1001')  # Bitwise OR example
        self.assertEqual(decimal_To_Binary(1 & 2), '0010')  # Bitwise AND example
        self.assertEqual(decimal_To_binary(1 ^ 2), '0101')  # Bitwise XOR example
        self.assertEqual(decimal_To_binary(~1), '11111111' )  # Bitwise NOT (ones complement)

    def test_edge_cases(self):
        self.assertEqual(decimal_To_Binary(1e308), '1000...000' )  # Max value for a 64-bit unsigned int
        self.assertRaises(OverflowError, decimal_To_Binary, (1e308 + 1))  # Should raise an OverflowError

    def test_empty_string(self):
        self.assertEqual(decimal_To_Binary(''), '0')  # An empty string should be treated as 0

# This allows the tests to be run from the command line with `python -m unittest your_test_file.py`
if __name__ == '__main__':
    unittest.main()