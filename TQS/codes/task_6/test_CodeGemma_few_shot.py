from string_xor import *
import unittest

class TestStringXor(unittest.TestCase):

    def test_equal_strings(self):
        self.assertEqual(string_xor('010', '010'), '000')

    def test_different_strings(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_strings_of_different_lengths(self):
        self.assertEqual(string_xor('010', '11'), '10')

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_strings_with_non_binary_characters(self):
        with self.assertRaises(ValueError):
            string_xor('a', 'b')