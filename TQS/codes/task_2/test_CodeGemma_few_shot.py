from how_many_times import *
import unittest

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times("", "a"), 0)

    def test_single_substring(self):
        self.assertEqual(how_many_times("aaa", "a"), 3)

    def test_overlapping_substrings(self):
        self.assertEqual(how_many_times("aaaa", "aa"), 3)

    def test_substring_longer_than_string(self):
        self.assertEqual(how_many_times("a", "aa"), 0)

    def test_different_substrings(self):
        self.assertEqual(how_many_times("abc", "def"), 0)

    def test_edge_case(self):
        self.assertEqual(how_many_times("abc", "bc"), 1)

if __name__ == '__main__':
    unittest.main()