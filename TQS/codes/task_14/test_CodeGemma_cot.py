from filter_by_prefix import *
import unittest

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:

    """

    Filter an input list of strings to include only those that start with the given prefix.

    """

    return [x for x in strings if x.startswith(prefix)]


class TestFilterByPrefix(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_non_empty_input(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_prefix_not_found(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'x'), [])

    def test_prefix_is_empty(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], ''), ['abc', 'bcd', 'cde'])


if __name__ == '__main__':
    unittest.main()