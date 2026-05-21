from max_chain_length import *
import unittest
class TestMaxChainLength(unittest.TestCase):
    def test_case1(self):
        # example inputs
        arr = [Pair(2, 3), Pair(5, 8), Pair(1, 4), Pair(3, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 2) # expected output: 2 (since there are two chains of length 2, [1, 4] and [2, 3])
    
    def test_case2(self):
        arr = [Pair(2, 5), Pair(10, 6), Pair(7, 8)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1) # expected output: 1 (since there is only one chain of length 2, [10, 6])
    
    def test_case3(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0) # expected output: 0 (since there are no chains)
    
    def test_case4(self):
        arr = [Pair(1, 2), Pair(3, 4), Pair(5, 6)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0) # expected output: 0 (since there is only one chain of length 1 [1, 2], [3, 4] and [5, 6])
    
    def test_case5(self):
        arr = [Pair(-1, -2), Pair(7, 8)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0) # expected output: 0 (since there is only one chain of length 1 [-1, -2] and [7, 8])
    
if __name__ == '__main__':
    unittest.main()