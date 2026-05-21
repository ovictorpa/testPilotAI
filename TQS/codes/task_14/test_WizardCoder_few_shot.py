from filter_by_prefix import *
import unittest
from typing import List

class TestFilterByPrefix(unittest.TestCase):
    
    def test_empty_list_given(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
        
    def test_empty_string_prefix_given(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], ''), ['abc', 'bcd', 'cde', 'array'])
        
    def test_single_element_list(self):
        self.assertEqual(filter_by_prefix(['a'], 'a'), ['a'])
        
    def test_no_matching_elements(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z'), [])
        
    def test_no_elements_in_list(self):
        self.assertEqual(filter_by_prefix([], 'a')
        
    def test_multiple_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'abcd', 'array'], 'a'), ['abc', 'abcd'])
        
    def test_case_sensitive(self):
        self.assertEqual(filter_by_prefix(['Abc', 'bcd', 'ABCd', 'Array'], 'A')
        
    def test_non_string_elements(self):
        self.assertRaises(TypeError, filter_by_prefix([123, 'abc', 456], 'a')