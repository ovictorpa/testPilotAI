def greatest_common_divisor(a: int, b: int) -> int:

    

    """

    Return the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.

    

    >>> greatest_common_divisor(3, 5)

    1

    >>> greatest_common_divisor(25, 15)

    5

    """



    while b:

        a, b = b, a % b

    return a