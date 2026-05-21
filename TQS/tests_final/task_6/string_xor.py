def string_xor(a: str, b: str) -> str:

    """

    Perform a binary XOR operation on two strings consisting only of 1s and 0s.

    The result is returned as a string of 1s and 0s.

    

    >>> string_xor('010', '110')

    '100'

    """



    def xor(i: str, j: str) -> str:

        if i == j:

            return '0'

        else:

            return '1'

    

    return ''.join(xor(x, y) for x, y in zip(a, b))