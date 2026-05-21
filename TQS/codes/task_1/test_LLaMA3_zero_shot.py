from intersperse import *
import unittest
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:
        return []
    
    result = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)
    result.append(numbers[-1])
    return result


class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_elements_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_longer_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4, 5], 4), [1, 4, 2, 4, 4, 5])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            intersperse('a', 4)

    def test_invalid_input_type_delimiter(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2, 3], 'a')

if __name__ == '__main__':
    unittest.main()