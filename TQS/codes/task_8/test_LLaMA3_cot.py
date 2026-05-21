import unittest
from has_close_elements import has_close_elements

class TestHasCloseElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_single_element_list(self):
        self.assertTrue(has_close_elements([1.0], 0.5))  # We can consider a single element to be close to itself
        self.assertFalse(has_close_elements([1.0], 10))  # But not with a large threshold

    def test_no_close_pairs(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 10000))

    def test_close_pair_found(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.5))

    def test_duplicate_elements(self):
        self.assertTrue(has_close_elements([1.0, 1.0, 2.0, 3.0], 0.5))  # Count duplicate elements as separate pairs

    def test_zero_threshold(self):
        self.assertTrue(has_close_elements([-10.0, -9.0], 0))  # Any difference is considered close when threshold is zero

if __name__ == '__main__':
    unittest.main()