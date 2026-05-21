import unittest
from collections import Counter
from remove_duplicates import remove_duplicates  # Assuming the function is in this file

class TestRemoveDuplicates(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicicates([1]), [1])

    def test_all_unique_elements(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_some_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])

    def test_mixed_elements(self):
        self.assertEqual(remove_duplicates([1, 1, 'a', 'b', 2, 'a', 2]), [1, 'a', 'b', 2])

    def test_order_preserved(self):
        self.assertEqual(remove_duplicates([3, 1, 2, 2, 4]), [3, 1, 4])

    def test_non_integer_elements(self):
        self.assertEqual(remove_duplicates(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_duplicates_at_start(self):
        self.assertEqual(remove_duplicates([2, 3, 2, 4, 1]), [3, 4, 1])

    def test_duplicates_at_end(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 3, 4]), [1, 2, 4])

    def test_multiple_occurrences_within(self):
        self.assertEqual(remove_duplicates([5, 5, 5, 5, 6]), [6])

    def test_large_list(self):
        large_list = list(range(100))
        unique_list = remove_duplicates(large_list)
        self.assertEqual(len(unique_list), 21)  # There should be 21 unique numbers from 0 to 99

    def test_performance(self):
        import timeit
        large_list = list(range(1000))
        start_time = timeit.default_timer()
        remove_duplicates(large_list)
        end_time = timeit.default_timer()
        self.assertLess((end_time - start_time), 0.5, "The function is too slow for large lists.")

if __name__ == '__main__':
    unittest.main()