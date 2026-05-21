from sequence import *
import unittest

def sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return sequence(sequence(n-1)) + sequence(n-sequence(n-1))

class TestSequenceFunction(unittest.TestCase):

    def test_base_cases(self):
        self.assertEqual(sequence(1), 1)
        self.assertEqual(sequence(2), 1)

    def testSmallNumbers(self):
        self.assertEqual(sequence(3), 2)
        self.assertEqual(sequence(4), 3)
        self.assertEqual(sequence(5), 5)

    def testLargerNumbers(self):
        self.assertEqual(sequence(10), 33)
        self.assertEqual(sequence(20), 37718051862089993)

if __name__ == '__main__':
    unittest.main()