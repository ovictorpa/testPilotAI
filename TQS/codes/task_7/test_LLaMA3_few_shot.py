import unittest
from mean_absolute_deviation import mean_absolute_deviation  # Import the function to test

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            mean_absolute_deviation([])

    def test_single_element_list(self):
        result = mean_absolute_deviation([1.0])
        self.assertAlmostEqual(result, 0.0)

    def test_two_elements_list(self):
        result = mean_absolute_deviation([1.0, 2.0])
        self.assertAlmostEqual(result, 1.5)

    def test_large_number_of_elements(self):
        numbers = [i for i in range(100)]
        result = mean_absolute_deviation(numbers)
        self.assertLessEqual(abs(result - 50.0), 1e-6)  # Small tolerance due to floating point errors

    def test_list_with_duplicates(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        result = mean_absolute_deviation(numbers)
        self.assertAlmostEqual(result, 1.25)

if __name__ == '__main__':
    unittest.main()