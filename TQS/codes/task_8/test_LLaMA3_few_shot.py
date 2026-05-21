import unittest
from has_close_elements import has_close_elements  # Import the function to test

class TestHasCloseElements(unittest.TestCase):

    def test_no_close_elements(self):
        """Test that no two elements are within threshold distance."""
        numbers = [1.0, 2.8, 3.0, 4.0, 5.0]
        self.assertFalse(has_close_elements(numbers, 0.5))

    def test_at_least_one_close_element(self):
        """Test that at least one pair of elements are within threshold distance."""
        numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
        self.assertTrue(has_close_elements(numbers, 0.3))

    def test_with_threshold_of_zero(self):
        """Test that no two elements are within threshold distance."""
        numbers = [1.0, 2.8, 3.0, 4.0, 5.0]
        self.assertFalse(has_close_elements(numbers, 0.0))

    def test_empty_list(self):
        """Test that an empty list returns False"""
        numbers = []
        self.assertFalse(has_close_elements(numbers, 0.5))

    def test_single_element_list(self):
        """Test that a single element list returns False"""
        numbers = [1.0]
        self.assertFalse(has_close_elements(numbers, 0.5))

if __name__ == '__main__':
    unittest.main()