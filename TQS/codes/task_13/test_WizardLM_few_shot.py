from count_distinct_characters import *
import unittest

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

class TestCountDistinctCharacters(unittest.TestCase):
    def test_no_characters(self):
        self.assertEqual(count_distinct_characters(''), 0)
    
    def test_with_whitespace(self):
        self.assertEqual(count_distinct_characters(' '), 1)
    
    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)
    
    def test_case_insensitive(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
    
    def test_multiple_identical_characters(self):
        self.assertEqual(count_distinct_characters('aaaaa'), 1)
    
    def test_uppercase_letters(self):
        self.assertEqual(count_distinct_characters('ABCabc'), 6)
    
    def test_punctuation(self):
        self.assertEqual(count_distinct_characters('Hello, World!'), 8)
    
    def test_special_characters(self):
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)
    
    def test_accented_characters(self):
        self.assertEqual(count_distinct_characters('CafÃ©'), 4)
    
    def test_emoji(self):
        self.assertEqual(count_distinct_characters('ðŸ˜€ðŸ˜„ðŸ˜‚'), 3)
    
    def test_empty_string_with_whitespace(self):
        self.assertEqual(count_distinct_characters('\n'), 1)
    
    def test_mixed_case_with_digits(self):
        self.assertEqual(count_distinct_characters('HeLlO123'), 7)
    
    def test_non_alphanumeric_characters(self):
        self.assertEqual(count_distinct_characters('This is a test! 12345'), 10)
    
    def test_string_with_newlines(self):
        self.assertEqual(count_distinct_characters('\n\rHello, World!\n'), 9)
    
    def test_string_with_tab(self):
        self.assertEqual(count_distinct_characters('\tHello, World!\t'), 8)
    
    # Additional tests can be added to cover more edge cases or special characters.

if __name__ == '__main__':
    unittest.main()