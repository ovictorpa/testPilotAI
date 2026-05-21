import unittest
from longest import longest  # Import the function from your module

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_with_same_length(self):
        self.assertEqual(longest(['abc', 'abcd']), 'abcd')

    def test_multiple_elements_with_different_lengths(self):
        self.assertEqual(longest(['abc', 'abcd', 'def']), 'abcd')

    def test_longest_string_at_beginning(self):
        self.assertEqual(longest(['ccc', 'bb', 'a']), 'ccc')

    def test_no_longest_string(self):
        self.assertIsNone(longest(['ab', 'cd']))

if __name__ == '__main__':
    unittest.main()