from how_many_times import *
import unittest

class TestHowManyTimes(unittest.TestCase):
    
    def test_with_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)
    
    def test_with_single_char_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
    
    def test_with_longer_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
        
    def test_with_multiple_occurrences(self):
        self.assertEqual(how_many_times('banana', 'an'), 2)
    
    def test_with_no_occurence(self):
        self.assertEqual(how_many_times('hello world', 'zebra'), 0)
    
    def test_with_overlapping_occurrences(self):
        self.assertEqual(how_many_times('mississippi', 'is'), 2)