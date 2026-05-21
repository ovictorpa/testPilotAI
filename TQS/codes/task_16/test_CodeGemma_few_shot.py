from remove_Occ import *
import unittest

class TestRemoveOcc(unittest.TestCase):

    def test_remove_first_occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

    def test_remove_last_occ(self):
        self.assertEqual(remove_Occ("hello", "o"), "hell")

    def test_remove_middle_occ(self):
        self.assertEqual(remove_Occ("hello", "e"), "hllo")

    def test_empty_string(self):
        self.assertEqual(remove_Occ("", "l"), "")

    def test_single_character(self):
        self.assertEqual(remove_Occ("a", "a"), "")

if __name__ == '__main__':
    unittest.main()