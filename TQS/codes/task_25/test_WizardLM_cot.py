import unittest
from binomial_Coeff import binomial_Coeff, sum_Of_product  # Assuming these functions are in a file named 'binomial.py'

class TestBinomialCoeff(unittest.TestCase):
    def test_baseline(self):
        self.assertEqual(binomial_Coeff(5, 0), 1)
        self.assertEqual(binomial_Coeff(5, 3), 10)
        self.assertEqual(binomial_Coeff(5, 5), 1)

    def test_symmetry(self):
        self.assertEqual(binomial_Coeff(6, 2), binomial_Coeff(4, 2))
        self.assertEqual(binomial_Coeff(5, 2), binomial_Coeff(5, 3))

    def test_non_negative_inputs(self):
        for i in range(-10, 10):
            for k in range(-10, 10):
                if i >= 0 and k >= 0:
                    self.assertIn(binomial_Coeff(i, k), [0] * (k + 1))

    def test_large_values(self):
        large_n = 50
        large_k = 20
        self.assertEqual(binomial_Coeff(large_n, large_k), binomial_Coeff(large_n, large_n - large_k))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            binomial_Coeff(-1, 2)
        with self.assertRaises(ValueError):
            binomial_Coeff(3, -1)
        with self.assertRaises(ValueError):
            binomial_Coeff("a", 2)

    def test_recursive_validation(self):
        self.assertEqual(binomial_Coeff(4, 0), 1)
        self.assertEqual(binomial_Coeff(4, 3), binomial_Coeff(4, 1) + binomial_Coeff(4, 2))
        self.assertEqual(binomial_Coeff(4, 4), binomial_Coeff(4, 3))

    def test_performance(self):
        import timeit
        n = 50
        k = 10
        start_time = timeit.default_timer()
        for _ in range(1000):
            binomial_Coeff(n, k)
        end_time = timeit.default_timer()
        elapsed_time = end_time - start_time
        self.assertLess(elapsed_time, 1.0, "Performance test failed for large inputs.")

class TestSumOfProduct(unittest.TestCase):
    def test_sum_of_product(self):
        self.assertEqual(sum_Of_product(1), binomial_Coeff(2, 0))  # nCn-1 = 1 for n >= 1
        self.assertEqual(sum_Of_product(2), binomial_Coeff(4, 1))  # nCn-2 = 2 for n >= 2
        self.assertEqual(sum_Of_product(3), binomial_Coeff(6, 2))  # nCn-3 = 6 for n >= 3
        # Add more test cases as needed to cover different values of `n`

if __name__ == '__main__':
    unittest.main()