from has_close_elements import *
import unittest

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:

    """

    Check if in given list of numbers, are any two numbers closer to each other than given threshold.


    """

    for idx, elem in enumerate(numbers):

        for idx2, elem2 in enumerate(numbers):

            if idx != idx2:

                distance = abs(elem - elem2)

                if distance < threshold:

                    return True

    return False


class TestHasCloseElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_list_with_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_list_without_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))


if __name__ == '__main__':
    unittest.main()