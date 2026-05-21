from has_close_elements import *
import unittest
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False

class TestHasCloseElements(unittest.TestCase):
    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))
    
    def test_close_elements_found(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
    
    def test_elements_within_threshold(self):
        self.assertTrue(has_close_elements([1.1, 1.2, 1.3], 0.1))
    
    def test_no_elements_within_threshold_after_sorting(self):
        numbers = [3.5, 4.1, 5.7]
        self.assertFalse(has_close_elements(numbers, 2.0))
        sorted_numbers = sorted(numbers)
        self.assertFalse(has_close_elements(sorted_numbers, 2.0))
    
    def test_exact_threshold_case(self):
        self.assertTrue(has_close_elements([1.5, 1.4], 0.1))
    
    def test_same_number_with_threshold(self):
        self.assertFalse(has_close_elements([1.0, 1.0], 0.3))
    
    def test_very_small_threshold(self):
        self.assertTrue(has_close_elements([1.0, 2.0 + 1e-10], 1e-10))
    
    def test_large_numbers(self):
        self.assertTrue(has_close_elements([1000000.1, 1000000.2], 0.1))
    
    def test_no_close_elements_with_negative_threshold(self):
        self.assertFalse(has_close_elements([-1.0, -2.0, 3.0], -0.5))
    
    def test_close_elements_with_large_list(self):
        large_list = [i + j for i in range(10) for j in range(10)]
        self.assertTrue(has_close_elements(large_list, 5.0))
    
    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 10.0))
    
    def test_threshold_larger_than_distance_between_any_pair(self):
        self.assertFalse(has_close_elements([1.0, 2000000.0], 2000000.5))
    
    def test_threshold_equal_to_max_distance_in_list(self):
        numbers = [1.0, 3.0]
        self.assertTrue(has_close_elements(numbers, max(numbers) - min(numbers)))
    
    def test_case_insensitivity_with_float(self):
        # Test to ensure that floating point representation issues don't cause false negatives
        self.assertTrue(has_close_elements([0.123456789, 0.123456789], 0.00000001))
    
    def test_case_insensitivity_with_large_numbers(self):
        self.assertTrue(has_close_elements([1e18 + 1, 1e18], 1e17))

if __name__ == '__main__':
    unittest.main()