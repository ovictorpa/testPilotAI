import unittest

from has_close_elements import has_close_elements


class TestHasCloseElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(has_close_elements([], 0.5))

    def test_single_element_list(self):
        self.assertFalse(has_close_elements([1.0], 0.5))

    def test_no_close_elements(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_close_elements(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_threshold_equal_to_distance(self):
        self.assertTrue(has_close_elements([1.0, 2.0], 1.0))

    def test_threshold_greater_than_distance(self):
        self.assertFalse(has_close_elements([1.0, 2.0], 0.5))


if __name__ == '__main__':
    unittest.main()