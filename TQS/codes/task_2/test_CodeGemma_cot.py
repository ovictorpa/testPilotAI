from how_many_times import *
import unittest

class HowManyTimesTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times("", "a"), 0)

    def test_single_substring(self):
        self.assertEqual(how_many_times("aaa", "a"), 3)

    def test_multiple_substrings(self):
        self.assertEqual(how_many_times("aaaa", "aa"), 3)

    def test_overlapping_substrings(self):
        self.assertEqual(how_many_times("ababa", "ba"), 2)

    def test_different_substring(self):
        self.assertEqual(how_many_times("hello", "world"), 0)

    def test_long_string_and_substring(self):
        string = "a" * 1000
        substring = "a" * 100
        self.assertEqual(how_many_times(string, substring), 10)

if __name__ == '__main__':
    unittest.main()