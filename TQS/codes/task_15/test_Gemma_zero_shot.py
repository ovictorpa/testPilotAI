from filter_by_substring import *
import unittest

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_no_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'), [])

    def test_substring_present(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])


if __name__ == '__main__':
    unittest.main()