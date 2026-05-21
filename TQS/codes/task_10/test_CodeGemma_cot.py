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

    def test_single_element_list(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_element_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_elements(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, -24))

    def test_mixed_elements(self):
        self.assertEqual(sum_product([1, 2, -3, 4]), (2, 8))


if __name__ == "__main__":
    unittest.main()