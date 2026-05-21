from string_xor import *
import unittest
from typing import AnyStr as str  # Python 3.10 and above

class TestStringXOR(unittest.TestCase):
    def test_equal_strings(self):
        self.assertEqual(string_xor('110', '110'), '0')

    def test_different_strings(self):
        self.assertEqual(string_xor('110', '001'), '110')

    def test_longer_string(self):
        self.assertEqual(string_xor('1101', '00110'), '1011')

    def test_different_lengths(self):
        with self.assertRaises(ValueError):
            string_xor('110', '1101')

    def test_non_binary_string(self):
        with self.assertRaises(ValueError):
            string_xor('210', '110')

if __name__ == "__main__":
    unittest.main()