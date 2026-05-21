from count_distinct_characters import *
import unittest

class TestCountDistinctCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(""), 0)

    def test_duplicate_characters(self):
        self.assertEqual(count_distinct_characters("aaa"), 1)
        self.assertEqual(count_distinct_characters("zzz"), 1)

    def test_normal_string(self):
        self.assertEqual(count_distinct_characters("xyzXYZ"), 3)
        self.assertEqual(count_distinct_characters("Jerry"), 4)