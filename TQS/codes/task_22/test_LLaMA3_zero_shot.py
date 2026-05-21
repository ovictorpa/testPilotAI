import unittest
from freq_count import freq_count  # replace 'your_module' with the actual name of the module where the function is defined

class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_count([]), collections.Counter())

    def test_single_element_list(self):
        self.assertEqual(freq_count([1]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_list_with_duplicates_and_non_unique_elements(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 4, 4, 4]), {1: 1, 2: 2, 3: 3, 4: 3})

    def test_list_with_negative_numbers(self):
        with self.assertRaises(TypeError):
            freq_count([-1, -2, -3])

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            freq_count([1, 'a', 2.5])

if __name__ == '__main__':
    unittest.main()