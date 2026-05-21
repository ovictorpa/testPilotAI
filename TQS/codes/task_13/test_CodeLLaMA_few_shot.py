from count_distinct_characters import *
import unittest

class TestCountDistinctCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_distinct_characters('abcdefg'), 7)

    def test_case_insensitive(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)

    def test_non_ascii_characters(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)