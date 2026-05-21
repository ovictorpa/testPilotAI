from filter_by_substring import *
import unittest

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


class TestFilterBySubstring(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_no_match(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], 'z'), [])

    def test_single_match(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], 'a'), ['abc', 'bacd'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_substring_in_middle(self):
        self.assertEqual(filter_by_substring(['hello', 'world', 'python'], 'or'), ['world'])

    def test_substring_in_beginning(self):
        self.assertEqual(filter_by_substring(['array', 'list', 'tuple'], 'ar'), ['array'])

    def test_substring_in_end(self):
        self.assertEqual(filter_by_substring(['hello', 'world', 'python'], 'on'), ['python'])


if __name__ == '__main__':
    unittest.main()