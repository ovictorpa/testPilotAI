from filter_by_prefix import *
import unittest
from typing import List

class TestFilterByPrefix(unittest.TestCase):

    def test_filter_by_prefix_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
    
    def test_filter_by_prefix_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])
    
    def test_filter_by_prefix_no_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['xyz', 'uvw', 'rstu'], 'a'), [])
    
    def test_filter_by_prefix_all_strings_match_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])
    
if __name__ == '__main__':
    unittest.main()