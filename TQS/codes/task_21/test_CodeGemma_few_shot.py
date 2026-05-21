from sequence import *
import unittest

def sequence(n): 

	if n == 1 or n == 2: 

		return 1

	else: 

		return sequence(sequence(n-1)) + sequence(n-sequence(n-1)) 

class TestSequence(unittest.TestCase):

    def test_sequence_base_case(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_sequence_recursive_case(self):
        self.assertEqual(sequence(3), 3)
        self.assertEqual(sequence(4), 7)

    def test_sequence_invalid_input(self):
        with self.assertRaises(RecursionError):
            sequence(float('nan'))

if __name__ == '__main__':
    unittest.main()