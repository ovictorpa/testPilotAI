from filter_by_substring import *
import unittest


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_single_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_substring_not_found(self):
        self.assertEqual(filter_by_substring(['cde', 'array'], 'a'), [])

    def test_substring_in_multiple_words(self):
        self.assertEqual(filter_by_substring(['abc def', 'bacg', 'cde'], 'bc'), ['abc def', 'bacg'])


if __name__ == '__main__':
    unittest.main()