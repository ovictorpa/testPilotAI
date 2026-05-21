from filter_by_substring import *
import unittest

from typing import List


class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        strings = []
        substring = 'a'
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, [])

    def test_single_match(self):
        strings = ['abc', 'bacd', 'cde', 'array']
        substring = 'a'
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, ['abc', 'bacd', 'array'])

    def test_no_match(self):
        strings = ['bcd', 'def', 'ghi']
        substring = 'a'
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, [])

    def test_case_sensitive(self):
        strings = ['abc', 'bacd', 'cde', 'array']
        substring = 'A'
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()