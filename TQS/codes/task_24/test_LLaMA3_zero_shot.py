import unittest
from check_Equality import check_Equality, count_Substring_With_Equal_Ends

class TestFunctions(unittest.TestCase):

    def test_check_equality(self):
        self.assertTrue(check_Equality("ab"))
        self.assertFalse(check_Equality("abc"))

    def test_count_substring_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abab"), 3)
        self.assertEqual(count/Substring_With_Equal_Ends("abcabcabc"), 0)
        self.assertEqual(count/Substring_With_Equal_Ends("ab"), 1)

    def test_count_substring_with_equal_ends_empty_string(self):
        with self.assertRaises(RecursionError):
            count_Substring_With_Equal_Ends("")

    def test_count_substring_with_equal_ends_single_character_string(self):
        self.assertEqual(count/Substring_With_Equal_Ends("a"), 0)

if __name__ == '__main__':
    unittest.main()