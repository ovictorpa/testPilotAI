from check_Equality import *
class TestCheckEquality:
    def test_empty_string(self):
        self.assertEqual(check_Equality(''), False)

    def test_single_character_string(self):
        self.assertEqual(check_Equality('a'), True)

    def test_string_with_equal_ends(self):
        self.assertEqual(check_Equality('abcdcba'), True)

    def test_string_with_unequal_ends(self):
        self.assertEqual(check_Equality('abcdabc'), False)

class TestCountSubstringWithEqualEnds:
    def test_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(''), 0)

    def test_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends('a'), 1)

    def test_string_with_equal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abcdcba'), 2)

    def test_string_with_unequal_ends(self):
        self.assertEqual(count_Substring_With_Equal_Ends('abcdabc'), 1)