from concatenate_nested import *
import unittest

class TestConcatenateNested(unittest.TestCase):

    def test_concatenate_nested(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6)
        expected_result = (1, 2, 3, 4, 5, 6)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected_result)

    def test_concatenate_nested_empty_tuple(self):
        test_tup1 = ()
        test_tup2 = (1, 2, 3)
        expected_result = (1, 2, 3)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected_result)

    def test_concatenate_nested_different_types(self):
        test_tup1 = (1, 'a', 3.14)
        test_tup2 = ('b', 4, True)
        expected_result = (1, 'a', 3.14, 'b', 4, True)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected_result)

if __name__ == '__main__':
    unittest.main()