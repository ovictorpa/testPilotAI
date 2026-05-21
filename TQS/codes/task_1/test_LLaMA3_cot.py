from intersperse import *
import unittest

class TestIntersperseFunction(unittest.TestCase):

    def test_empty_input(self):
        # Test case: Empty input list
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        # Test case: Single-element input list
        self.assertEqual(intersperse([1], 4), [1, 4])

    def test_two_elements(self):
        # Test case: Two-element input list
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2, 4])

    def test_longer_list(self):
        # Test case: Longer input list (three or more elements)
        self.assertEqual(intersperse([1, 2, 3, 4, 5], 4), [1, 4, 2, 4, 4, 5, 4])

    def test_longer_list_with_delimiter(self):
        # Test case: Longer input list with a specific delimiter
        self.assertEqual(intersperse([10, 20, 30, 40, 50], 5), [10, 5, 20, 5, 30, 5, 4, 40, 5, 50, 5])

    def test_empty_list_with_non_zero_delimiter(self):
        # Test case: Empty input list with non-zero delimiter
        self.assertEqual(intersperse([], 10), [])

if __name__ == '__main__':
    unittest.main()