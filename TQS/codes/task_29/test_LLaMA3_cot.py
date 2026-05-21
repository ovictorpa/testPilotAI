from concatenate_nested import *
import unittest

def concatenate_nested(test_tup1, test_tup2):
    """Concatenates two tuples into one."""
    res = test_tup1 + test_tup2
    return (res)

class TestConcatenateNested(unittest.TestCase):

    def test_concat_two_tuples(self):
        # Test concatenation of two tuples.
        tup1 = (1, 2, 3)
        tup2 = ('a', 'b')
        expected_result = (1, 2, 3, 'a', 'b')
        
        result = concatenate_nested(tup1, tup2)
        
        # Check if the result is as expected.
        self.assertEqual(result, expected_result)

    def test_concat_tuple_with_empty(self):
        # Test concatenation of a tuple with an empty tuple.
        tup1 = (1, 2, 3)
        tup2 = ()
        expected_result = (1, 2, 3,)
        
        result = concatenate_nested(tup1, tup2)
        
        # Check if the result is as expected.
        self.assertEqual(result, expected_result)

    def test_concat_tuple_with_single_element(self):
        # Test concatenation of a tuple with another tuple that contains one element.
        tup1 = (1, 2, 3)
        tup2 = (4,)
        expected_result = (1, 2, 3, 4)
        
        result = concatenate_nested(tup1, tup2)
        
        # Check if the result is as expected.
        self.assertEqual(result, expected_result)

    def test_concat_tuples_of_different_types(self):
        # Test concatenation of two tuples with different types (not supported).
        tup1 = (1, 2, 3)
        tup2 = ('a', 'b')
        
        with self.assertRaises(TypeError):
            concatenate_nested(tup1, tup2)

if __name__ == '__main__':
    unittest.main()