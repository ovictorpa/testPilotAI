from remove_Occ import *
import unittest

class TestRemoveOcc(unittest.TestCase):

    def test_remove_single_character(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

    def test_remove_multiple_characters(self):
        self.assertEqual(remove_Occ("Mississippi", "i"), "Mssppss")

    def test_remove_nonexistent_character(self):
        self.assertEqual(remove_Occ("banana", "z"), "banana")

    def test_empty_string(self):
        self.assertEqual(remove_Occ("", "a"), "")

    def test_string_with_single_character(self):
        self.assertEqual(remove_Occ("a", "a"), "")

if __name__ == "__main__":
    unittest.main()