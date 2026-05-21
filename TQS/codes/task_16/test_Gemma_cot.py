from remove_Occ import *
import unittest

class TestRemoveOcc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_Occ('', 'a'), '')

    def test_single_character(self):
        self.assertEqual(remove_Occ('a', 'a'), '')

    def test_multiple_occ_front(self):
        self.assertEqual(remove_Occ('aaabbcc', 'b'), 'cc')

    def test_multiple_occ_back(self):
        self.assertEqual(remove_Occ('abcabcdeee', 'e'), 'abcabcde')

    def test_char_not_in_string(self):
        self.assertEqual(remove_Occ('abcabcde', 'z'), 'abcabcde')


if __name__ == '__main__':
    unittest.main()