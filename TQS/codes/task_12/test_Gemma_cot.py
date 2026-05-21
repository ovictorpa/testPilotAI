from longest import *
import unittest

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:

    if not strings:
        return None

    maxlen = max(len(x) for x in strings)

    for s in strings:
        if len(s) == maxlen:
            return s


class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_strings_equal_length(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_string_longer_than_others(self):
        self.assertEqual(longest(['ab', 'abc', 'abcd']), 'abcd')

    def test_string_shorter_than_others(self):
        self.assertEqual(longest(['xyz', 'y', 'z']), 'xyz')


if __name__ == '__main__':
    unittest.main()