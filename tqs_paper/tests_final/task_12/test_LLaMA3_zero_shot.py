import unittest
from longest import longest  # Import the function to be tested


class TestLongestFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings_same_length(self):
        self.assertEqual(longest(['abc', 'def', 'ghi']), 'abc')

    def test_multiple_strings_different_lengths(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_strings_with_duplicates(self):
        self.assertEqual(longest(['aa', 'ab', 'aba']), 'aba')

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            longest([None, 'a', 'b'])

if __name__ == '__main__':
    unittest.main()