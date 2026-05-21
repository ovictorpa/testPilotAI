import unittest
from sum_product import sum_product  # replace 'your_module' with the actual name of the module where the function is defined

class TestSumProductFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_non_empty_list(self):
        numbers = [1, 2, 3, 4]
        expected_sum = sum(numbers)
        expected_product = 1
        for i in range(1, len(numbers)):
            expected_product *= numbers[i]
        self.assertEqual(sum_product(numbers), (expected_sum, expected_product))

    def test_list_with_zero(self):
        numbers = [0, 2, 3, 4]
        expected_sum = 5
        expected_product = 0
        for i in range(1, len(numbers)):
            expected_product *= numbers[i]
        self.assertEqual(sum_product(numbers), (expected_sum, expected_product))

    def test_list_with_negative_numbers(self):
        numbers = [-1, -2, -3, -4]
        expected_sum = -10
        expected_product = 1
        for i in range(1, len(numbers)):
            expected_product *= numbers[i]
        self.assertEqual(sum_product(numbers), (expected_sum, expected_product))

    def test_list_with_duplicates(self):
        numbers = [2, 2, 3, 4]
        expected_sum = 9
        expected_product = 8
        for i in range(1, len(numbers)):
            expected_product *= numbers[i]
        self.assertEqual(sum_product(numbers), (expected_sum, expected_product))

if __name__ == '__main__':
    unittest.main()