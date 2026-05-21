from string_xor import *
import unittest
from typing import Tuple

def string_xor(a: str, b: str) -> str:
    """
    Perform a binary XOR operation on two strings consisting only of 1s and 0s.
    The result is returned as a string of 1s and 0s.
    
    Args:
        a (str): A string consisting only of 1s and 0s.
        b (str): A string consisting only of 1s and 0s.
    Returns:
        str: The result of XOR operation on the input strings as a binary string.
    
    Example:
        >>> string_xor('010', '110')
        '100'
    """

    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'
        
    return ''.join(xor(x, y) for x, y in zip(a, b))

class TestStringXOR(unittest.TestCase):
    def test_binary_inputs(self):
        self.assertEqual(string_xor('010', '110'), '100')  # Example case from the doc string
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            string_xor(3, 4)  # inputs must be strings
            
    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            string_xor('10', '1')  # input strings should have equal length
            
    def test_nonbinary_input(self):
        with self.assertRaises(TypeError):
            string_xor('123', '456')  # inputs must be binary strings
        
    def test_different_cases(self):
        self.assertEqual(string_xor('010', 'a1B'), '101')  # case-insensitive comparison
        
    def test_padding(self):
        self.assertEqual(string_xor('01', '1111'), '0011')  # padding with zeros to make the strings of equal length
        
if __name__ == "__main__":
    unittest.main()