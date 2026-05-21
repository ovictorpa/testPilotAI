from filter_by_substring import *
from typing import List

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_non_matching_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'), [])

    def test_matching_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])