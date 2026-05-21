from remove_multiple_spaces import *
import unittest

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces("Hello world"), "Hello world")

    def test_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello   world"), "Hello world")

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces("  Hello world  "), "Hello world")

    def test_special_characters(self):
        self.assertEqual(remove_multiple_spaces("Hello world!   "), "Hello world!")


if __name__ == '__main__':
    unittest.main()