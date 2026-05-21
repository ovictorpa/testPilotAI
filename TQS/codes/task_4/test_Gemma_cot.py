from remove_duplicates import *
import unittest

from collections import Counter


def remove_duplicates(numbers: list[int]) -> list[int]:
    """
    From a list of integers, remove all elements that occur more than once.

    Keep the order of the elements left the same as in the input.

    """

    c = Counter(numbers)
    return [n for n in numbers if c[n] == 1]


class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_duplicates_removed(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_duplicates_preserved_order(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_large_list(self):
        self.assertEqual(remove_duplicates([1] * 100), [1] * 100)

    def test_none_type(self):
        with self.assertRaises(TypeError):
            remove_duplicates(None)

    def test_list_of_strings(self):
        with self.assertRaises(TypeError):
            remove_duplicates(["a", "b", "c", "b"])


if __name__ == "__main__":
    unittest.main()