from sum_product import *
import unittest
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    """
    For a given list of integers, return a tuple consisting of the sum and the product of all the integers in the list.
    An empty sum should be equal to 0, and an empty product should be equal to 1.
    """
    
    if not numbers: # edge case: empty list
        return (0, 1)
    else:
        total_sum = sum(numbers) # calculate the sum of all elements in the list
        prod_value = 1 # initialize product value to 1 for multiplication
        
        for n in numbers: # iterate through each element and multiply it with the current product value
            if isinstance(n, (int, float): # checking if the input is a number
                total_sum += n
                prod_value *= n
    
    return total_sum, prod_value # return tuple of sum and product values


class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))
    
    def test_single_element_list(self):
        self.assertEqual(sum_product([4]), (4, 4))
    
    def test_negative_integers(self):
        self.assertEqual(sum_product([-2,-3,-1]), (-6, -6))
    
    def test_positive_and_negative_integers(self):
        self.assertEqual(sum_product([1, 2, -3, 4], (7, -6)
    
    def test_zeroes(self):
        self.assertEqual(sum_product([0, 0, 0]), (0, 0))
    
    def test_floats(self):
        self.assertEqual(sum_product([2.5, -1.3, 0, 4.6], (3.1, -1.3*0.6)) # check if it can handle float inputs as well
    
if __name__ == '__main__':
    unittest.main()