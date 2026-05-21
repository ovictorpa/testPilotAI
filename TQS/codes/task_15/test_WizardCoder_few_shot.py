from filter_by_substring import *
import unittest
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings, returning only those that contain the given substring.

    >>> filter_by_substring([], 'a')
    []

    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'
    ['abc', 'bacd']

    >>> filter_by_substring(['foo', 'bar', 'baz', 'foobar'], 'o')
    ['foo', 'bar', 'foobar']
    
    >>> filter_by_substring(['hello world', 'python', 'programming', 'code'], 'pr')
    ['programming']

    """

    return [x for x in strings if substring in x]

class TestFilterBySubstring(unittest.TestCase):
    def test_filter_by_substring_empty(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_filter_by_substring_non_matching(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], 'z'), [])

    def test_filter_by_substring_single_match(self):
        self.assertEqual(filter_by_substring(['foo', 'bar', 'baz'], 'o'), ['foo'])

    def test_filter_by_substring_multiple_matches(self):
        self.assertEqual(filter_by_substring(['hello world', 'python', 'programming', 'code'], 'pr'), ['programming'])

    def test_filter_by_substring_no_match(self):
        self.assertEqual(filter_by_substring(['foo', 'bar', 'baz'], 'z'), [])