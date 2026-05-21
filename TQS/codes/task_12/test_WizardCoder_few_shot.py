from longest import *
import unittest
from typing import List, Optional

class TestLongest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(longest([]), None)
    
    def test_single_element(self):
        self.assertEqual(longest(['a']), 'a')
    
    def test_multiple_elements(self):
        self.assertEqual(longest(['apple', 'banana', 'cherry']), 'banana')
    
    def test_no_max(self):
        self.assertEqual(longest(['cat', 'dog', 'bird']), None)
    
    def test_same_lengths(self):
        self.assertIn(longest(['car', 'airplane', 'boat'], ['bike', 'carpet', 'hat']), ['car', 'carpet'])