from intersperse import *
from typing import List
from unittest import TestCase, main

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:
        return []
    
    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)
    result.append(numbers[-1])
    return result

class Testintersperse(TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])
    
    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1, 4])
    
    def test_no_delimiter(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 2, 3])
    
    def test_with_delimiter(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])
    
    def test_with_negative_delimiter(self):
        self.assertEqual(intersperse([1, 2], -1), [1, -1, 2, -1])
    
    def test_all_elements_same(self):
        self.assertEqual(intersperse([1, 1, 1], 4), [1, 4, 1, 4, 1])
    
    def test_delimiter_is_zero(self):
        self.assertEqual(intersperse([1, 2], 0), [1, 2])
    
    def test_mixed_types(self):
        self.assertEqual(intersperse([1, 'a', 3.5], '|'), [1, '|', 'a', '|', 3.5])
    
    def test_delimiter_in_list(self):
        self.assertEqual(intersperse([1, 2, 4], 3), [1, 3, 2, 3, 4])
    
    def test_large_list(self):
        numbers = list(range(1, 6))
        self.assertEqual(intersperse(numbers, 2), [1, 2, 3, 2, 4, 2, 5])
    
    def test_empty_delimiter(self):
        self.assertEqual(intersperse([1, 2, 3], ''), ['1', '', '2', '', '3'])
    
    def test_non_integer_delimiter(self):
        self.assertEqual(intersperse([1, 2], 'x'), [1, 'x', 2, 'x'])