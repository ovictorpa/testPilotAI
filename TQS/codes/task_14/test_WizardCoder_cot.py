import unittest
from filter_by_prefix import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
    
    def test_nonexistent_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z'), [])
    
    def test_nonempty_list(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            filter_by_prefix('not a list', 'a')

if __name__ == "__main__":
    unittest.main()