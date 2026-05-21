from TQS.tests_final.task_6.string_xor import *
import unittest

class TestStringXor(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(string_xor("", ""), "")

    def test_equal_strings(self):
        self.assertEqual(string_xor("010", "010"), "000")

    def test_different_strings(self):
        self.assertEqual(string_xor("010", "110"), "100")

    def test_strings_different_lengths(self):
        self.assertEqual(string_xor("010", "1100"), "100")

if __name__ == '__main__':
    unittest.main()