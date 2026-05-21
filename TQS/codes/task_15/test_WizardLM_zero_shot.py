import unittest
from typing import List

from filter_by_substring import filter_by_substring  # Replace 'your_module' with the actual module name where the function is defined

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_no_substring_in_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde'], 'x'), [])

    def test_all_strings_contain_substring(self):
        self.assertEqual(filter_by_substring(['a', 'ab', 'abc'], 'bc'), ['a', 'ab', 'abc'])

    def test_some_strings_contain_substring(self):
        self.assertEqual(filter_by_substring(['apple', 'banana', 'apricot', 'cherry'], 'p'), ['apple', 'apricot'])

    def test_case_insensitive(self):
        self.assertEqual(filter_by_substring(['AbC', 'abc', 'aBc', 'Xyz'], 'bc'), ['AbC', 'abc', 'aBc'])

    def test_substring_at_start_of_string(self):
        self.assertEqual(filter_by_substring(['Hello', 'World', 'Hello there', 'Hi', 'Goodbye'], 'Hello'), ['Hello', 'Hello there'])

    def test_substring_in_middle_of_string(self):
        self.assertEqual(filter_by_substring(['HelloWorld', 'World', 'Hello there', 'Hi', 'Goodbye'], 'World'), ['HelloWorld', 'World'])

    def test_substring_at_end_of_string(self):
        self.assertEqual(filter_by_substring(['Hello', 'World', 'Hello there', 'Hi123', 'Goodbye'], '123'), ['Hi123'])

    def test_substring_partially_in_string(self):
        self.assertEqual(filter_by_substring(['HelloWorld', 'WorldIsFun', 'Hello there', 'Hi', 'Goodbye'], 'orld'), ['HelloWorld', 'WorldIsFun'])

    def test_whitespace_around_substring(self):
        self.assertEqual(filter_by_substring(['  Hello World  ', 'World', 'Hello there'], 'World'), ['  Hello World  '])

    def test_mixed_case_substring(self):
        self.assertEqual(filter_by_substring(['abcDE', 'aBcD', 'Abcde', 'XYZ'], 'bcDe'), ['abcDE', 'aBcD', 'Abcde'])

    def test_substring_with_special_characters(self):
        self.assertEqual(filter_by_substring(['test123', 'test!', 'test@gmail.com', 'test#'], 'test'), ['test123', 'test!', 'test@gmail.com'])

    def test_empty_string_in_list(self):
        self.assertEqual(filter_by_substring(['a', '', 'b'], 'a') ,['a', ''])

    def test_all_strings_empty(self):
        self.assertEqual(filter_by_substring(['', '', ''], 'a'), [''])

    def test_substring_with_non_alphabetic_characters(self):
        self.assertEqual(filter_by_substring(['Hello123', 'World!', 'Hello there#', 'Hi$', 'Goodbye&'], 'llo'), ['Hello123', 'Hello there#'])

if __name__ == '__main__':
    unittest.main()