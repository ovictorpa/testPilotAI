import unittest
from mean_absolute_deviation import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mean_absolute_deviation([])

    def test_single_element(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)

    def test_multiple_elements(self):
        numbers = [1.0, 2.0, 3.0]
        expected_mad = (abs(1 - 1) + abs(2 - 1) + abs(3 - 1)) / len(numbers)
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad)

    def test_list_with_duplicates(self):
        numbers = [1.0, 2.0, 2.0]
        expected_mad = (abs(1 - 1) + abs(2 - 1) + abs(2 - 1)) / len(numbers)
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad)

    def test_list_with_negative_numbers(self):
        numbers = [-1.0, 0.0, 1.0]
        expected_mad = (abs(-1 - (-1/3)) + abs(0 - (-1/3)) + abs(1 - (-1/3))) / len(numbers)
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad)

    def test_large_list(self):
        numbers = [i for i in range(100)]
        expected_mad = sum(abs(i - sum(numbers) / len(numbers)) for i in numbers) / len(numbers)
        self.assertAlmostEqual(mean_absolute_deviation(numbers), expected_mad)

if __name__ == '__main__':
    unittest.main()