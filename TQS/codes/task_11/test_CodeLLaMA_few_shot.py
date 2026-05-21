from all_prefixes import *
import unittest
from typing import List


class TestAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_single_character(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_characters(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_longer_string(self):
        self.assertEqual(all_prefixes('abcdefghijklmnopqrstuvwxyz'), [
            'a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh',
            'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl',
            'abcdefghijklm', 'abcdefghijklmn', 'abcdefghijklmno',
            'abcdefghijklmnop', 'abcdefghijklmnopq', 'abcdefghijklmnopqu',
            'abcdefghijklmnopqrs', 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrstu',
            'abcdefghijklmnopqrstuv', 'abcdefghijklmnopqrstuvw',
            'abcdefghijklmnopqrstuvwx', 'abcdefghijklmnopqrstuvwxy',
            'abcdefghijklmnopqrstuvwxyz'
        ])