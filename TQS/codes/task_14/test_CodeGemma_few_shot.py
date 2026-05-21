from filter_by_prefix import *
import unittest

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_prefix_match(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'a'), [])

    def test_single_prefix_match(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_multiple_prefix_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array', 'apple'], 'a'), ['abc', 'array', 'apple'])

if __name__ == '__main__':
    unittest.main()