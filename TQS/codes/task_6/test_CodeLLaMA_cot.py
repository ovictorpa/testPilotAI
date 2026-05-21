from string_xor import *
import unittest

class TestStringXOR(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_single_character_strings(self):
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')
        self.assertEqual(string_xor('0', '0'), '0')

    def test_multiple_character_strings(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '111'), '010')
        self.assertEqual(string_xor('111', '100'), '011')

    def test_unequal_length_strings(self):
        with self.assertRaises(ValueError):
            string_xor('010', '11')

    def test_non_binary_strings(self):
        with self.assertRaises(ValueError):
            string_xor('abc', 'def')