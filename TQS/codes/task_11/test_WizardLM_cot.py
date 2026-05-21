from all_prefixes import *
import unittest
from typing import List

class TestAllPrefixes(unittest.TestCase):
    def test_non_empty_string(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

    def test_one_character_string(self):
        self.assertEqual(all_prefixes('a'), ['a'])

    def test_multiple_characters_string(self):
        self.assertEqual(all_prefixes('hello'), ['h', 'he', 'hel', 'hell', 'hello'])

    def test_ascii_letters_and_numbers(self):
        self.assertEqual(all_prefixes('a1!'), ['a', 'a1', 'a1!', 'a1! '])

    def test_special_characters(self):
        self.assertEqual(all_prefixes('gr@p#'), ['g', 'gr', 'gr@', 'gr@p', 'gr@p#'])

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [''])

    def test_whitespace_only_string(self):
        self.assertEqual(all_prefixes('   '), ['', ' ', '  ', '   '])

    def test_non_printable_characters(self):
        self.assertEqual(all_prefixes('\x01abc'), ['\x01', '\x01a', '\x01ab', '\x01abc'])

    def test_leading_whitespace(self):
        self.assertEqual(all_prefixes('  abc'), ['  ', '  ab', '  abc', 'abc'])

    def test_trailing_whitespace(self):
        self.assertEqual(all_prefixes('abc '), ['abc ', 'abc', 'ab', 'a'])

    def test_mixed_case_string(self):
        self.assertEqual(all_prefixes('FooBar'), ['F', ' Fo', ' Foob', ' FooBar', 'FooBa', 'FooBar'])

    def test_no_prefix_for_empty_result(self):
        self.assertEqual(all_prefixes('')[:0], [''])

    def test_slicing_beyond_string_length(self):
        self.assertEqual(all_prefixes('abcde')[4:], ['abcde'])

    def test_case_insensitivity(self):
        self.assertEqual(all_prefixes('ABC'), [
            'ABC', 'ABCa', 'ABCb', 'ABCc', 'aBC', 'bBC', 'cBC', 'abcB', 'abCB', 'abc'
        ])

    def test_returning_correct_order(self):
        self.assertEqual(all_prefixes('xyz'), ['x', 'xy', 'xyz'])

if __name__ == '__main__':
    unittest.main()