from TQS.tests_final.task_1.intersperse import *
import unittest


class TestInterperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_intersecting_even_numbers(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_intersecting_odd_numbers(self):
        self.assertEqual(intersperse([1, 3, 5], 2), [1, 2, 3, 2, 5])


if __name__ == '__main__':
    unittest.main()