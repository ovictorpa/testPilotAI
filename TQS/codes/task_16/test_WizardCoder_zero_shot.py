from remove_Occ import *
def remove_occ(s, ch):
    """This function will remove all occurrences of a given character from the string s"""
    return s.replace(ch, '')

# Unit Test Cases for remove_Occ Function
def test_remove_occ():
    assert remove_occ('hello', 'l') == 'heo'  #Test Case 1
    assert remove_occ('World', 'r') == 'Wod'  #Test Case 2
    assert remove_occ('abc', 'a') == 'bc'  #Test Case 3
    assert remove_occ('xyz', 'z') == 'xy'  #Test Case 4
    assert remove_occ('', 'z') == ''   #Test Case 5