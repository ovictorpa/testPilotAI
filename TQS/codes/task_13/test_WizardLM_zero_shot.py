from count_distinct_characters import *
import unittest
from unittest.mock import patch
from datetime import datetime

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

class TestCountDistinctCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_multiple_identical_characters(self):
        self.assertEqual(count_distinct_characters('aaaaaaa'), 1)

    def test_mixed_case_string(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_string_with_digits(self):
        self.assertEqual(count_distinct_characters('abc123'), 6)

    def test_string_with_punctuation(self):
        self.assertEqual(count_distinct_characters('Hello, World!'), 9)

    def test_string_with_special_characters(self):
        self.assertEqual(count_distinct_characters('Some#Special chars: @^%&*()), 10)

    def test_string_with_accents(self):
        self.assertEqual(count_distinct_characters('CafÃ©'), 4)

    def test_string_with_emojis(self):
        self.assertEqual(count_distinct_characters('ðŸ˜ŠHelloðŸ˜Š'), 6)

    def test_string_with_whitespace_characters(self):
        self.assertEqual(count_distinct_characters('\t\n '), 3)

    def test_case_sensitivity(self):
        self.assertNotEqual(count_distinct_characters('Foo'), count_distinct_characters('foo'))

    def test_string_with_dates(self):
        # Dates should be considered as a single character if using a locale that does not separate day and month
        self.assertEqual(count_distinct_characters(datetime.now().strftime("%Y-%m-%d")), 10)

    def test_string_with_newline(self):
        # Newlines are usually represented by `\n` in strings, but we want to treat them as distinct characters
        self.assertEqual(count_distinct_characters('\n'), 1)

if __name__ == '__main__':
    unittest.main()