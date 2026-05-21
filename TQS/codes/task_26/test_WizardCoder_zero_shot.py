from max_chain_length import *
import unittest
from unittest.mock import patch, MagicMock

class TestPair(unittest.TestCase):
    def test_max_chain_length(self):
        # Arrange
        arr = [Pair(2, 1), Pair(3, 4), Pair(5, 6), Pair(7, 8)]
        n = len(arr)

        with patch.object(Pair, '__init__', lambda s, a, b: None):
            # Act
            result = max_chain_length(arr, n)

        # Assert
        self.assertEqual(result, 2) 

if __name__ == "__main__":
    unittest.main()