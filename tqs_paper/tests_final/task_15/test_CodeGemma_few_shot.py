from filter_by_substring import *
import unittest

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_substring_present(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_substring_not_present(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], 'b'), ['abc', 'bacd'])

    def test_empty_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], ''), ['abc', 'bacd', 'cde'])

    def test_whitespace_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], ' '), [])

if __name__ == '__main__':
    unittest.main()