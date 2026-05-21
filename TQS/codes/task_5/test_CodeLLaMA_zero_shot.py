from greatest_common_divisor import *
def test_gcd():
    assert greatest_common_divisor(3, 5) == 1

def test_gcd2():
    assert greatest_common_divisor(25, 15) == 5

def test_invalid_input():
    with pytest.raises(ValueError):
        greatest_common_divisor("a", "b")