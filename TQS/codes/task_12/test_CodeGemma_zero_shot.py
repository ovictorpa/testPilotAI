import unittest

from longest import longest

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_list(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'c')

    def test_multiple_strings_with_same_length(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()