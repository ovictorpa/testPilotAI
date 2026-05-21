from binomial_Coeff import *
def test_binomial_coeff():
    # Test with n = 3 and k = 1
    assert binomial_coeff(3, 1) == 3

    # Test with n = 5 and k = 2
    assert binomial_coeff(5, 2) == 10

    # Test with n = 7 and k = 3
    assert binomial_coeff(7, 3) == 35