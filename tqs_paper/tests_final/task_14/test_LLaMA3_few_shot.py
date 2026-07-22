import unittest
from io import StringIO
from filter_by_prefix import filter_by_prefix  # Replace 'your_module' with the actual name of the module containing the function.

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], "a"), [])

    def test_no_matches(self):
        self.assertEqual(filter_by_prefix(["hello", "world"], "z"), [])

    def test_partial_match(self):
        self.assertEqual(filter_by_prefix(["abc", "bcd", "cde"], "ab"), ["abc"])

    def test_exact_match(self):
        self.assertEqual(filter_by_prefix(["abc", "bcd", "cde"], "a"), ["abc"])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()