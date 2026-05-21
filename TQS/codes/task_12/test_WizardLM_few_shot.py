import unittest
from typing import List, Optional

from longest import longest  # Replace 'your_module' with the actual module name where the longest function is defined

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        """Test that longest returns None for an empty list."""
        self.assertEqual(longest([]), None)

    def test_single_element_list(self):
        """Test that longest returns the single element string for a list with one element."""
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_list(self):
        """Test that longest returns the longest string from a list with multiple elements."""
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_same_length_strings(self):
        """Test that longest returns the first longest string when there are strings of the same maximum length."""
        self.assertEqual(longest(['abc', 'abcd', 'bc']), 'abc')

    def test_all_strings_of_equal_length(self):
        """Test that longest returns the first string when all strings in the list are of equal length."""
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_mixed_length_strings(self):
        """Test that longest returns the correct longest string from a list with mixed length strings."""
        self.assertEqual(longest(['hello', 'h', 'hi', 'world']), 'hello')

    def test_with_none_element(self):
        """Test that longest handles None elements in the list correctly."""
        self.assertEqual(longest(['a', None, 'c']), 'a')  # Assuming 'a' is longer than 'c' and ignores None

    def test_with_empty_strings(self):
        """Test that longest handles empty strings in the list correctly."""
        self.assertEqual(longest(['', 'a', 'b']), 'a')  # Assuming 'a' is longer than 'b' and an empty string is not considered

    def test_case_sensitivity(self):
        """Test that longest is case-sensitive."""
        self.assertEqual(longest(['Hello', 'hello', 'world']), 'Hello')

    def test_large_string(self):
        """Test that longest correctly identifies the largest string, even if it's not the first one."""
        self.assertEqual(longest(['small', 'veryverylongstring', 'short']), 'veryverylongstring')

if __name__ == '__main__':
    unittest.main()