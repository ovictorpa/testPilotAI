from sum_product import *
import unittest
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_positive_integers(self):
        self.assertEqual(sum_product([1, 2, 3]), (6, 6))

    def test_negative_integers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_mixed_signs(self):
        self.assertEqual(sum_product([1, 2, -3]), (0, 0))

    def test_floating_point_numbers(self):
        self.assertEqual(sum_product([1.5, 2.5, 3.5]), (7, 36.25))

    def test_string_input(self):
        with self.assertRaises(TypeError):
            sum_product(['a', 'b'])

    def test_large_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        result = sum_product(numbers)
        self.assertEqual(result[0], sum(numbers))
        self.assertEqual(result[1], reduce((lambda x, y: x * y), numbers))