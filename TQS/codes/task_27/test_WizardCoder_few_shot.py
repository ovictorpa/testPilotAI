import unittest
import re
from remove_multiple_spaces import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    
    def test_remove_multiple_spaces_one_space(self):
        self.assertEqual(remove_multiple_spaces('hello   world'), 'hello world')
        
    def test_remove_multiple_spaces_two_spaces(self):
        self.assertEqual(remove_multiple_spaces('  hello     world  '), 'hello world')
        
    def test_remove_multiple_spaces_zero_space(self):
        self.assertEqual(remove_multiple_spaces('hello world'), 'hello world')
        
    def test_remove_multiple_spaces_empty_string(self):
        self.assertEqual(remove_multiple_spaces(''), '')
        
    def test_remove_multiple_spaces_no_space(self):
        self.assertEqual(remove_multiple_spaces('hello'), 'hello')
        
    def test_remove_multiple_spaces_none(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(None)
        
    def test_remove_multiple_spaces_list(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(['hello', 'world'])