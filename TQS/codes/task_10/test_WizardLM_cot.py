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

    def test_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-8, 24))

    def test_positive_and_negative_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (1, -24))

    def test_zero_in_list(self):
        self.assertEqual(sum_product([0, 1, 2, 3]), (6, 0))
        self.assertEqual(sum_product([0]), (0, 1))

    def test_floating_point_numbers(self):
        self.assertTupleEqual(sum_product([1.5, 2.5, 3.5]), ((7.5, 156.25)))

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            sum_product(['a', 'b', 'c'])

    def test_large_numbers(self):
        large_list = [10**6, 2*10**6]
        self.assertEqual(sum_product(large_list), (3000006, 2))

    def test_small_numbers(self).parametrize(
        'numbers',
        [(-1<<62, -2<<62), (-1<<96, -2<<96)],
        expect_no_float=True
    )
    def test_same_number(self, numbers):
        self.assertEqual(sum_product([numbers[0], numbers[0]]), (numbers[0] * 2, numbers[0]))

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            sum_product([None, 1, 2])

    def test_performance_with_large_list(self):
        large_list = list(range(10**6))
        result = sum_product(large_list)
        self.assertEqual(result, (500000500000, 50000049999987648))

if __name__ == '__main__':
    unittest.main()