from sum_product import *
import unittest
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    """
    For a given list of integers, return a tuple consisting of the sum and the product of all the integers in the list.
    An empty sum should be equal to 0, and an empty product should be equal to 1.
    
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    
    if not numbers:
        return 0, 1
    
    else:
        sum_value = 0
        prod_value = 1
        for n in numbers:
            sum_value += n
            prod_value *= n
        return (sum_value, prod_value)