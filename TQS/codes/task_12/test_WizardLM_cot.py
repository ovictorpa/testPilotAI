import unittest
from typing import List, Optional
from longest import longest  # Replace 'your_module' with the actual module name where the longest function is defined

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_strings_of_same_max_length(self):
        self.assertEqual(longest(['a', 'ab', 'abc', 'abcd']), 'abcd')

    def test_all_strings_of_equal_non_max_length(self):
        self.assertIsNone(longest(['a', 'b', 'c', 'd'])), "The result should be None since 'a', 'b', 'c', and 'd' all have the same length which is not the longest."

    def test_non_string_elements(self):
        self.assertEqual(longest(['a', 123, 'c']), 'a')

    def test_strings_with_leading_trailing_whitespaces(self):
        self.assertEqual(longest(['  a  ', 'bb', 'ccc']), 'ccc')

    def test_unicode_strings(self):
        self.assertEqual(longest(['a', 'balle', 'football'])], 'football')

    def test_empty_strings(self):
        self.assertEqual(longest(['', 'a', 'bb']), 'a')

    def test_mixed_string_lengths(self):
        self.assertEqual(longest(['abc', 'a', 'ab', 'abcd', 'aabbcc']), 'aabbcc')

if __name__ == '__main__':
    unittest.main()