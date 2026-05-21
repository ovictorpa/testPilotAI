import unittest

from sum_product import sum_product


class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_non_empty_list(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_list_with_zero(self):
        self.assertEqual(sum_product([1, 0, 3, 4]), (8, 12))

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))


if __name__ == '__main__':
    unittest.main()