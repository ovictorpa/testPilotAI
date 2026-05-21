from has_close_elements import *
import unittest
from typing import List, Tuple

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of floating point numbers.
        threshold (float): Threshold for distance between two elements.

    Returns:
        bool: True if any two numbers in the list have a distance smaller than the given threshold, False otherwise.
    
    """
    for idx, elem in enumerate(numbers):

        for idx2, elem2 in enumerate(numbers):
            if idx != idx2 and abs(elem - elem2) < threshold:
                return True
    return False

class TestHasCloseElements(unittest.TestCase):
    
    def test_no_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.5), False)
        
    def test_close_elements(self):
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3), True)
    
    def test_single_element(self):
        self.assertEqual(has_close_elements([1.0], 0.5), False)
        
    def test_threshold_equal_to_distance(self):
        self.assertEqual(has_close_elements([2, 3, 4], 1.0), True)
    
    def test_empty_list(self):
        self.assertEqual(has_close_elements([], 0.5), False)
        
    def test_negative_threshold(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], -1.0), False)
    
    def test_threshold_greater_than_distance(self):
        self.assertEqual(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 1.5), False)
        
    def test_zero_threshold(self):
        self.assertEqual(has_close_elements([1.0, 2.0, 3.0], 0.0), True