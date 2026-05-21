import unittest
from filter_by_substring import filter_by_substring  # Replace 'your_module' with the actual name of the module containing the function


class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_no_matches(self):
        strings = ['abc', 'bacd', 'cde']
        substring = 'xyz'
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, [])

    def test_single_match(self):
        strings = ['abc', 'bacd', 'cde']
        substring = 'a'
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, ['abc'])

    def test_multiple_matches(self):
        strings = ['abc', 'bacd', 'cde', 'array']
        substring = 'a'
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, ['abc', 'bacd', 'array'])

    def test_case_insensitivity(self):
        strings = ['AbC', 'BaCd', 'CDe']
        substring = 'A'
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, ['AbC', 'BaCd', 'CDe'])

    def test_empty_substring(self):
        strings = ['abc', 'bacd', 'cde']
        substring = ''
        result = filter_by_substring(strings, substring)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()