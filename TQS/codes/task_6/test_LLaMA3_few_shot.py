import unittest
from string_xor import string_xor  # replace 'your_module' with the actual name of the module containing the function

class TestStringXOR(unittest.TestCase):

    def test_equal_strings(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_different_length_strings(self):
        with self.assertRaises(ValueError):
            string_xor('010', '1101')

    def test_mismatched_characters(self):
        with self.assertRaises(ValueError):
            string_xor('01', '10')

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_single_character_strings(self):
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')

if __name__ == '__main__':
    unittest.main()