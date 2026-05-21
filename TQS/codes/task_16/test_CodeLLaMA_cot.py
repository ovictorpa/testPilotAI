from remove_Occ import *
def remove_occ(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            s = s[:i] + s[i+1:]
            break
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ch:
            s = s[:i] + s[i+1:]
            break
    return s