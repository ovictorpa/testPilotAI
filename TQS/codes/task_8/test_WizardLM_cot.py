import unittest
from typing import List

from has_close_elements import has_close_elements  # Replace 'your_module' with the actual module name where the function is defined

class TestHasCloseElements(unittest.TestCase):
    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_sorted_ascending(self):
        self.assertTrue(has_close_elements(sorted([1.0, 2.5, 3.5, 4.5]), 1.0))
        self.assertFalse(has_close_elements(sorted([1.0, 2.5, 3.5, 4.5], key=lambda x: x**2), 1.0))  # Test with squared values

    def test_sorted_descending(self):
        self.assertTrue(has_close_elements(sorted([5.0, 4.0, 3.0, 2.0, 1.0], reverse=True), 1.0))
        self.assertFalse(has_close_elements(sorted([5.0, 4.0, 3.0, 2.0, 1.0], key=lambda x: x**2, reverse=True), 1.0))  # Test with squared values

    def test_large_and_small_numbers(self):
        self.assertFalse(has_close_elements([1e-10, 3.0, 5e10], 2.0))

    def test_duplicate_elements(self):
        self.assertTrue(has_close_elements([1.0, 1.1, 2.2, 2.1, 1.0], 0.2))

    def test_empty_list(self):
        self.assertFalse(has_close_elements([] , 1.0))

    def test_single_element(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_threshold_zero(self):
        self.assertTrue(has_close_elements([1.0, 2.0], 0.0))
        self.assertFalse(has_close_elements([1.0, 2.1], 0.1))

    def test_large_threshold(self):
        self.assertFalse(has_close_elements([1.0, 2.0], 10.0))

    def test_precision(self):
        # Test for floating-point precision issues
        self.assertTrue(has_close_elements([1e-30, 1+1e-30], 2*1e-30))
        self.assertFalse(has_close_elements([1e-30, 1+1e-30], 1e-30))

    def test_complex_numbers(self):
        # Test with complex numbers (if the function allows it)
        self.assertTrue(has_close_elements([1+2j, 1-2j], 3))
        self.assertFalse(has_close_elements([1+2j, 1-1.5j], 2.5))

if __name__ == '__main__':
    unittest.main()