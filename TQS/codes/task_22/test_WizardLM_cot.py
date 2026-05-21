import unittest
from collections import Counter
from freq_count import freq_count  # Assuming freq_count is defined in 'your_script.py'

class TestFreqCount(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(freq_count([1, 2, 3, 2]), Counter({1: 1, 2: 2, 3: 1}))

    def test_empty_list(self):
        self.assertEqual(freq_count([]), Counter())

    def test_single_element(self):
        self.assertEqual(freq_count(['a']), Counter({'a': 1}))

    def test_duplicate_elements(self):
        self.assertEqual(freq_count(['apple', 'banana', 'apple', 'cherry', 'banana']), Counter({'apple': 2, 'banana': 2, 'cherry': 1}))

    def test_mixed_types(self):
        self.assertEqual(freq_count([42, 'hello', 3.14, [1, 2, 3]]), Counter({42: 1, 'hello': 1, 3.14: 1, [1, 2, 3]: 1}))

    def test_large_dataset(self):
        large_list = list(range(1000))
        counter = Counter(large_list)
        self.assertEqual(freq_count(large_list), counter)

    def test_none_type(self):
        self.assertEqual(freq_count([None, 'hello', 42]), Counter({None: 1, 'hello': 1, 42: 1}))

    def test_non_hashable_types(self):
        with self.assertRaises(TypeError):
            freq_count([{'key': 'value'}, [1, 2, 3]])

    def test_nested_lists(self):
        self.assertEqual(freq_count([[1, 2], [3, 4]]), Counter({(1, 2): 1, (3, 4): 1}))

    def test_large_frequency_counts(self):
        large_counter = Counter({'item': 999999999})
        self.assertEqual(freq_count(['item'] * 99999999), large_counter)

    def test_performance_consistency(self):
        # This is a performance test rather than an equality test
        import timeit
        small_list = [i for i in range(100)]
        large_list = [i for i in range(10000)]
        
        small_count = freq_count(small_list).mapping
        large_count = freq_count(large_list).mapping
        
        self.assertTrue((small_count == large_count.most_common(1)[0][1]) or (small_count == large_count.most_common(-1)[-1][1]))
        time_small = timeit.timeit(lambda: freq_count(small_list).mapping, number=100)
        time_large = timeit.timeit(lambda: freq_count(large_list).mapping, number=100)
        self.assertGreaterEqual(time_large, time_small)

if __name__ == '__main__':
    unittest.main()