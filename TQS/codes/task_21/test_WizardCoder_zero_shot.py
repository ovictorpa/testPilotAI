from sequence import *
import pytest

def test_sequence():
    assert sequence(1) == 1
    assert sequence(2) == 1
    assert sequence(3) == 1
    assert sequence(4) == 2
    assert sequence(5) == 2
    assert sequence(6) == 5
    assert sequence(7) == 8