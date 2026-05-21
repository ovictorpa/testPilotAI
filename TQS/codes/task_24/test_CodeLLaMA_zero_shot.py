from check_Equality import *
def test_count_substrings():
    assert count_Substring_With_Equal_Ends("abcde") == 1
    assert count_Substring_With_Equal_Ends("aabbccdde") == 5
    assert count_Substring_With_Equal_Ends("aabbccddee") == 7

def test_count_substrings_empty():
    assert count_Substring_With_Equal_Ends("") == 0

def test_count_substrings_single_char():
    assert count_Substring_With_Equal_Ends("a") == 1

def test_count_substrings_longer_than_str():
    assert count_Substring_With_Equal_Ends("abc", "abcd") == 2