import unittest
from count_distinct_characters import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):
    
    def test_lowercase(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        
    def test_uppercase(self):
        self.assertEqual(count_distinct_characters('jERRY'), 4)
    
    def test_empty(self):
        self.assertEqual(count_distinct_characters(''), 0)
    
    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)
    
    def test_no_duplicates(self):
        self.assertEqual(count_distinct_characters('hello'), 5)
    
    def test_punctuation(self):
        self.assertEqual(count_distinct_characters('hello, world!'), 10)
    
if __name__ == '__main__':
    unittest.main()