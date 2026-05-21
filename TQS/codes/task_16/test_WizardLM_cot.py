from remove_Occ import *
import unittest

def remove_Occ(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            s = s[:i] + s[i+1:]
            break
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ch:
            s = s[:i] + s[i+1:]
            break
    return s

class TestRemoveOcc(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_Occ("", 'a'), "")

    def test_single_occurrence(self):
        self.assertEqual(remove_Occ("hello", 'o'), "helo")

    def test_multiple_occurrences(self):
        self.assertEqual(remove_Occ("abracadabra", 'a'), "brcbr")

    def test_no_occurrence(self):
        self.assertEqual(remove_Occ("world", 'o'), "world")

    def test_all_character_string(self):
        self.assertEqual(remove_Occ("aaabbcc", 'a'), "")

    def test_mixed_cases(self):
        self.assertEqual(remove_Occ("Hello World", 'l'), "Heo Wrd")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_Occ(12345, 'a')

    def test_large_strings(self):
        # Assuming the function can handle large strings without performance issues
        large_str = 'a' * 10000
        self.assertEqual(remove_Occ(large_str, 'a'), "")

if __name__ == '__main__':
    unittest.main()