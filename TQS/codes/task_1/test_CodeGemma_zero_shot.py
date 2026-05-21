from intersperse import *
import unittest

from typing import List


class InterperseTestCase(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_three_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimiter_is_none(self):
        self.assertEqual(intersperse([1, 2, 3], None), [1, None, 2, None, 3])


if __name__ == '__main__':
    unittest.main()