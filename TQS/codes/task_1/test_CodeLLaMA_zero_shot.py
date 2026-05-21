from intersperse import *
import unittest
from typing import List

class TestIntersperse(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_elements(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_three_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimiter_at_start(self):
        self.assertEqual(intersperse([4, 1, 2, 3], 4), [4, 1, 4, 2, 4, 3])

    def test_delimiter_at_end(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 4), [1, 4, 2, 4, 3, 4])

if __name__ == '__main__':
    unittest.main()