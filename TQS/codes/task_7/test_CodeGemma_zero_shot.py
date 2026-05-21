import unittest

from mean_absolute_deviation import mean_absolute_deviation


class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), float('nan'))

    def test_single_element_list(self):
        self.assertEqual(mean_absolute_deviation([1]), 0)

    def test_positive_numbers(self):
        self.assertEqual(mean_absolute_deviation([1, 2, 3]), 1)

    def test_negative_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1, -2, -3]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(mean_absolute_deviation([1, -2, 3]), 2)

    def test_large_numbers(self):
        self.assertEqual(mean_absolute_deviation([100, 200, 300]), 100)


if __name__ == '__main__':
    unittest.main()