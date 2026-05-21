import unittest
from mean_absolute_deviation import mean_absolute_deviation  # Replace 'your_module' with the actual name of the module containing the function

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(ZeroDivisionError, mean_absolute_deviation, [])

    def test_single_element(self):
        result = mean_absolute_deviation([5.0])
        self.assertEqual(result, 0)

    def test_positive_numbers(self):
        result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        self.assertAlmostEqual(result, 1.25)  # Expected MAD for [1.0, 2.0, 3.0, 4.0] is 1.25

    def test_negative_numbers(self):
        result = mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0])
        self.assertAlmostEqual(result, 2.5)  # Expected MAD for [-1.0, -2.0, -3.0, -4.0] is 2.5

    def test_mixed_numbers(self):
        result = mean_absolute_deviation([-1.0, 2.0, 3.0, -4.0])
        self.assertAlmostEqual(result, 2.25)  # Expected MAD for [-1.0, 2.0, 3.0, -4.0] is 2.25

    def test_duplicates(self):
        result = mean_absolute_deviation([1.0, 2.0, 2.0, 2.0])
        self.assertAlmostEqual(result, 0)  # Expected MAD for [1.0, 2.0, 2.0, 2.0] is 0

if __name__ == '__main__':
    unittest.main()