from how_many_times import *
import unittest

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_chars(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('abca', 'd'), 0)

    def test_substring_length_zero(self):
        self.assertEqual(how_many_times('abca', ''), 4)

    def test_long_string(self):
        self.assertEqual(how_many_times('abcdefghijklmnopqrst', 'pqr'), 1)


if __name__ == '__main__':
    unittest.main()