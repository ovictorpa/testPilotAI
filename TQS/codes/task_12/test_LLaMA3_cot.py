from longest import *
import unittest

class TestLongestFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual('a', longest(['a']))

    def test_multiple_strings(self):
        self.assertEqual('ccc', longest(['a', 'bb', 'ccc']))
        # Test that all longest strings are returned if there are multiple
        self.assertEqual({'a': 1, 'bb': 2, 'ccc': 3}, {s: len(s) for s in longest(['a', 'bb', 'ccc'])})

    def test_string_with_non_numeric_value(self):
        with self.assertRaises(TypeError):
            longest(['a', None, 'b'])

    # Additional tests based on specific requirements

if __name__ == '__main__':
    unittest.main()