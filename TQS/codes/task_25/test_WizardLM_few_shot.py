from binomial_Coeff import *
import unittest
from typing import List

def binomial_Coeff(n: int, k: int) -> int:
    C = [0] * (k + 1)
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            C[j] = C[j] + C[j - 1]
    return C[k]

class TestBinomialCoeff(unittest.TestCase):
    def test_binomial_coeff_basics(self):
        self.assertEqual(binomial_Coeff(3, 0), 1)
        self.assertEqual(binomial_Coeff(3, 1), 3)
        self.assertEqual(binomial_Coeff(3, 2), 3)
        self.assertEqual(binomial_Coeff(3, 3), 1)
        # Test with k greater than n
        self.assertEqual(binomial_Coeff(2, 3), 0)

    def test_binomial_coeff_negative_k(self):
        self.assertRaises(IndexError, binomial_Coeff, 1, -1)

    def test_binomial_coeff_negative_n(self):
        self.assertRaises(ValueError, binomial_Coeff, -1, 0)

    def test_binomial_coeff_large_values(self):
        self.assertEqual(binomial_Coeff(100, 50), 2985985)

    # Additional edge cases and typical values
    def test_binomial_coeff_edge_cases(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(1, 0), 1)
        self.assertEqual(binomial_Coeff(1, 1), 1)
        self.assertEqual(binomial_Coeff(2, 1), 2)
        self.assertEqual(binomial_Coeff(5, 5), 1)

    def test_binomial_coeff_symmetry(self):
        # Binomial coefficients are symmetric: C(n, k) == C(n, n-k)
        for n in range(6):
            for k in range(n + 1):
                self.assertEqual(binomial_Coeff(n, k), binomial_Coeff(n, n - k))

    def test_binomial_coeff_cyclic_symmetry(self):
        # Binomial coefficients are cyclically symmetric: C(n, k) == C(n+r, k+r) for r >= 0
        for n in range(6):
            for k in range(n + 1):
                self.assertEqual(binomial_Coeff(n, k), binomial_Coeff(n % 5, k % 5))

    def test_binomial_coeff_consistency(self):
        # Check the consistency of the Pascal's triangle using symmetry and cyclic symmetry
        for i in range(10):
            for j in range(i + 1):
                self.assertEqual(binomial_Coeff(i, j), binomial_Coeff(i, i - j))
                self.assertEqual(binomial_Coeff(i, j), binomial_Coeff((i + j) % 5, min(i, j)))

    def test_binomial_coeff_large_n_k(self):
        # Test with large n and k values where the result can be computed directly
        self.assertEqual(binomial_Coeff(10**6, 10**6), 1)

class TestBinomialCoeffPerformance(unittest.TestCase):
    def test_performance_large_n(self):
        n = 20
        for _ in range(1000):
            _ = binomial_Coeff(n, n - 1)
        # Performance check can be added here if needed