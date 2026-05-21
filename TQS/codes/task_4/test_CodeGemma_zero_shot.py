import unittest

from remove_duplicates import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_with_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_with_multiple_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4]), [1, 4])


if __name__ == '__main__':
    unittest.main()