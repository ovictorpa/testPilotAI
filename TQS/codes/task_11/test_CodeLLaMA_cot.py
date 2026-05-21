from all_prefixes import *
import unittest
from typing import List

class TestAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [])
    
    def test_one_character_string(self):
        self.assertEqual(all_prefixes('a'), ['a'])
    
    def test_multi_character_string_no_repeats(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
    
    def test_multi_character_string_with_repeats(self):
        self.assertEqual(all_prefixes('aabbc'), ['aa', 'aab', 'aabb', 'aabbc'])
    
    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            all_prefixes(123)
    
    def test_invalid_character(self):
        with self.assertRaises(UnicodeEncodeError):
            all_prefixes('Ã¶')