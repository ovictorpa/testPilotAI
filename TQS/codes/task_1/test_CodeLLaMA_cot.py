from intersperse import *
import unittest

class TestIntersperse(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_input(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_element_input(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_multiple_element_input(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimiter_is_not_provided(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2, 3], None)

    def test_delimiter_is_an_integer(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimiter_is_a_string(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2, 3], "hello")

    def test_input_list_contains_duplicates(self):
        self.assertEqual(intersperse([1, 2, 3, 3, 4], 4), [1, 4, 2, 4, 3, 4])

    def test_input_list_contains_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3, -4], 4), [-1, 4, -2, 4, -3, -4])

if __name__ == '__main__':
    unittest.main()