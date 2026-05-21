from how_many_times import *
import unittest

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_substring_occurrence(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_multiple_substring_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 2)

    def test_no_substring_occurrences(self):
        self.assertEqual(how_many_times('abcd', 'xyz'), 0)

    def test_substring_is_empty(self):
        self.assertEqual(how_many_times('hello world', ''), 0)

    def test_substring_length_equals_string_length(self):
        self.assertEqual(how_many_times('a' * 100, 'a' * 100), 1)

if __name__ == '__main__':
    unittest.main()