from remove_Occ import *
import unittest

class TestRemoveOcc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_Occ('', 'a'), '')

    def test_single_char(self):
        self.assertEqual(remove_Occ('aaabbcc', 'b'), 'aacc')

    def test_multiple_chars(self):
        self.assertEqual(remove_Occ('abcabcdeeeefg', 'c'), 'abdeeefg')

    def test_char_not_in_string(self):
        self.assertEqual(remove_Occ('abcabcde', 'z'), 'abcabcde')


if __name__ == '__main__':
    unittest.main()