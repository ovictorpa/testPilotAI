import unittest
from how_many_times import how_many_times

class TestHowManyTimes(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)
        
    def test_substring_not_found(self):
        self.assertEqual(how_many_times('hello world', 'foo'), 0)
        
    def test_overlapping_cases(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        
    def test_longer_substring(self):
        self.assertEqual(how_many_times('abcdefghi', 'hi'), 2)
        
    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaaaaa', 'aa'), 3)
        
    def test_even_length_substring(self):
        self.assertEqual(how_many_times('ababa', 'aba'), 4)
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()