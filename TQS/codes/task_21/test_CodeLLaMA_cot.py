from sequence import *
import unittest

class TestSequence(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def test_recursive_case(self):
        self.assertEqual(sequence(3), sequence(sequence(2)) + sequence(n-sequence(2)))
        self.assertEqual(sequence(4), sequence(sequence(3)) + sequence(n-sequence(3)))

    def test_edge_cases(self):
        self.assertEqual(sequence(-1), None)
        self.assertEqual(sequence(0), None)
        self.assertEqual(sequence(5), sequence(sequence(4)) + sequence(n-sequence(4)))

if __name__ == '__main__':
    unittest.main()