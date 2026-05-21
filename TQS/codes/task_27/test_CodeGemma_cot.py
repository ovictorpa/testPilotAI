from remove_multiple_spaces import *
import unittest
import re

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_normal_case(self):
        text1 = "This is a string with multiple spaces."
        expected_output = "This is a string with multiple spaces."
        self.assertEqual(remove_multiple_spaces(text1), expected_output)

    def test_empty_string(self):
        text1 = ""
        expected_output = ""
        self.assertEqual(remove_multiple_spaces(text1), expected_output)

    def test_single_space(self):
        text1 = "This is a string with single spaces."
        expected_output = "This is a string with single spaces."
        self.assertEqual(remove_multiple_spaces(text1), expected_output)

    def test_multiple_leading_spaces(self):
        text1 = "    This is a string with multiple spaces."
        expected_output = "This is a string with multiple spaces."
        self.assertEqual(remove_multiple_spaces(text1), expected_output)

    def test_multiple_trailing_spaces(self):
        text1 = "This is a string with multiple spaces.    "
        expected_output = "This is a string with multiple spaces."
        self.assertEqual(remove_multiple_spaces(text1), expected_output)

    def test_multiple_leading_trailing_spaces(self):
        text1 = "    This is a string with multiple spaces.    "
        expected_output = "This is a string with multiple spaces."
        self.assertEqual(remove_multiple_spaces(text1), expected_output)

if __name__ == "__main__":
    unittest.main()