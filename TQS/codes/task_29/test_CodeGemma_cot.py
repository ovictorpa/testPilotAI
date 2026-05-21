from concatenate_nested import *
import unittest

class TestConcatenateNested(unittest.TestCase):

    def test_basic(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6)
        expected = (1, 2, 3, 4, 5, 6)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected = ()
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_tuple_with_none(self):
        test_tup1 = (1, None, 3)
        test_tup2 = (4, None, 6)
        expected = (1, None, 3, 4, None, 6)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_different_types(self):
        test_tup1 = (1, "a", True)
        test_tup2 = (4.5, "b", False)
        with self.assertRaises(TypeError):
            concatenate_nested(test_tup1, test_tup2)

if __name__ == '__main__':
    unittest.main()