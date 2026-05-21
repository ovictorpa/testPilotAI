import unittest
from freq_count import freq_count  # Import the module where freq_count is defined

class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_count([]), collections.Counter())

    def test_single_element_list(self):
        self.assertEqual(freq_count([1]), {1: 1})

    def test_multiple_elements_list(self):
        self.assertEqual(freq_count([1, 2, 3, 2, 4, 5, 3]), {1: 1, 2: 2, 3: 2, 4: 1, 5: 1})

    def test_duplicate_counts(self):
        self.assertEqual(freq_count([1, 1, 1]), {1: 3})

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            freq_count([-1, -2, -3])

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            freq_count(['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()