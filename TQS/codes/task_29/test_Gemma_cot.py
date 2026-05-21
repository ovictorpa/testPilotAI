from concatenate_nested import *
import unittest

class TestConcatenateNested(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertEqual(concatenate_nested([], []), ())

    def test_one_empty_tuple(self):
        self.assertEqual(concatenate_nested([], [1, 2, 3]), ([1, 2, 3]))

    def test_different_lengths(self):
        self.assertEqual(concatenate_nested([1, 2], [3, 4]), ([1, 2, 3, 4]))

    def test_equal_length_integers(self):
        self.assertEqual(concatenate_nested([1, 2], [3, 4]), ([1, 2, 3, 4]))

    def test_equal_length_strings(self):
        self.assertEqual(concatenate_nested(['a', 'b'], ['c', 'd']),(['a', 'b', 'c', 'd']))

if __name__ == '__main__':
    unittest.main()