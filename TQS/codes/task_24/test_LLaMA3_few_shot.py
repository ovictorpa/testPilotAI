import unittest
from check_Equality import check_Equality, count_Substring_With_Equal_Ends

class TestCheckEquality(unittest.TestCase):

    def test_check_equality_one_character_string(self):
        self.assertTrue(check_Equality('a'))
        
    def test_check_equality_two_characters_string(self):
        self.assertTrue(check_Equality('ab'))

    def test_check_equality_no_matching_characters_string(self):
        self.assertFalse(check_Equality('abc'))

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_count_substring_with_equal_ends_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)
        
    def test_count_substring_with_equal_ends_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal Ends("a"), 0)

    def test_count_substring_with_equal_ends_two_characters_string(self):
        self.assertEqual(count_Substring_With_Equal Ends("ab"), 1)

    def test_count_substring_with_equal_ends_three_characters_string(self):
        self.assertEqual(count_Substring_With_Equal Ends("abc"), 2)
        
    def test_count_substring_with_equal_ends_multiple_strings(self):
        self.assertEqual(count_Substring_With_Equal Ends('abcb'), 4)


if __name__ == '__main__':
    unittest.main()