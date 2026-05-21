import unittest
from filter_by_substring import filter_by_substring  # replace 'your_module' with the actual name of the module containing the function

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_no_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], 'x'), [])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_single_match(self):
        self.assertEqual(filter_by_substring(['hello world'], 'world'), ['hello world'])

    def test_case_insensitivity(self):
        self.assertEqual(filter_by_substring(['ABC', 'bacD', 'array'], 'A'), ['ABC', 'array'])

    def test_substring_at_end(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], 'd'), ['cde'])

if __name__ == '__main__':
    unittest.main()