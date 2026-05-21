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

    def test_duplicates_at_the_beginning(self):
        self.assertEqual(remove_duplicates([2, 2, 3, 3]), [2, 3])

    def test_duplicates_in_the_middle(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4]), [1, 3, 4])

    def test_duplicates_at_the_end(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 4]), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()