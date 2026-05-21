from string_xor import *
def test_string_xor():
    """
    Test the string_xor function by comparing its output with the expected result.
    """
    a = '010'
    b = '110'
    expected = '100'
    actual = string_xor(a, b)
    assert actual == expected, f"string_xor('{a}', '{b}') returned {actual}, but expected {expected}"

def test_string_xor_with_empty_strings():
    """
    Test the string_xor function with empty strings.
    """
    a = ''
    b = ''
    expected = ''
    actual = string_xor(a, b)
    assert actual == expected, f"string_xor('{a}', '{b}') returned {actual}, but expected {expected}"

def test_string_xor_with_different_length_strings():
    """
    Test the string_xor function with strings of different lengths.
    """
    a = '010'
    b = '1101'
    expected = '1001'
    actual = string_xor(a, b)
    assert actual == expected, f"string_xor('{a}', '{b}') returned {actual}, but expected {expected}"

def test_string_xor_with_non_binary_strings():
    """
    Test the string_xor function with non-binary strings.
    """
    a = 'abc'
    b = 'def'
    expected = ''
    actual = string_xor(a, b)
    assert actual == expected, f"string_xor('{a}', '{b}') returned {actual}, but expected {expected}"