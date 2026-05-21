from concatenate_nested import *
import unittest
from typing import Any, List, Tuple

def concatenate_nested(test_tup1: Tuple[Any], test_tup2: Tuple[Any]) -> Tuple[Any]:
    return test_tup1 + test_tup2

class TestConcatenateNested(unittest.TestCase):
    def test_concatenation_of_two_tuples(self):
        # Test with two tuples containing different types of elements
        test_tup1 = ('a', 1, [3, 4])
        test_tup2 = ('b', 2, {'m': 5, 'n': 6})
        expected = ('a', 1, [3, 4], 'b', 2, {'m': 5, 'n': 6})
        self.assertListEqual(list(concatenate_nested(test_tup1, test_tup2)), expected)

    def test_empty_tuples_should_return_empty_tuple(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertListEqual(list(concatenate_nested(test_tup1, test_tup2)), ())

    def test_concatenation_with_single_element_tuples(self):
        test_tup1 = ('first',)
        test_tup2 = ('second', 'third')
        expected = ('first', 'second', 'third')
        self.assertListEqual(list(concatenate_nested(test_tup1, test_tup2)), expected)

    def test_concatenation_with_mixed_types_in_tuples(self):
        test_tup1 = (42, 'hello', [1, 2, 3])
        test_tup2 = ('world', {'key': 'value'}, None)
        expected = (42, 'hello', [1, 2, 3], 'world', {'key': 'value'}, None)
        self.assertListEqual(list(concatenate_nested(test_tup1, test_tup2)), expected)

    def test_concatenation_with_nested_tuples(self):
        test_tup1 = ((1, 2), (3, 4))
        test_tup2 = ((5, 6), (7, 8))
        expected = ((1, 2), (3, 4), (5, 6), (7, 8))
        self.assertListEqual(list(concatenate_nested(test_tup1, test_tup2)), expected)

if __name__ == '__main__':
    unittest.main()