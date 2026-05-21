from check_Equality import *
import unittest

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(''), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends('a'), 1)

    def test_string_with_only_equal_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends('aaabbbccdddeeeefff'), 10)

    def test_string_with_different_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abcdefa'), 0)

    def test_large_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abcabcdeffedcba'), 12)

if __name__ == '__main__':
    unittest.main()