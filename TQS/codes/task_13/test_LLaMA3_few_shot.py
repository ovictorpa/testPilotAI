from count_distinct_characters import *
import unittest

def count_distinct_characters(string: str) -> int:
    # Function implementation here...
    pass

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_distinct_characters("xyzXYZ"), 3)

    def test_case_insensitive(self):
        self.assertEqual(count_distinct_characters("Jerry"), 4)

    def test_no_duplicates(self):
        self.assertEqual(count_distinct_characters("aaaaaa"), 1)

    def test_whitespace(self):
        self.assertEqual(count_distinct_characters("   "), 0)

    def test_numbers_and_special_chars(self):
        self.assertEqual(count_distinct_characters("123!@#"), 3)

if __name__ == '__main__':
    unittest.main()