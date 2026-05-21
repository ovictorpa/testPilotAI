from check_Equality import *
import unittest

class TestCountSubstring(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(0, count_Substring_With_Equal_Ends(''))

    def test_single_character_string(self):
        self.assertEqual(1, count_Substring_With_Equal_Ends('a'))

    def test_simple_case(self):
        self.assertEqual(3, count_Substring_With_Equal_Ends('abababa'))

    def test_complex_case(self):
        self.assertEqual(10, count_Substring_With_Equal_Ends('abcdefghijklmnopqrstuvwxyz'))