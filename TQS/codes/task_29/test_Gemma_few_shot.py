from concatenate_nested import *
import unittest

def concatenate_nested(test_tup1, test_tup2):

  res = test_tup1 + test_tup2

  return (res)


class TestConcatenateNested(unittest.TestCase):

    def test_basic(self):
        test_tup1 = (1, 2)
        test_tup2 = (3, 4)
        expected = (1, 2, 3, 4)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected = ()
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected)

    def test_unequal_length(self):
        test_tup1 = (1, 2)
        test_tup2 = (3,)
        with self.assertRaises(ValueError):
            concatenate_nested(test_tup1, test_tup2)