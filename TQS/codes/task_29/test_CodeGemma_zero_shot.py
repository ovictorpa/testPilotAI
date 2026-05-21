from concatenate_nested import *
import unittest

class TestConcatenateNested(unittest.TestCase):

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        result = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(result, ())

    def test_non_empty_tuples(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6)
        result = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(result, (1, 2, 3, 4, 5, 6))

    def test_mixed_types(self):
        test_tup1 = (1, 'a', 3.14)
        test_tup2 = ('b', 5, True)
        result = concatenate_nested(test_tup1, test_tup2)
        self.assertEqual(result, (1, 'a', 3.14, 'b', 5, True))

if __name__ == '__main__':
    unittest.main()