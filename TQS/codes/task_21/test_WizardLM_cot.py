from sequence import *
import unittest

def sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return sequence(sequence(n-1)) + sequence(n-sequence(n-1))

class TestSequenceFunction(unittest.TestCase):
    def test_base_case_1(self):
        self.assertEqual(sequence(1), 1)
    
    def test_base_case_2(self):
        self.assertEqual(sequence(2), 1)
    
    def test_recursive_behavior(self):
        # This should compute the sequence for n=3, n=4, etc., recursively.
        # We can test a few levels to ensure it's working correctly.
        self.assertEqual(sequence(3), 1)  # n=2, then recursive calls to n=1
        self.assertEqual(sequence(4), 2)  # n=3, then recursive calls to n=2 and n=1
        self.assertEqual(sequence(5), 5)  # n=4, then recursive calls to n=3, n=2, n=1
    
    def test_large_values(self):
        # Test the function with a large value of `n` that shouldn't cause a stack overflow.
        self.assertEqual(sequence(100), 140209547963)
    
    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            sequence("not an integer")
    
    def test_negative_and_zero_values(self):
        # The function does not handle negative or zero values, which might lead to errors.
        with self.assertRaises(ValueError):
            sequence(-1)
        with self.assertRaises(ValueError):
            sequence(0)
    
    def test_consistency(self):
        # Test that the function gives consistent results for the same input.
        result = sequence(3)
        self.assertEqual(sequence(3), result)
    
    def test_performance(self):
        import timeit
        n = 10000
        start_time = timeit.default_timer()
        _ = sequence(n)
        end_time = timeit.default_timer()
        self.assertLess(end_time - start_time, 5, msg=f"sequence function took too long for n={n}")

if __name__ == '__main__':
    unittest.main()