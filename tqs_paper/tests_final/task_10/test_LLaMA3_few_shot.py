import unittest
from sum_product import sum_product  # replace 'your_module' with the actual name of the module containing the function


class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element_list(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_elements_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_non_integer_in_list(self):
        with self.assertRaises(TypeError):
            sum_product([1, 'a', 3])

    def test_negative_numbers_in_list(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_zero_in_list(self):
        self.assertEqual(sum_product([0, 1, 2]), (3, 0))


if __name__ == '__main__':
    unittest.main()