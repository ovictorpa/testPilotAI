from count_distinct_characters import *
import unittest

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))


class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)

    def test_uppercase_and_lowercase_characters(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_string_with_duplicates(self):
        self.assertEqual(count_distinct_characters('aaabbcc'), 3)


if __name__ == '__main__':
    unittest.main()