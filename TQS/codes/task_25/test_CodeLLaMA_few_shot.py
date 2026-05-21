from binomial_Coeff import *
import unittest
from math import comb

class TestBinomialCoeff(unittest.TestCase):
    def test_binomial_coeff(self):
        self.assertEqual(comb(2, 1), 2)
        self.assertEqual(comb(3, 2), 3)
        self.assertEqual(comb(4, 3), 4)
        self.assertEqual(comb(5, 4), 5)