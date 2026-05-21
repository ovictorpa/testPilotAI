from intersperse import *
import unittest
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list `numbers`.
    
    >>> intersperse([], 4)
    []
    
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    
    if not numbers:
        return []
    
    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)
    
    result.append(numbers[-1])
    return result


class TestInterspersed(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])
        
    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 2), [1])
        
    def test_two_elements_list(self):
        self.assertEqual(intersperse([1, 2], 3), [1, 3, 2]
        
    def test_general_case(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 5), [1, 5, 2, 5, 3, 5, 4])
        
    def test_empty_delimiter(self):
        with self.assertRaises(ValueError):
            intersperse([1, 2], None)