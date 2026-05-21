from decimal_To_Binary import *
import unittest

class TestDecimalToBinary(unittest.TestCase):

    def test_zero_input(self):
        # Arrange
        N = 0
        
        # Act
        result = decimal_To_Binary(N)
        
        # Assert
        self.assertEqual(result, 0)

    def test_positive_int(self):
        # Arrange
        N = 5
        
        # Act
        result = decimal_To_Binary(N)
        
        # Assert
        self.assertEqual(result, 101)

    def test_negative_int(self):
        with self.assertRaises(TypeError):
            # Act and Assert (expecting a TypeError because negative numbers are not handled)
            decimal_To_Binary(-1)

    def test_large_input(self):
        # Arrange
        N = 1024
        
        # Act
        result = decimal_To_Binary(N)
        
        # Assert
        self.assertEqual(result, 1111111000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            # Act and Assert (expecting a TypeError because non-numeric inputs are not handled)
            decimal_To_Binary("hello")

if __name__ == '__main__':
    unittest.main()