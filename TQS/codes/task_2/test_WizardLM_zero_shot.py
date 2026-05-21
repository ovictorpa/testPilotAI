from how_many_times import *
import unittest

def how_many_times(string: str, substring: str) -> int:
    times = 0
    substring_length = len(substring)
    for i in range(len(string) - substring_length + 1):
        if string[i:i + substring_length] == substring:
            times += 1
    return times

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)
    
    def test_substring_not_in_string(self):
        self.assertEqual(how_many_times('hello', 'world'), 0)
    
    def test_substring_in_string_once(self):
        self.assertEqual(how_many_times('abcdef', 'abc'), 1)
    
    def test_substring_in_string_twice(self):
        self.assertEqual(how_many_times('abababc', 'ab'), 2)
    
    def test_substring_in_string_multiple_times(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
    
    def test_substring_in_string_with_overlap(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
    
    def test_substring_at_start_of_string(self):
        self.assertEqual(how_many_times('abcabc', 'abc'), 2)
    
    def test_substring_at_end_of_string(self):
        self.assertEqual(how_many_times('abcabc', 'cab'), 1)
    
    def test_substring_case_insensitive(self):
        self.assertEqual(how_many_times('This is a Test', 'test'), 1)
    
    def test_multiple_instances_different_cases(self):
        self.assertEqual(how_many_times('Hello World', 'hello'), 2)
    
    def test_substring_with_whitespace(self):
        self.assertEqual(how_many_times('  Hello World  ', 'hello'), 1)
    
    def test_empty_substring(self):
        with self.assertRaises(ValueError):
            how_many_times('hello', '')
    
    def test_substring_with_newline(self):
        self.assertEqual(how_many_times('Line 1\nLine 2\nLine 1', 'Line 1'), 2)
    
    def test_substring_across_lines(self):
        self.assertEqual(how_many_times('Line 1\nLine 2 Line 3\nLine 1', 'Line 1'), 2)
    
    def test_substring_spanning_entire_string(self):
        self.assertEqual(how_many_times('abcdefghij', 'abcdefghij'), 1)
    
    def test_substring_spanning_entire_string_with_overlap(self):
        self.assertEqual(how_many_times('abcabcabcabcabc', 'abcaaaaa'), 2)

if __name__ == '__main__':
    unittest.main()