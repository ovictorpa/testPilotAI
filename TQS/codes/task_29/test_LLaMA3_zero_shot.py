from concatenate_nested import *
import unittest

def concatenate_nested(test_tup1, test_tup2):
    res = test_tup1 + test_tup2
    return (res)

class TestConcatenateNested(unittest.TestCase):

    def test_concatenation_of_two_tuples(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))

    def test_concatenation_of_multiple_tuples(self):
        self.assertEqual(concatenate_nested((1, 2), concatenate_nested((3, 4), (5, 6))), 
                         ((1, 2), (3, 4, 5, 6)))

    def test_concatenation_with_empty_tuple(self):
        self.assertEqual(concatenate_nested((1, 2), ()), (1, 2))

    def test_concatenation_with_single_element_tuple(self):
        self.assertEqual(concatenate_nested((1,), (2, 3)), (1, 2, 3))

if __name__ == '__main__':
    unittest.main()