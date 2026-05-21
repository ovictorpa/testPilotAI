import unittest

from intersperse import intersperse


class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_odd_number_of_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_even_number_of_elements(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 4), [1, 4, 2, 4, 3, 4])


if __name__ == '__main__':
    unittest.main()