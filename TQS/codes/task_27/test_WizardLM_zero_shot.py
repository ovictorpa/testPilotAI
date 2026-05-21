from remove_multiple_spaces import *
import unittest
import re

def remove_multiple_spaces(text1):
    return re.sub(' +', ' ', text1)

# Unit tests for the remove_multiple_spaces function
class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_single_space(self):
        """Single space should remain unchanged."""
        self.assertEqual(remove_multiple_spaces("Hello "), "Hello ")

    def test_leading_multiple_spaces(self):
        """Leading multiple spaces should be reduced to a single space."""
        self.assertEqual(remove_multiple_spaces("   Hello"), " Hello")

    def test_trailing_multiple_spaces(self):
        """Trailing multiple spaces should be reduced to a single space."""
        self.assertEqual(remove_multiple_spaces("Hello   "), "Hello ")

    def test_multiple_spaces_in_middle(self):
        """Multiple spaces in the middle of the text should be reduced to a single space."""
        self.assertEqual(remove_multiple_spaces("Hell o  w orld"), "Hello world")

    def test_only_single_space(self):
        """Text with only single spaces should remain unchanged."""
        self.assertEqual(remove_multiple_spaces("Hello   World   "), "Hello   World   ")

    def test_empty_string(self):
        """Empty string should remain empty."""
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_newlines(self):
        """Newlines with multiple spaces around should preserve newlines and reduce spaces."""
        text = ("This is a line.\n"
                " This is another line.")
        expected = ("This is a line.\n"
                     " This is another line.")
        self.assertEqual(remove_multiple_spaces(text), expected)

    def test_mixed_spaces_and_tabs(self):
        """Mixed spaces and tabs should be reduced to single spaces."""
        text = ("This\tis a\n\tline with\t  multiple\tspaces.")
        expected = ("This is a line with multiple spaces.")
        self.assertEqual(remove_multiple_spaces(text), expected)

    def test_no_extra_spaces_after_replacement(self):
        """No extra spaces should be added after replacement."""
        text = "Hello     World"
        expected = "Hello World"
        self.assertEqual(remove_multiple_spaces(text), expected)

    def test_non_breaking_spaces(self):
        """Non-breaking spaces (U+00A0) should be considered as single spaces."""
        text = ("Helloï¿½  Hello")
        expected = ("Helloï¿½Hello")
        self.assertEqual(remove_multiple_spaces(text), expected)

    def test_other_whitespace(self):
        """Other whitespace characters (like tabs) should not be affected."""
        text = ("Hello\tWorld")
        expected = ("Hello\tWorld")
        self.assertEqual(remove_multiple_spaces(text), expected)

if __name__ == '__main__':
    unittest.main()