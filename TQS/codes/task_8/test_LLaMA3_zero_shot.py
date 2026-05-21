import unittest
from has_close_elements import has_close_elements  # Import the function from your module

class TestHasCloseElements(unittest.TestCase):

    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_at_least_one_close_element(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            has_close_elements([], 0.5)

    def test_threshold_zero(self):
        with self.assertRaises(ZeroDivisionError):
            has_close_elements([1.0, 2.0, 3.0], 0.0)

    def test_same_element(self):
        self.assertFalse(has_close_elements([1.0, 1.0, 1.0], 0.5))

    def test_large_threshold(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 3.0], float('inf')))

if __name__ == '__main__':
    unittest.main()