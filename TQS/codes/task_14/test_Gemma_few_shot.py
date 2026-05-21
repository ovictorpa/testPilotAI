from filter_by_prefix import *
import unittest

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_prefix_match(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_prefix_mismatch(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b'), ['bcd'])

    def test_prefix_in_capital(self):
        self.assertEqual(filter_by_prefix(['ABC', 'bcd', 'cde', 'ARRAY'], 'A'), ['ABC', 'ARRAY'])

    def test_prefix_with_special_chars(self):
        self.assertEqual(filter_by_prefix(['abc!@#$%^', 'bcd', 'cde', 'array'], '!'), ['abc!@#$%^'])


if __name__ == '__main__':
    unittest.main()