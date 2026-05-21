from filter_by_prefix import *
import unittest
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'x'), ['x'])

    def test_multiple_strings_with_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_partial_match_with_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap'), ['apple', 'apricot'])

    def test_case_insensitive_match(self):
        self.assertListEqual(filter_by_prefix(['Apple', 'orange', 'APPLE', 'Banana'], 'a'), ['Apple', 'orange'])

    def test_all_strings_have_prefix(self):
        self.assertEqual(filter_by_prefix(['alpha', 'beta', 'gamma'], 'al'), ['alpha', 'beta', 'gamma'])

if __name__ == '__main__':
    unittest.main()