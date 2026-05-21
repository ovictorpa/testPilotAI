from string_xor import *
import unittest

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Strings must have the same length")

    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

class TestStringXOR(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_different_lengths(self):
        with self.assertRaises(ValueError):
            string_xor('101', '110')

    def test_identical_strings(self):
        self.assertEqual(string_xor('010', '010'), '000')
        self.assertEqual(string_xor('111', '111'), '000')
        self.assertEqual(string_xor('', ''), '')

    def test_only_ones(self):
        self.assertEqual(string_xor('111111', '111111'), '000000')

    def test_only_zeros(self):
        self.assertEqual(string_xor('000000', '000000'), '000000')

if __name__ == '__main__':
    unittest.main()