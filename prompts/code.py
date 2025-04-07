import math
from typing import Optional

def is_prime(p: int) -> bool:

    if p < 2:
        return False
    for k in range(2, int(math.sqrt(p)) + 1):
        if p % k == 0:
            return False
    return True

def prime_fib(n: int) -> Optional[int]:

    f = [0, 1] 
    prime_fib_count = 0
    
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            prime_fib_count += 1
            if prime_fib_count == n:
                return f[-1]