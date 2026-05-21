import unittest
from typing import List

from filter_by_prefix import filter_by_prefix  # Replace 'your_module' with the actual module where the function is defined.

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_all_strings_start_with_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_some_strings_start_with_prefix(self):
        self.assertEqual(filter_by_prefix(['apple pie', 'Apple pie', 'Baked apple pie', 'array'], 'apple'),
                             ['apple pie', 'Apple pie'])

    def test_no_strings_start_with_prefix(self):
        self.assertEqual(filter_by_prefix(['orange', 'banana', 'grape'], 'apple'), [])

    def test_empty_string_in_list(self):
        self.assertEqual(filter_by_prefix(['', 'hello', 'world'], 'h'), ['hello'])

    def test_case_sensitive_match(self):
        self.assertEqual(filter_by_prefix(['Hello', 'hello', 'WORLD'], 'H'), ['Hello', 'hello'])

    def test_whitespace_handling(self):
        self.assertEqual(filter_by_prefix(['  apple  pie', 'Apple pie', 'Baked apple pie'], 'apple'),
                             ['  apple  pie', 'Apple pie'])

    def test_null_prefix(self):
        self.assertEqual(filter_by_prefix(['a', 'b', 'c'], None), [])

    def test_non_string_inputs(self):
        with self.assertRaises(TypeError):
            filter_by_prefix([1, 2, 3], 'a')
        with self.assertRaises(TypeError):
            filter_by_prefix(['a', 'b', 'c'], 1)

    def test_non_string_list_elements(self):
        self.assertEqual(filter_by_prefix([1, 'apple', 3], 'apple'), ['apple'])

    def test_mixed_case_match(self):
        self.assertEqual(filter_by_prefix(['fOO', 'FOObar', 'foo', 'Bar'], 'Foo'), ['fOO', 'foo'])

if __name__ == '__main__':
    unittest.main()