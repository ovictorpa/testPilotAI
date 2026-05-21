import unittest
from freq_element import freq_element  # Replace 'your_module' with the actual name of the module containing the function.

class TestFreqElementFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_element([]), Counter())

    def test_single_element_list(self):
        nums = [1]
        expected_result = Counter({1: 1})
        self.assertEqual(freq_element(nums), expected_result)

    def test_multiple_elements_with_same_frequency(self):
        nums = [1, 2, 3, 2, 1]
        expected_result = Counter({1: 2, 2: 2, 3: 1})
        self.assertEqual(freq_element(nums), expected_result)

    def test_multiple_elements_with_different_frequencies(self):
        nums = [1, 2, 3, 4, 5]
        expected_result = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
        self.assertEqual(freq_element(nums), expected_result)

    def test_list_with_duplicates(self):
        nums = [1, 2, 2, 3]
        expected_result = Counter({1: 1, 2: 2, 3: 1})
        self.assertEqual(freq_element(nums), expected_result)

if __name__ == '__main__':
    unittest.main()