from count_distinct_characters import *
import unittest

class TestCountDistinctCharacters(unittest.TestCase):

    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters('aAbBcCd'), 6)
        self.assertEqual(count_distinct_characters('aabbccddee'), 6)
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 8)


if __name__ == '__main__':
    unittest.main()