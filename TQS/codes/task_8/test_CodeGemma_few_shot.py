from has_close_elements import *
import unittest

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False


class TestHasCloseElements(unittest.TestCase):
    def test_has_close_elements_true(self):
        numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
        threshold = 0.3
        self.assertTrue(has_close_elements(numbers, threshold))

    def test_has_close_elements_false(self):
        numbers = [1.0, 2.0, 3.0]
        threshold = 0.5
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_has_close_elements_empty_list(self):
        numbers = []
        threshold = 0.5
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_has_close_elements_single_element_list(self):
        numbers = [1.0]
        threshold = 0.5
        self.assertFalse(has_close_elements(numbers, threshold))

if __name__ == '__main__':
    unittest.main()