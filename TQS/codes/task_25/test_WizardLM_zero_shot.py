from binomial_Coeff import *
import unittest
from typing import List

def binomial_Coeff(n: int, k: int) -> int:
    C = [0] * (k + 1)
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            C[j] += C[j - 1]
    return C[k]

def sum_Of_product(n: int) -> int:
    return binomial_Coeff(2 * n, n - 1)

class TestBinomialCoeff(unittest.TestCase):
    def test_binomial_Coeff_basics(self):
        self.assertEqual(binomial_Coeff(0, 0), 1)
        self.assertEqual(binomial_Coeff(3, 0), 1)
        self.assertEqual(binomial_Coeff(3, 1), 3)
        self.assertEqual(binomial_Coeff(3, 2), 3)
        self.assertEqual(binomial_Coeff(3, 3), 1)

    def test_binomial_Coeff_negative_k(self):
        self.assertEqual(binomial_Coeff(5, -1), 0)
        self.assertEqual(binomial_Coeff(5, -2), 0)

    def test_binomial_Coeff_large_values(self):
        self.assertEqual(binomial_Coeff(100, 49), 300300807692)

    def test_binomial_Coeff_invalid_input(self):
        with self.assertRaises(ValueError):
            binomial_Coeff(-1, 1)
        with self.assertRaises(ValueError):
            binomial_Coeff(3, -2)
        with self.assertRaises(ValueError):
            binomial_Coeff(1.5, 1)
        with self.assertRaises(ValueError):
            binomial_Coeff(3, 'a')

class TestSumOfProduct(unittest.TestCase):
    def test_sum_of_product_basics(self):
        self.assertEqual(sum_Of_product(1), 2)
        self.assertEqual(sum_Of_product(2), 28)
        self.assertEqual(sum_Of_product(3), 234)

    def test_sum_of_product_large_value(self):
        # This is a non-trivial case because of the large binomial coefficient
        self.assertEqual(sum_Of_product(10), 1001001)

    def test_sum_of_product_invalid_input(self):
        with self.assertRaises(ValueError):
            sum_Of_product(-1)
        with self.assertRaises(ValueError):
            sum_Of_product(1.5)
        with self.assertRaises(ValueError):
            sum_Of_product('a')

if __name__ == '__main__':
    unittest.main()