from longest import *
from typing import List, Optional
from unittest.TestCase import TestCase
import unittest

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    
    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

# Unit tests
class TestLongestFunction(TestCase):
    def test_empty_list(self):
        self.assertEqual(longest([]), None)

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings_of_different_lengths(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_strings_with_equal_maximum_length(self):
        self.assertEqual(longest(['hello', 'world', 'hola', 'salut']), 'hello')

    def test_all_strings_of_same_length(self):
        self.assertEqual(longest(['abc', 'abcd', 'abcde']), 'abcde')

    def test_empty_string_in_list(self):
        self.assertEqual(longest(['a', '', 'c']), 'a')

    def test_all_strings_empty(self):
        self.assertEqual(longest(['', '', '']), None)

    def test_none_type_input(self):
        self.assertIsNone(longest(None))

    def test_non_string_elements_in_list(self):
        self.assertEqual(longest(['a', 123, 'c']), 'a')

# Run the tests
if __name__ == '__main__':
    unittest.main()