from string_xor import *
import unittest

class TestStringXor(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_non_binary_characters(self):
        self.assertRaises(ValueError, string_xor('a', 'b'))

    def test_different_lengths(self):
        self.assertRaises(ValueError, string_xor('01', '10'))

    def test_xor_identical_strings(self):
        self.assertEqual(string_xor('010', '010'), '000')

    def test_xor_different_strings(self):
        self.assertEqual(string_xor('010', '110'), '100')


if __name__ == '__main__':
    unittest.main()