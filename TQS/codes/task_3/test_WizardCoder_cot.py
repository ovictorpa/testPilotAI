import unittest
from is_happy import is_happy

class TestHappy(unittest.TestCase):
    def test_edge_case_empty_string(self):
        self.assertEqual(is_happy(""), False)

    def test_edge_case_single_letter(self):
        self.assertEqual(is_happy("a"), False)

    def test_edge_case_two_letters(self):
        self.assertEqual(is_happy("aa"), False)

    def test_edge_case_three_consecutive_same(self):
        self.assertEqual(is_happy("abcda"), False)

    def test_edge_case_four_consecutive_same(self):
        self.assertEqual(is_happy("abcbcde"), False)

    def test_not_happy(self):
        self.assertEqual(is_happy("aabbccddd"), False)

    def test_happy(self):
        self.assertEqual(is_happy("abcde"), True)