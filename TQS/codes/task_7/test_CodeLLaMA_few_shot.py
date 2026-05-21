from mean_absolute_deviation import *
class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        self.assertEqual(mean_absolute_deviation([1, 2, 3, 4]), 1.0)

def test_mean_absolute_deviation_with_negative_numbers(self):
    self.assertEqual(mean_absolute_deviation([-1, -2, -3, -4]), 1.0)

def test_mean_absolute_deviation_with_decimal_numbers(self):
    self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

def test_mean_absolute_deviation_with_large_input(self):
    numbers = [i for i in range(1000)]
    self.assertEqual(mean_absolute_deviation(numbers), 0.5)

def test_mean_absolute_deviation_with_empty_list(self):
    with self.assertRaises(ValueError):
        mean_absolute_deviation([])