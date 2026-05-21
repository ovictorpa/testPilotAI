from filter_by_substring import *
import unittest
from typing import List

class TestFilterSubstring(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])
    
    def test_no_matching_substrings(self):
        self.assertEqual(filter_by_substring(['def', 'ghi'], 'a'), [])
    
    def test_all_matching_substrings(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])
    
    def test_no_matching_substring(self):
        self.assertEqual(filter_by_substring(['abcdef', 'ghijkl', 'mnopqr'], 'z'), [])
    
    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            filter_by_substring([123, 'abc', 456], 'a')
    
    def test_general_case_1(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'r'), ['array'])
    
    def test_general_case_2(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])
    
    def test_general_case_3(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ar'), ['array']