from filter_by_prefix import *
import unittest
from typing import List

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matching_strings(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'f'), [])

    def test_one_matching_string(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'a'), ['abc'])

    def test_multiple_matching_strings(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()