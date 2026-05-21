import unittest
from string_xor import string_xor  # Import the function to be tested

class TestStringXOR(unittest.TestCase):

    def test_xor_two_equal_strings(self):
        self.assertEqual(string_xor('010', '110'), '')

    def test_xor_two_unequal_strings(self):
        self.assertEqual(string_xor('010', '111'), '100')

    def test_xor_empty_string_first(self):
        self.assertEqual(string_xor('', '101'), '0')

    def test_xor_empty_string_second(self):
        self.assertEqual(string_xor('0101', ''), '01')

    def test_xor_non_binary_strings(self):
        with self.assertRaises(ValueError):
            string_xor('abc', '110')

    def test_xor_non_same_length_strings(self):
        with self.assertRaises(ValueError):
            string_xor('010', '1010')

    def test_xor_large_input(self):
        large_string = 'a' * 1000
        large_other_string = 'b' * 1000

        result = string_xor(large_string, large_other_string)
        self.assertEqual(len(result), 1000)

if __name__ == '__main__':
    unittest.main()