from how_many_times import *
import unittest

def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, counting overlapping cases.
    
    :param string: The original string to search within.
    :param substring: The substring to search for.
    :return: The number of non-overlapping occurrences of the substring in the string.
    """
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
        self.assertEqual(how_many_times('abcdef', 'def'), 1)

    def test_substring_in_string_twice(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 2)

    def test_substring_in_string_three_times(self):
        self.assertEqual(how_many_times('aaaa', 'aaa'), 3)

    def test_substring_in_string_overlapping(self):
        self.assertEqual(how_many_times('abcabc', 'bc'), 2)  # Overlapping case

    def test_empty_substring(self):
        self.assertEqual(how_many_times('hello', ''), 0)

    def test_substring_in_string_multiple_occurrences(self):
        self.assertEqual(how_many_times('ababab', 'ab'), 3)

    def test_case_sensitivity(self):
        self.assertEqual(how_many_times('HelloWorld', 'hello'), 1)

    def test_substring_at_end_of_string(self):
        self.assertEqual(how_many_times('abcde', 'cde'), 1)

    def test_substring_at_start_of_string(self):
        self.assertEqual(how_many_times('abcd', 'abcd'), 1)

    def test_substring_spanning_entire_string(self):
        self.assertEqual(how_many_times('abcdefgh', 'abcdefghi'), 1)

    def test_substring_with_whitespace(self):
        self.assertEqual(how_many_times('Hello World ', 'Hello World'), 1)

    # Additional tests for edge cases or performance considerations could be added here:
    def test_performance_with_large_strings(self):
        large_string = 'a' * 1000
        large_substring = 'a' * 500
        self.assertEqual(how_many_times(large_string, large_substring), 2)

    def test_performance_with_very_large_strings(self):
        very_large_string = 'a' * 10**6
        very_large_substring = 'a' * 10**5
        self.assertEqual(how_many_times(very_large_string, very_large_substring), 10)

if __name__ == '__main__':
    unittest.main()