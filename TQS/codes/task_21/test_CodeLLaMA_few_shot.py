import unittest
from sequence import sequence

class TestSequence(unittest.TestCase):
    def test_sequence1(self):
        self.assertEqual(sequence(1), 1)

    def test_sequence2(self):
        self.assertEqual(sequence(2), 1)

    def test_sequence3(self):
        self.assertEqual(sequence(3), 3)

    def test_sequence4(self):
        self.assertEqual(sequence(4), 7)

if __name__ == '__main__':
    unittest.main()