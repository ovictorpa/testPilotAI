from max_chain_length import *
import unittest
from your_module import Pair, max_chain_length  # replace 'your_module' with the actual name of the module where the function is defined

class TestMaxChainLength(unittest.TestCase):

    def test_max_chain_length_single_element(self):
        arr = [Pair(1, 2)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_max_chain_length_two_elements(self):
        arr = [Pair(3, 4), Pair(5, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 2)

    def test_max_chain_length_equal_pairs(self):
        arr = [Pair(1, 1), Pair(1, 1)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 2)

    def test_max_chain_length_different_pairs(self):
        arr = [Pair(1, 5), Pair(4, 3), Pair(6, 7)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_max_chain_length_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_max_chain_length_negative_values(self):
        with pytest.raises(ValueError): # Assuming a check for negative values is implemented
            max_chain_length([Pair(-1, -2)], 1)

if __name__ == '__main__':
    unittest.main()