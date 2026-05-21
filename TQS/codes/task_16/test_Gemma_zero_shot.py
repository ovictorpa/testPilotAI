from remove_Occ import *
import unittest

class TestRemoveOcc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_Occ('', '*'), '')

    def test_single_char(self):
        self.assertEqual(remove_Occ('a', 'a'), '')

    def test_multiple_chars(self):
        self.assertEqual(remove_Occ('abca', 'c'), 'aba')

    def test_char_not_in_string(self):
        self.assertEqual(remove_Occ('abca', 'd'), 'abca')

    def test_string_with_multiple_chars(self):
        self.assertEqual(remove_Occ('abcaab', 'b'), 'caab')

if __name__ == '__main__':
    unittest.main()