import unittest

from mean_absolute_deviation import mean_absolute_deviation


class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_single_number(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)

    def test_equal_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 1.0, 1.0]), 0.0)

    def test_symmetric_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_asymmetric_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 5.0]), 1.5)


if __name__ == '__main__':
    unittest.main()