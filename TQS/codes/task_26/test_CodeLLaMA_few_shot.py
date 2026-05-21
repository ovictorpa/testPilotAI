from max_chain_length import *
class TestMaxChainLength(unittest.TestCase):
    def test_max_chain_length(self):
        arr = [Pair(1, 2), Pair(2, 3), Pair(3, 4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 3)

    def test_max_chain_length_empty(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 0)

    def test_max_chain_length_single_element(self):
        arr = [Pair(1, 2)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_max_chain_length_no_increase(self):
        arr = [Pair(1, 1), Pair(2, 2), Pair(3, 3)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_max_chain_length_negative_values(self):
        arr = [Pair(-1, -2), Pair(-2, -3), Pair(-3, -4)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 1)

    def test_max_chain_length_large_input(self):
        arr = [Pair(i, i+1) for i in range(100)]
        n = len(arr)
        self.assertEqual(max_chain_length(arr, n), 100)