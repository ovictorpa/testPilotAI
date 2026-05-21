from string_xor import *
import unittest

def string_xor(a: str, b: str) -> str:
    # ... (function implementation as provided)

class TestStringXor(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_one_empty_string(self):
        self.assertEqual(string_xor('01', ''), '01')
        self.assertEqual(string_xor('', '10'), '10')

    def test_strings_with_equal_lengths(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('1010', '1100'), '0110')

    def test_strings_with_different_lengths(self):
        # Pad the shorter string with its tail to match the length of the longer one
        self.assertEqual(string_xor('01', '110'), '100')
        self.assertEqual(string_xor('00101', '110011'), '101100')

    def test_all_zeros(self):
        self.assertEqual(string_xor('000', '000'), '000')

    def test_all_ones(self):
        self.assertEqual(string_xor('111', '111'), '000')

    def test_alternating_bits(self):
        self.assertEqual(string_xor('01011', '101101'), '001100')

    def test_strings_with_non_binary_values(self):
        # Test with invalid input to ensure the function handles only binary strings
        with self.assertRaises(ValueError):
            string_xor('01', 'abc')

    def test_strings_with_mixed_binary_and_non_binary_values(self):
        # Test with a mix of valid and invalid input to ensure the function fails gracefully
        with self.assertRaises(ValueError):
            string_xor('01abc', '10def')

    def test_strings_with_only_zeros(self):
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('00', '000'), '000')

    def test_strings_with_only_ones(self):
        self.assertEqual(string_xor('1', '1'), '1')
        self.assertEqual(string_xor('111', '1111'), '1111')

    def test_case_sensitivity(self):
        # Ensure that the function is not case-sensitive (even though it doesn't matter for binary strings)
        self.assertEqual(string_xor('A0B', 'a1b'), 'b0C')

# This allows the tests to be run as a script if needed
if __name__ == '__main__':
    unittest.main()