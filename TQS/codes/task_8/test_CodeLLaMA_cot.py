from has_close_elements import *
import unittest

class TestHasCloseElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0))

    def test_single_element(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_positive_threshold(self):
        self.assertTrue(has_close_elements([1.0, 2.0], 1.0))

    def test_negative_threshold(self):
        self.assertFalse(has_close_elements([1.0, 2.0], -1.0))

    def test_duplicate_elements(self):
        self.assertTrue(has_close_elements([1.0, 1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            has_close_elements([1.0, "hello", 3.0, 4.0, 5.0, 2.0], 0.3)