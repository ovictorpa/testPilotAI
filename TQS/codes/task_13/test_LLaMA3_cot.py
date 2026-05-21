from count_distinct_characters import *
import unittest

class TestDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)
        self.assertEqual(count_distinct_characters('A'), 1)

    def test_duplicate_characters(self):
        self.assertEqual(count_distinct_characters('aaa'), 1)
        self.assertEqual(count_distinct_characters('AAA'), 1)

    def test_uppercase_lowercase_mix(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_string_with_numbers_and_special_chars(self):
        self.assertEqual(count_distinct_characters('Hello, World!'), 7)

if __name__ == '__main__':
    unittest.main()