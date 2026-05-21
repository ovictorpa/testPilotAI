from filter_by_substring import *
import unittest
from typing import List

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_nonempty_input(self):
        strings = ['abc', 'bacd', 'cde', 'array']
        substring = 'a'
        expected = ['abc', 'bacd', 'array']
        self.assertEqual(filter_by_substring(strings, substring), expected)