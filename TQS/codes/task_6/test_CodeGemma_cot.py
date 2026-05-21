from string_xor import *
import unittest

class TestStringXor(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_different_lengths(self):
        self.assertEqual(string_xor('101', '10'), '101')

    def test_equal_lengths(self):
        self.assertEqual(string_xor('101', '101'), '000')

    def test_only_ones(self):
        self.assertEqual(string_xor('111', '111'), '000')

    def test_only_zeros(self):
        self.assertEqual(string_xor('000', '000'), '000')

    def test_random_strings(self):
        self.assertEqual(string_xor('10101', '11010'), '01111')

if __name__ == '__main__':
    unittest.main()