from count_distinct_characters import *
import unittest

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_single_character_string(self):
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_multiple_distinct_characters(self):
        self.assertEqual(count_distinct_characters("hello"), 4)

    def test_multiple_non_distinct_characters(self):
        self.assertEqual(count_distinct_characters("Mississippi"), 4)

    def test_mixed_case_characters(self):
        self.assertEqual(count_distinct_characters("Jerry"), 4)

if __name__ == '__main__':
    unittest.main()