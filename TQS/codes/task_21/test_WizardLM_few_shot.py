from sequence import *
import unittest

def sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return sequence(sequence(n-1)) + sequence(n-sequence(n-1))

class TestSequence(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)
    
    def test_recursive_calls(self):
        # When n > 2, the function will make recursive calls.
        # We should check that it returns the correct values for these cases as well.
        self.assertEqual(sequence(3), 1)
        self.assertEqual(sequence(4), 5)
        self.assertEqual(sequence(5), 18)
    
    def test_large_n(self):
        # Test with a large value of n to ensure the function can handle it without overflow or error.
        self.assertGreater(sequence(100), 0)
    
    def test_negative_n(self):
        # The function should handle negative values gracefully, although the specification doesn't require this.
        with self.assertRaises(ValueError):
            sequence(-1)
    
    def test_zero(self):
        # According to the specification, the function does not handle zero as a valid input and should raise an error.
        with self.assertRaises(ValueError):
            sequence(0)
    
    def test_non_integer_input(self):
        # The function expects an integer input, so it should handle non-integer inputs by raising an error.
        with self.assertRaises(TypeError):
            sequence('a')
        with self.assertRaises(TypeError):
            sequence(3.5)
    
    def test_large_recursion(self):
        # Test the function with a value of n that will cause it to recursively call itself multiple times.
        # This helps verify that the recursive calls are being made correctly and that the base case eventually terminates.
        self.assertEqual(sequence(6), 194)
    
    def test_consistency(self):
        # Check if the function's output is consistent with its mathematical definition.
        # This is a more complex test and might require some mathematical reasoning or induction to determine the expected result.
        self.assertEqual(sequence(5), 1 + sequence(4) + sequence(1))
        self.assertEqual(sequence(6), 1 + sequence(5) + sequence(2))
        # And so on, until you've covered enough cases to be confident of the function's correctness.

if __name__ == '__main__':
    unittest.main()