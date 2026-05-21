from all_prefixes import *
import unittest

from typing import List


class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_single_character(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_long_string(self):
        self.assertEqual(all_prefixes('abcdefghijklmnopqrstuvwxyz'), [
            'a', 'ab', 'abc', 'abcd', ... 'abcdefghijklmnopqrstuvwxyz'])

    def test_prefix_length_0(self):
        self.assertEqual(all_prefixes('abc')[0], '')

    def test_prefix_length_1(self):
        self.assertEqual(all_prefixes('abc')[1], 'a')

    def test_prefix_length_equal_to_string_length(self):
        self.assertEqual(all_prefixes('abc')[2], 'abc')


if __name__ == '__main__':
    unittest.main()