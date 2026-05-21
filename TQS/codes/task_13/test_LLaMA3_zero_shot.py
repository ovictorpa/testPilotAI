from count_distinct_characters import *
import unittest

def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters it consists of, regardless of case.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    return len(set(string.lower()))

class TestDistinctCharacters(unittest.TestCase):
    
    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        
    def test_case_sensitive_string(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        
    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)
        
    def test_only_whitespace(self):
        self.assertEqual(count_distinct_characters('   '), 0)

if __name__ == '__main__':
    unittest.main()