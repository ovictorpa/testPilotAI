from binomial_Coeff import *
import unittest

class TestBinomialCoeff(unittest.TestCase):

    def test_edge_cases(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)

    def test_symmetry(self):
        for n in range(10):
            for k in range(n + 1):
                self.assertEqual(binomial_Coeff(n, k), binomial_Coeff(n, n-k))

    def test_pascal_identity(self):
        for n in range(10):
            for k in range(n + 1):
                self.assertEqual(binomial_Coeff(n, k) + binomial_Coeff(n, k+1), binomial_Coeff(n+1, k+1))

class TestSumOfProduct(unittest.TestCase):

    def test_n_is_zero(self):
        self.assertEqual(sum_Of_product(0), 1)

    def test_n_is_positive(self):
        for n in range(1, 10):
            self.assertEqual(sum_Of_product(n), binomial_Coeff(2 * n, n - 1))

if __name__ == '__main__':
    unittest.main()