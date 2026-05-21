from remove_Occ import *
def remove_Occ(s, ch):
    return ''.join([c for c in s if c != ch])