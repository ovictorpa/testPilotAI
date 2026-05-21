from remove_Occ import *
import unittest

def remove_Occ(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            s = s[:i] + s[i+1:]
            break
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ch:
            s = s[:i] + s[i+1:]
            break
    return s

class TestRemoveOcc(unittest.TestCase):
    def test_remove_single_occurrence(self):
        self.assertEqual(remove_Occ("hello", 'o'), "heli")

    def test_remove_multiple_occurrences(self):
        self.assertEqual(remove_Occ("worldwide", 'w'), "orldide")

    def test_remove_from_start(self):
        self.assertEqual(remove_Occ("occurrence", 'c'), "ourrance")

    def test_remove_from_middle(self):
        self.assertEqual(remove_Occ("banana", 'n'), "baaana")

    def test_remove_from_end(self):
        self.assertEqual(remove_Occ("goodbye", 'e'), "goodby")

    def test_remove_last_occurrence(self):
        self.assertEqual(remove_Occ("racecar", 'c'), "racera")

    def test_remove_all_occurrences_from_a_long_string(self):
        self.assertEqual(remove_Occ("This is a test string with several occurrences of the letter t", 't'), "This is a est string with several occurrences of the letter")

    def test_remove_character_not_present(self):
        self.assertEqual(remove_Occ("example", 'x'), "example")

    def test_remove_from_empty_string(self):
        self.assertEqual(remove_Occ("", 'a'), "")

    def test_remove_first_character(self):
        self.assertEqual(remove_Occ("a", 'a'), "")

    def test_remove_last_character(self):
        self.assertEqual(remove_Occ("b", 'b'), "")

    def test_case_sensitivity(self):
        self.assertNotEqual(remove_Occ("HelloWorld", 'w'), "HeilloWorld")
        self.assertEqual(remove_Occ("helloWorld", 'W'), "hellod")

    def test_remove_from_string_with_leading_trailing_spaces(self):
        self.assertEqual(remove_Occ("  remove this space  ", ' '), "remove this m")

# To run the tests, use the following command in your terminal:
# python -m unittest test_remove_occ