from how_many_times import *
import unittest

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string_empty_substring(self):
        self.assertEqual(how_many_times('', ''), 0)

    def test_single_character_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('abca', 'd'), 0)

    def test_substring_length_greater_than_string(self):
        with self.assertRaises(ValueError):
            how_many_times('a', 'aa')


if __name__ == '__main__':
    unittest.main()