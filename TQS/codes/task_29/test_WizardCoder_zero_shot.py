from concatenate_nested import *
import unittest

class TestConcatenateNested(unittest.TestCase):
    def test_concatenate_nested(self):
        """
        Test case for concatenating nested tuples.
        """
        test_tup1 = (("a", 1, "b")
        test_tup2 = ("c", 2, "d", 3)
        expected_result = ("a", 1, "b", "c", 2, "d", 3)
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected_result) 

    def test_concatenate_empty_tuples(self):
        """
        Test case for concatenating empty tuples.
        """
        test_tup1 = ()
        test_tup2 = ("c", 2, "d")
        expected_result = ("c", 2, "d")
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected_result)
        
    def test_tuple_with_nested_tuples(self):
        """
        Test case for concatenating tuples with nested tuples.
        """
        test_tup1 = (("a", 1, "b"), ("c", 2)
        test_tup2 = ("d")
        expected_result = ("a", 1, "b", "d")
        self.assertEqual(concatenate_nested(test_tup1, test_tup2), expected_result)
        
    def test_mismatching_tuple_lengths(self):
        """
        Test case for concatenating tuples of different lengths.
        """
        test_tup1 = (("a", 1, "b")
        test_tup2 = ("c", 2, "d", 3, 4)
        with self.assertRaises(TypeError):
            concatenate_nested(test_tup1, test_tup2)
    
if __name__ == '__main__':
    unittest.main()