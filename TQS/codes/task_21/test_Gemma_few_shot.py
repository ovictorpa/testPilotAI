from sequence import *
import unittest

class TestSequence(unittest.TestCase):

    def test_sequence_1(self):
        self.assertEqual(sequence(1), 1)

    def test_sequence_2(self):
        self.assertEqual(sequence(2), 1)

    def test_sequence_3(self):
        self.assertEqual(sequence(3), 2)

    def test_sequence_4(self):
        self.assertEqual(sequence(4), 3)

    def test_sequence_5(self):
        self.assertEqual(sequence(5), 5)

    def test_sequence_large(self):
        self.assertEqual(sequence(10), 55)


if __name__ == '__main__':
    unittest.main()