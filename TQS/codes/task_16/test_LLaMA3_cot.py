from remove_Occ import *
import unittest

class TestRemoveOccFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_Occ("","a"), "")

    def test_single_character_removed(self):
        self.assertEqual(remove_Occ("abc","b"), "ac")

    def test_multiple_characters_removed_from_beginning(self):
        self.assertEqual(remove_Occ("abca","b"), "ac")

    def test_multiple_characters_removed_from_end(self):
        self.assertEqual(remove_Occ("abc","a"), "bc")

    def test_multiple_characters_removed_from_both_ends(self):
        self.assertEqual(remove_Occ("abca","b"), "c")

    def test_duplicate_characters(self):
        self.assertEqual(remove_Occ("aaab","a"), "")

    def test_leading_space(self):
        self.assertEqual(remove_Occ(" a ab a ","a"), " ab ")

    def test_trailing_space(self):
        self.assertEqual(remove_Occ("abc","b"), "bc")

    def test_no_characters_to_remove(self):
        self.assertEqual(remove_Occ("abca","c"), "abca")

if __name__ == '__main__':
    unittest.main()