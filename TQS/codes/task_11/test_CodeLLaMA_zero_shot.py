from all_prefixes import *
import unittest
from typing import List

class TestAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])

    def test_one_character_string(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_character_string(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_empty_list_for_non_strings(self):
        self.assertIsInstance(all_prefixes(1), List)

if __name__ == '__main__':
    unittest.main()