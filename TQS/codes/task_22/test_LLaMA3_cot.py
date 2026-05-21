import unittest
from collections import Counter
from freq_count import freq_count  # Replace 'your_module' with the actual module name

class TestFreqCountFunction(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(freq_count([1, 2, 2, 3]), Counter({1: 1, 2: 2, 3: 1}))

    def test_empty_list(self):
        self.assertEqual(freq_count([]), Counter())

    def test_single_element(self):
        self.assertEqual(freq_count([5]), Counter({5: 1}))

    def test_duplicate_elements(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3]), Counter({1: 1, 2: 2, 3: 2}))

    def test_empty_string_input(self):
        with self.assertRaises(TypeError):
            freq_count('')

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            freq_count(123)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            freq_count(None)

if __name__ == '__main__':
    unittest.main()