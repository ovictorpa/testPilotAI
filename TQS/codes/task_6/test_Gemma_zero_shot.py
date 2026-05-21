from string_xor import *
import unittest

class TestStringXor(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_xor_of_equal_strings(self):
        self.assertEqual(string_xor('010', '010'), '000')

    def test_xor_of_different_strings(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_strings_with_longer_length(self):
        self.assertEqual(string_xor('0101', '1101'), '1010')


if __name__ == '__main__':
    unittest.main()