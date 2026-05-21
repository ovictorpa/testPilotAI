from intersperse import *
import unittest


class TestInterperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_elements(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimiter_is_zero(self):
        self.assertRaises(ValueError, lambda: intersperse([1, 2], 0))


if __name__ == '__main__':
    unittest.main()