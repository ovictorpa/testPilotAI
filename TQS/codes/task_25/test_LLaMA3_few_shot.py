import unittest
from binomial_Coeff import binomial_Coeff, sum_Of_product  # Replace 'your_module' with actual module name


class TestBinomialCoefficient(unittest.TestCase):

    def test_binomial_coefficient_0(self):
        self.assertEqual(binomial_Coeff(3, 0), 1)
        self.assertEqual(binomial_Coeff(5, 0), 1)
        self.assertEqual(binomial_Coeff(10, 0), 1)

    def test_binomial_coefficient_1(self):
        self.assertEqual(binomial_Coeff(3, 1), 3)
        self.assertEqual(binomial_Coeff(5, 1), 5)
        self.assertEqual(binomial_Coeff(10, 1), 10)

    def test_binomial_coefficient_max_k(self):
        self.assertEqual(binomial_Coeff(5, 4), 5)

    def test_binomial_coefficient_edge_case_n_0(self):
        with self.assertRaises(ValueError):
            binomial_Coeff(0, 3)


class TestSumOfProduct(unittest.TestCase):

    def test_sum_of_product_even_numbers(self):
        self.assertEqual(sum_Of_product(1), 2)
        self.assertEqual(sum_Of_product(2), 6)

    def test_sum_of_product_odd_numbers(self):
        with self.assertRaises(ValueError):
            sum_Of_product(3)


class TestBinomialCoefficientEdgeCases(unittest.TestCase):

    def test_binomial_coefficient_invalid_input_type_n(self):
        with self.assertRaises(TypeError):
            binomial_Coeff("a", 2)
        with self.assertRaises(TypeError):
            binomial_Coeff(5, "b")

    def test_binomial_coefficient_invalid_input_type_k(self):
        with self.assertRaises(TypeError):
            binomial_Coeff(3, "c")
        with self.assertRaises(TypeError):
            binomial_Coeff(5, None)


class TestBinomialCoefficientBoundaryCases(unittest.TestCase):

    def test_binomial_coefficient_small_n(self):
        self.assertEqual(binomial_Coeff(2, 1), 2)
        self.assertEqual(binomial_Coeff(3, 0), 1)

    def test_binomial_coefficient_large_k(self):
        self.assertEqual(binomial_Coeff(5, 4), 5)


if __name__ == '__main__':
    unittest.main()