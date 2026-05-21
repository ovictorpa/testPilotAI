from decimal_To_Binary import *
import unittest
from typing import List

def decimal_to_binary(N: float) -> int:
    B_Number = 0
    cnt = 0
    while N != 0:
        rem = int(N % 2)  # Ensure we're dealing with an integer remainder
        c = pow(10, cnt)
        B_Number += rem * c
        N //= 2
        cnt += 1
    return B_Number

class TestDecimalToBinary(unittest.TestCase):
    test_cases: List[tuple] = [
        # Positive integers
        (5, '101'),
        (25, '11001'),
        (1023, '11111011'),
        # Special cases
        (0, '0'),  # Zero should return zero as a string of binary digits
        (1, '1'),   # One should return one as a string of binary digits
        (-1, '1111'),  # Negative integer (two's complement for 3)
        # Large numbers
        (2**63-1, '111111111111111111111111111111'),
        # Floats (truncate decimal part)
        (3.2, '11'),  # Should truncate to 3
        (3.99, '11'),  # Should truncate to 3
        (3.5, '11'),   # Should truncate to 3
        # Invalid inputs should be handled/ignored
        ('not a number', None),
        (float('nan'), None),
        # Binary numbers
        (0b1010, '1010'),
        # Edge cases and boundaries
        (2.0, '10'),  # Should handle as integer representation
        (2.99, '10'),   # Should handle as integer representation
        (-2.0, '1111'),  # Negative integer (two's complement for -1)
        # Boundary of the float to int conversion
        (3.999999999999998, '11'),  # Should truncate to 3
        (-3.999999999999998, '1111111')  # Should be the two's complement of 3
    ]

    def test_decimal_to_binary(self, input_value: float, expected_output: str):
        with self.subTest(input_value=input_value):
            result = decimal_to_binary(input_value)
            self.assertEqual(result, int(expected_output, 2), msg=f"Input: {input_value}, Expected: {expected_output}, Got: {bin(result)}")

    def test_invalid_input(self):
        for invalid in [None, 'not a number', float('nan')]:
            with self.subTest(invalid_input=invalid):
                self.assertIsNone(decimal_to_binary(invalid), msg=f"Invalid input: {invalid}")

    def test_binary_input(self):
        for binary in [0b1010, '1010']:
            with self.subTest(binary_input=binary):
                result = decimal_to_binary(binary)
                self.assertEqual(result, int(binary, 2), msg=f"Input: {binary}, Expected: {binary}, Got: {bin(result)}")

if __name__ == '__main__':
    unittest.main()