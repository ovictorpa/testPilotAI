from all_prefixes import *
import unittest
from typing import List

def all_prefixes(string: str) -> List[str]:
    
    """
    Return a list of all prefixes of the input string, from shortest to longest.
    
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    
    result = []
    for i in range(len(string)):
        result.append(string[:i + 1])
    return result

class TestAllPrefixes(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(all_prefixes(''), [])
    
    def test_single_letter(self):
        self.assertEqual(all_prefixes('a'), ['a'])
        
    def test_multi_letters(self):
        self.assertEqual(all_prefixes('ab'), ['a', 'ab'])
        
    def test_longer_string(self):
        self.assertEqual(all_prefixes('abcdefghijklmnopqrstuvwxyz'), ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef',
                            'abcdefg', 'abcdefh', 'abcdefi', 'abcdefj', 'abcdefk', 'abcdefl', 'abcdefm', 'abcdefn',
                            'abcdefo', 'abcdefp', 'abcdeft', 'abcdefu', 'abcdefv', 'abcdefw', 'abcdefx', 'abcdefy',
                            'abcdefz'])
        
    def test_multiple_strings(self):
        self.assertEqual(all_prefixes(['ab', 'cd', 'ef']), ['a', 'ab', 'c', 'cd', 'd', 'e', 'ef'])