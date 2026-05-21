import unittest
from remove_duplicates import remove_duplicates  # Replace 'your_module' with the actual name of the file containing the function

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicates([5]), [5])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 1]), [])

    def test_all_unique_elements(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()