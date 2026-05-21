from decimal_To_Binary import *
def decimal_to_binary(N):
    B_Number = 0
    cnt = 0
    while N > 0:
        rem = N % 2
        c = 1 << cnt  # equivalent to pow(10, cnt) but more appropriate for binary conversion
        B_Number += rem * c
        N //= 2
        cnt += 1
    return B_Number if B_Number != 0 else '0'  # Return '0' for the number 0