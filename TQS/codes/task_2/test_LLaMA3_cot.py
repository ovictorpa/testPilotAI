from how_many_times import *
import unittest

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_non_overlapping_substring(self):
        self.assertEqual(how_many_times('abcde', 'ab'), 1)
        self.assertEqual(how_many_times('abcdefg', 'abc'), 2)

    def test_overlapping_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaaaa', 'aa'), 6)

    def test_long_string(self):
        self.assertEqual(how_many_times('abcdabcdabcdabcd', 'ab'), 12)
        self.assertEqual(how_many_times('abcdefghijabcdefghijabcdefghij', 'ab'), 24)

    def test_non_alphabetic_substring(self):
        self.assertEqual(how_many_times('abc!de', '!'), 1)

    def test_substring_at_start_or_end(self):
        self.assertEqual(how_many_times('abcd123e', 'a'), 2)
        self.assertEqual(how_many_times('123456ab', 'z'), 0)

    def test_all_overlapping_occurrences(self):
        self.assertEqual(how_many_times('aaaaaa', 'aa'), 6)

if __name__ == '__main__':
    unittest.main()