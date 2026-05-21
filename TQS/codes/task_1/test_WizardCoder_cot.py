from intersperse import *
import unittest
from typing import List

class TestIntersperse(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])
    
    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])
    
    def test_two_elements_list(self):
        self.assertEqual(intersperse([1,2], 4), [1, 4, 2])
    
    def test_three_elements_list(self):
        self.assertEqual(intersperse([1,2,3], 4), [1, 4, 2, 4, 3])
    
    def test_four_elements_list(self):
        self.assertEqual(intersperse([1,2,3,4], 5), [1, 5, 2, 5, 3, 5, 4])
    
    def test_no_delimiter_input(self):
        with self.assertRaises(TypeError) as context:
            intersperse([], None)
        self.assertEqual(str(context.exception), "Delimiter must be an integer")
    
    def test_noninteger_delimiter(self):
        with self.assertRaises(TypeError) as context:
            intersperse([], 'a')
        self.assertEqual(str(context.exception), "Delimiter must be an integer")
    
    def test_negative_delimiter(self):
        with self.assertRaises(ValueError) as context:
            intersperse([], -5)
        self.assertEqual(str(context.exception), "Delimiter must be a positive integer")