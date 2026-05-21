from filter_by_substring import *
import unittest

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        # Test that an empty list returns an empty list.
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_no_matching_strings(self):
        # Verify that a non-empty list with no matching strings returns an empty list.
        self.assertEqual(
            filter_by_substring(['abc', 'bacd', 'cde'], 'x'),
            []
        )

    def test_single_element_list(self):
        # Check that a single-element list is included or excluded based on the substring presence.
        self.assertIn('abc' if 'a' in 'abc' else 'bacd' if 'a' in 'bacd' else None,
                      filter_by_substring(['abc', 'bacd'], 'a'))
        self.assertNotIn('cde', filter_by_substring(['abc', 'bacd'], 'a'))

    def test_multiple_elements(self):
        # Test various scenarios with multiple strings, some containing the substring.
        result = filter_by_substring(['abc', 'bacd', 'array'], 'a')
        expected_result = ['abc', 'bacd', 'array']
        self.assertEqual(result, expected_result)

        result = filter_by_substring(['abc', 'bacd', 'cde'], 'b')
        expected_result = ['bacd']
        self.assertEqual(result, expected_result)

    def test_duplicate_substrings(self):
        # Verify that duplicate occurrences of the substring within the same string
        # result in only one occurrence being included in the output.
        result = filter_by_substring(['abc', 'abca', 'bacd'], 'a')
        expected_result = ['abca', 'abc']
        self.assertEqual(result, expected_result)

    def test_null_substring(self):
        # Ensure that null or empty substring is handled correctly.
        with self.assertRaises(TypeError):
            filter_by_substring(['abc', 'bacd'], None)

if __name__ == '__main__':
    unittest.main()