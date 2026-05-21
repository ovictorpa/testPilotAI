from count_distinct_characters import *
import unittest
from unittest.mock import patch

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

class TestCountDistinctCharacters(unittest.TestCase):
    def test_normal_case_with_alphabetic_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
    
    def test_with_non_alphabetic_characters(self):
        self.assertEqual(count_distinct_characters('Hello, World!'), 7)
    
    def test_with_repeated_characters(self):
        self.assertEqual(count_distinct_characters('aabc'), 4)
    
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)
    
    def test_with_whitespace_characters(self):
        self.assertEqual(count_distinct_characters('   '), 1)
    
    def test_with_a_mix_of_alphabetic_and_non_alphabetic_characters(self):
        self.assertEqual(count_distinct_characters('Hello123!'), 8)
    
    def test_case_insensitivity(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters('jerry'), 4)
        self.assertEqual(count_distinct_characters('JeRrY'), 4)
    
    def test_with_unicode_characters(self):
        self.assertEqual(count_distinct_characters('HÃ©llÃ¶ WÃ¶rld!'), 9)
    
    def test_with_accented_characters(self):
        self.assertEqual(count_distinct_characters('cafÃ©'), 5)
    
    def test_performance_with_large_string(self):
        large_str = 'a' * 10000  # A string with 10000 'a' characters
        self.assertEqual(count_distinct_characters(large_str), 1)
    
    def test_performance_with_very_large_string(self):
        very_large_str = 'a' * 10**7  # A string with 10 million 'a' characters
        with patch('sys.stdout', open(os.devnull, 'w')):  # Suppress output to avoid performance impact due to logging
            self.assertEqual(count_distinct_characters(very_large_str), 1)

if __name__ == '__main__':
    unittest.main()