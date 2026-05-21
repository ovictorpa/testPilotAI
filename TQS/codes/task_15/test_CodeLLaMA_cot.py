from filter_by_substring import *
import unittest
from typing import List

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_non_empty_list_with_matching_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_non_empty_list_without_matching_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'), [])

if __name__ == '__main__':
    unittest.main()