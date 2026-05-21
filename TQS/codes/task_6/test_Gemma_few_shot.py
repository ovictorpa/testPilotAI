from string_xor import *
import unittest

class TestStringXor(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_strings_of_different_lengths(self):
        self.assertRaises(ValueError, string_xor('01', '10'))

    def test_basic_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_xor_of_equal_strings(self):
        self.assertEqual(string_xor('000', '000'), '000')

    def test_xor_of_strings_with_ones_and_zeros(self):
        self.assertEqual(string_xor('111', '000'), '111')


if __name__ == '__main__':
    unittest.main()