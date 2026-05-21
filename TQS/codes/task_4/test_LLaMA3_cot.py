import unittest
from io import StringIO
import sys
from remove_duplicates import remove_duplicates  # Replace 'your_module' with the actual module name

class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element_repeated(self):
        self.assertEqual(remove_duplicates([1, 1]), [1])

    def test_two_elements_with_different_frequencies(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_all_elements_have_same_frequency(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 3]), [])

    def test_negative_numbers_and_zero(self):
        self.assertEqual(remove_duplicates([-1, -2, -2, 0, 0, 1]), [-1])

    def test_large_list(self):
        import random
        large_list = [random.randint(-100, 100) for _ in range(10000)]
        result = remove_duplicates(large_list)
        self.assertEqual(len(result), len(set(large_list)))

if __name__ == '__main__':
    unittest.main()