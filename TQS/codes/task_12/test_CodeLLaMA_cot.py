from longest import *
import unittest
from typing import List, Optional

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))
    
    def test_single_element(self):
        self.assertEqual(longest(['a']), 'a')
    
    def test_multiple_elements(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')
    
    def test_duplicate_max_length(self):
        self.assertIsNone(longest(['a', 'aa', 'aa']))
    
    def test_input_type(self):
        with self.assertRaises(TypeError):
            longest('hello')