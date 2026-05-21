from sum_product import *
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of the sum and the product of all the integers in the list.
    
    An empty sum should be equal to 0, and an empty product should be equal to 1.
    """
    sum_value = 0
    prod_value = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

import unittest

class TestSumProduct(unittest.TestCase):
    def test_sum_product(self):
        self.assertEqual((0, 1), sum_product([]))
        self.assertEqual((10, 24), sum_product([1, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()