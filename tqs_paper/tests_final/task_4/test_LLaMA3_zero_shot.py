import unittest
from remove_duplicates import remove_duplicates  # Replace 'your_module' with the actual name of the module where the function is defined.

class TestRemoveDuplicates(unittest.TestCase):

    def test_no_duplicates(self):
        numbers = [1, 2, 3]
        expected_result = [1, 2, 3]
        self.assertEqual(remove_duplicates(numbers), expected_result)

    def test_duplicates(self):
        numbers = [1, 2, 3, 2, 4]
        expected_result = [1, 3, 4]
        self.assertEqual(remove_duplicates(numbers), expected_result)

    def test_all_duplicates(self):
        numbers = [1, 1, 1]
        expected_result = []
        self.assertEqual(remove_duplicates(numbers), expected_result)

    def test_empty_list(self):
        numbers = []
        expected_result = []
        self.assertEqual(remove_duplicates(numbers), expected_result)

    def test_single_element(self):
        numbers = [5]
        expected_result = [5]
        self.assertEqual(remove_duplicates(numbers), expected_result)

if __name__ == '__main__':
    unittest.main()