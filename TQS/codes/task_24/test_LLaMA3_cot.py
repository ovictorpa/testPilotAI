from check_Equality import *
def check_Equality(s):
    """
    Checks if the first and last characters of a given string are equal.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    bool: True if the first and last characters are equal, False otherwise.
    """
    return ord(s[0]) == ord(s[-1])