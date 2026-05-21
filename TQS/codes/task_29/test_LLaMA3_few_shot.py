from concatenate_nested import *
import unittest

def concatenate_nested(test_tup1, test_tup2):
    res = test_tup1 + test_tup2
    return (res)

class TestConcatenateNested(unittest.TestCase):

    def test_concatenation(self):
        # Test with tuples of integers
        result = concatenate_nested((1, 2), (3, 4))
        self.assertEqual(result, (1, 2, 3, 4))

    def test_concatenation_with_strings(self):
        # Test with tuples of strings
        result = concatenate_nested(("hello", "world"), ("python", "testing"))
        self.assertEqual(result, ("hello", "world", "python", "testing"))

    def test_concatenation_with_mixed_types(self):
        # Test with tuples containing mixed types
        result = concatenate_nested((1, "a", 2.5), (3, "b", None))
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 6)

    def test_empty_tuples(self):
        # Test concatenation of empty tuples
        result = concatenate_nested((), ())
        self.assertEqual(result,())

    def test_non_tuple_types(self):
        with self.assertRaises(TypeError):
            concatenate_nested("not a tuple", (1, 2))

if __name__ == '__main__':
    unittest.main()