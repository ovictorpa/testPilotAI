import pytest
from decimal_To_Binary import decimal_To_Binary

def test_convert():
    assert decimal_To_Binary(0) == 0
    assert decimal_To_Binary(1) == 10
    assert decimal_To_Binary(2) == 100
    assert decimal_To_Binary(3) == 1100
    assert decimal_To_Binary(4) == 1000
    assert decimal_To_Binary(5) == 101
    assert decimal_To_Binary(6) == 1100
    assert decimal_To_Binary(7) == 1111
    assert decimal_To_Binary(8) == 10000