from all_prefixes import *
import unittest
from typing import List, Tuple

class TestAllPrefixes(unittest.TestCase):
  
    def test_edge_cases(self):
        self.assertEqual(all_prefixes(''), [])
        self.assertEqual(all_prefixes('a'), ['a'])
        self.assertEqual(all_prefixes('ab'), ['a', 'ab'])
    
    def test_behaviour(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertEqual(all_prefixes('1234567890'), ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789', '1234567890'])
        self.assertEqual(all_prefixes('hello world'), ['h', 'he', 'hel', 'hell', 'hello', 'hellw', 'hellow', 'world', 'worl']
    
    def test_exceptions(self):
        with self.assertRaises(TypeError):
            all_prefixes(123) # raises TypeError because string argument is expected to be of type str.
        
if __name__ == '__main__':
    unittest.main()