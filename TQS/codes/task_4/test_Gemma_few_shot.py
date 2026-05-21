from remove_duplicates import *
import unittest

from typing import List

import collections


def remove_duplicates(numbers: List[int]) -> List[int]:

    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] == 1]


class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_duplicates_removed(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_duplicates_in_order(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3]), [1, 3])


if __name__ == '__main__':
    unittest.main()