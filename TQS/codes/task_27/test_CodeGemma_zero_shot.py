from remove_multiple_spaces import *
import unittest
import re

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_single_space(self):
        text = "This is a string with a single space."
        expected = "This is a string with a single space."
        result = remove_multiple_spaces(text)
        self.assertEqual(result, expected)

    def test_multiple_spaces(self):
        text = "This   is   a string with multiple spaces."
        expected = "This is a string with multiple spaces."
        result = remove_multiple_spaces(text)
        self.assertEqual(result, expected)

    def test_leading_trailing_spaces(self):
        text = "   This is a string with leading and trailing spaces.   "
        expected = "This is a string with leading and trailing spaces."
        result = remove_multiple_spaces(text)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()