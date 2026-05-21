from remove_Occ import *
import unittest

class TestRemoveOcc(unittest.TestCase):

    def test_remove_first_occ(self):
        self.assertEqual(remove_Occ("hello", "h"), "ello")

    def test_remove_last_occ(self):
        self.assertEqual(remove_Occ("hello", "o"), "hell")

    def test_remove_middle_occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

    def test_remove_non_existent_occ(self):
        self.assertEqual(remove_Occ("hello", "z"), "hello")

    def test_empty_string(self):
        self.assertEqual(remove_Occ("", "h"), "")

    def test_single_character_string(self):
        self.assertEqual(remove_Occ("h", "h"), "")

if __name__ == "__main__":
    unittest.main()