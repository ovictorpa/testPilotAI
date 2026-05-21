import unittest
from collections import Counter
from itertools import chain
from freq_element import freq_element  # Replace 'your_module' with the actual name of the module containing the function

class TestFreqElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_element([]), Counter())

    def test_single_element(self):
        self.assertEqual(freq_element([1]), Counter({1: 1}))

    def test_multiple_elements(self):
        nums = [1, 2, 2, 3, 3, 3]
        expected_result = Counter({1: 1, 2: 2, 3: 3})
        self.assertEqual(freq_element(nums), expected_result)

    def test_duplicate_multiples(self):
        nums = [1, 2, 2, 2, 3, 3, 3]
        expected_result = Counter({1: 1, 2: 3, 3: 3})
        self.assertEqual(freq_element(nums), expected_result)

    def test_negative_numbers(self):
        nums = [-1, -1, 2, 3, 3]
        expected_result = Counter({-1: 2, 2: 1, 3: 2})
        self.assertEqual(freq_element(nums), expected_result)

    def test_floats(self):
        with self.assertRaises(TypeError):
            freq_element([1.0, 2.0])

if __name__ == '__main__':
    unittest.main()