from remove_multiple_spaces import *
import unittest
import re

def remove_multiple_spaces(text1):
    return re.sub(r'\s+', ' ', text1)

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_remove_single_space(self):
        self.assertEqual(remove_multiple_spaces("Hello World"), "Hello World")

    def test_remove_multiple_consecutive_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello  !     World"), "Hello! World")

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces("  Hello World  "), "Hello World")

    def test_preserve_single_space_in_word(self):
        self.assertEqual(remove_multiple_spaces("This is a test with   two spaces here."),
                             "This is a test with  two spaces here.")

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_newlines(self):
        self.assertEqual(remove_multiple_spaces("\nHello\nWorld"), "Hello World")

    def test_tab_spaces(self):
        self.assertEqual(remove_multiple_spaces("\tHello\tWorld"), "Hello World")

    def test_non_breaking_space(self):
        self.assertEqual(remove_multiple_spaces("Hello World\u00A0"), "Hello World")

    def test_with_special_characters(self):
        self.assertEqual(remove_multiple_spaces("Hello!World???!"), "Hello!World??!")

    def test_with_punctuation(self):
        self.assertEqual(remove_multiple_spaces("Hello, World; Another test."),
                             "Hello, World; Another test.")

    def test_with_non_printable_characters(self):
        self.assertEqual(remove_multiple_spaces("Hello\x01World"), "HelloWorld")

    def test_with_empty_lines(self):
        self.assertEqual(remove_multiple_spaces("\n\nHello World\n\n"), "Hello World")

    def test_mixed_whitespaces(self):
        self.assertEqual(remove_multiple_spaces("Hello \tWorld!"), "Hello World!")

    # Additional test cases can be added to cover more scenarios, such as:
    # - Handling of tabs (which are often equivalent to one or more spaces)
    # - Emoji or other Unicode characters that might act like whitespace
    # - Edge cases with very long strings where performance might become an issue

if __name__ == '__main__':
    unittest.main()