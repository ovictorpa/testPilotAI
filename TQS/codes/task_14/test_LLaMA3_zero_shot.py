import unittest
from filter_by_prefix import filter_by_prefix  # replace 'your_module' with the actual name of the module containing the function

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'x'), [])

    def test_partial_match(self):
        self.assertEqual(filter_by_prefix(['abc', 'array'], 'a'), ['abc', 'array'])

    def test_full_match(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana'], 'app'), ['apple'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_prefix(['hello', 'world', 'python'], 'he'), ['hello', 'hello'])

if __name__ == '__main__':
    unittest.main()