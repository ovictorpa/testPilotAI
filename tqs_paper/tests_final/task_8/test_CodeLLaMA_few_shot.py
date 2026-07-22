from has_close_elements import *
import unittest
from typing import List

class TestHasCloseElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_single_element_list(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_one_close_element(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_multiple_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0, 1.9], 0.3))