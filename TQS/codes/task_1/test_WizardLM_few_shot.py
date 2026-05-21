import unittest
from typing import List

from intersperse import intersperse  # Replace 'your_module' with the actual module name where the function is defined

class TestInterspersed(unittest.TestCase):
    def test_empty_list(self):
        """Testing an empty list."""
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        """Testing a single element list."""
        self.assertEqual(intersperse([1], 4), [1])

    def test_no_delimiter(self):
        """Testing when delimiter is zero."""
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 2, 3])

    def test_positive_delimiter(self):
        """Testing with a positive integer as delimiter."""
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_negative_delimiter(self):
        """Testing with a negative integer as delimiter."""
        self.assertEqual(intersperse([1, 2, 3], -5), [1, -5, 2, -5, 3])

    def test_mixed_numbers_and_delimiters(self):
        """Testing with a list containing numbers and delimiter."""
        self.assertEqual(intersperse([1, 2, 'a', 3], 4), [1, 4, 'a', 4, 3])

    def test_non_integer_delimiter_raises_typeerror(self):
        """Testing with a non-integer delimiter should raise TypeError."""
        with self.assertRaises(TypeError):
            intersperse([1, 2, 3], '4')

    def test_mixed_data_types(self):
        """Testing with mixed data types in the list."""
        self.assertEqual(intersperse([1, 'hello', 3.5], 0), [1, 0, 'hello', 0, 3.5])

    def test_multiple_delimiters(self):
        """Testing with multiple delimiters."""
        self.assertEqual(intersperse([1, 2, 3, 4], [5, 6]), [1, 5, 2, 6, 3, 5, 4])

    def test_delimiter_list_empty(self):
        """Testing when delimiter list is empty."""
        self.assertEqual(intersperse([1, 2, 3], []), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()