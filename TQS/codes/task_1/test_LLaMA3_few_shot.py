import unittest
from intersperse import intersperse  # replace 'your_module' with the actual name of the module where the function is defined
import pytest

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_multiple_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_negative_numbers(self):
        with pytest.raises(TypeError):
            intersperse([-1, -2, -3], 4)

    def test_non_integer_delimiter(self):
        with pytest.raises(TypeError):
            intersperse([1, 2, 3], 'a')

    def test_invalid_input_type(self):
        with pytest.raises(TypeError):
            intersperse('hello', 4)


if __name__ == '__main__':
    unittest.main()