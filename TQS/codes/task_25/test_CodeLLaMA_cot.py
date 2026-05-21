from binomial_Coeff import *
import unittest

class TestBinomialCoefficients(unittest.TestCase):
    def test_binomial_coefficients(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(2, 1), 2)
        self.assertEqual(binomial_Coeff(3, 2), 6)
        self.assertEqual(binomial_Coeff(4, 3), 10)
        self.assertEqual(binomial_Coeff(5, 4), 10)