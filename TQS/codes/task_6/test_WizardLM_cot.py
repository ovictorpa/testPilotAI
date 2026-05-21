from string_xor import *
import unittest

class TestStringXor(unittest.TestCase):
    def test_equal_length_even_ones(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_equal_length_odd_ones(self):
        self.assertEqual(string_xor('101', '110'), '011')

    def test_unequal_length_ends_with_zero(self):
        self.assertEqual(string_xor('010', '1100'), '1000')

    def test_unequal_length_ends_with_one(self):
        self.assertEqual(string_xor('0101', '110'), '0011')

    def test_all_zeros(self):
        self.assertEqual(string_xor('000', '000'), '000')

    def test_all_ones(self):
        self.assertEqual(string_xor('111', '111'), '000')

    def test_mixed_with_even_ones(self):
        self.assertEqual(string_xor('01010', '110010'), '100010')

    def test_mixed_with_odd_ones(self):
        self.assertEqual(string_xor('01011', '110011'), '001100')

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_single_character_strings(self):
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('1', '1'), '0')

    def test_mixed_with_one_longer(self):
        self.assertEqual(string_xor('01010', '110'), '100010')

    def test_mixed_with_other_one_longer(self):
        self.assertEqual(string_xor('0101011', '11011'), '00110011')

    def test_ones_have_different_parity(self):
        self.assertEqual(string_xor('1111', '1010'), '0101')

    def test_leading_zeros(self):
        self.assertEqual(string_xor('000001010', '11000010'), '10010000')

    def test_trailing_ones(self):
        self.assertEqual(string_xor('1010', '010000'), '1010000')

if __name__ == '__main__':
    unittest.main()