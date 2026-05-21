from concatenate_nested import *
import unittest

class TestConcatenateNested(unittest.TestCase):

    def test_basic(self):
        test_tup1 = (1, 2, (3, 4))
        test_tup2 = (5, 6, (7, 8))
        expected = (1, 2, (3, 4), 5, 6, (7, 8))
        actual = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(expected, actual)

    def test_empty(self):
        test_tup1 = ()
        test_tup2 = ()
        expected = ()
        actual = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(expected, actual)

    def test_nested(self):
        test_tup1 = (1, 2, (3, 4))
        test_tup2 = (5, 6, (7, 8))
        expected = (1, 2, (3, 4), 5, 6, (7, 8))
        actual = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()