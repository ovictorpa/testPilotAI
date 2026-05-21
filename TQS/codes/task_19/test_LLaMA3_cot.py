from check_Equality import *
import unittest

class TestEqualityFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(check_Equality(""), 0)

    def test_single_character_string(self):
        self.assertEqual(check_Equality("a"), 1)
        self.assertEqual(check_Equality("A"), 1)
        # Only consider lowercase letters for this function

    def test_multi_character_string_with_repeated_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababa"), 3)

    def test_multi_character_string_with_alternating_characters(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcdefgh"), 1)

    def test_multi_character_string_without_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcde"), 0)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_Substring_With_Equal_Ends(1234)

    def test_non_string_input_with_spaces_and_punctuation(self):
        with self.assertRaises(TypeError):
            count/Substring_With_Equal_Ends("a b,c")

    def test_substring_count_calculation(self):
        # This function should return the same result as manually counting substrings
        # For example, for the string "abcd", it should return 2 (ab and cd)
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 2)


if __name__ == '__main__':
    unittest.main()