from remove_Occ import *
def test_remove_occ():
    """
    Test the remove_occ function to ensure it works correctly.
    """
    # Test case 1: Remove single occurrence of character
    s = "hello"
    ch = "l"
    expected = "helo"
    assert remove_occ(s, ch) == expected

    # Test case 2: Remove multiple occurrences of character
    s = "hellohello"
    ch = "l"
    expected = "heo"
    assert remove_occ(s, ch) == expected

    # Test case 3: Remove character not in string
    s = "hello"
    ch = "a"
    expected = "hello"
    assert remove_occ(s, ch) == expected

    # Test case 4: Empty string
    s = ""
    ch = "l"
    expected = ""
    assert remove_occ(s, ch) == expected

def test_remove_occ_edge_case():
    """
    Test the remove_occ function to ensure it works correctly for edge cases.
    """
    # Test case 1: String is None
    s = None
    ch = "l"
    with pytest.raises(TypeError):
        remove_occ(s, ch)

    # Test case 2: Character is None
    s = "hello"
    ch = None
    with pytest.raises(TypeError):
        remove_occ(s, ch)

def test_remove_occ_type_error():
    """
    Test the remove_occ function to ensure it raises a TypeError if the input is not a string or character.
    """
    # Test case 1: String is not a string
    s = 123
    ch = "l"
    with pytest.raises(TypeError):
        remove_occ(s, ch)

    # Test case 2: Character is not a character
    s = "hello"
    ch = 123
    with pytest.raises(TypeError):
        remove_occ(s, ch)