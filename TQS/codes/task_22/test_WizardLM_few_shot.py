from freq_count import *
import unittest
from collections import Counter

def freq_count(lst):
    return collections.Counter(lst)

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_count([]), Counter())

    def test_single_element_list(self):
        self.assertEqual(freq_count(['a']), Counter({'a': 1}))

    def test_all_same_element(self):
        self.assertEqual(freq_count([1, 1, 1, 1]), Counter({1: 4}))

    def test_mixed_elements(self):
        self.assertEqual(freq_count(['apple', 'banana', 'apple', 'cherry']), Counter({'apple': 2, 'banana': 1, 'cherry': 1}))

    def test_with_duplicates(self):
        self.assertEqual(freq_count(['cat', 'dog', 'cat', 'dog', 'cat']), Counter({'cat': 3, 'dog': 2}))

    def test_case_insensitive(self):
        self.assertEqual(freq_count(['Cat', 'cat', 'DOG']), Counter({'Cat': 1, 'cat': 2, 'DOG': 1}))

    def test_with_none(self):
        self.assertIn('None', freq_count([None, None, 1]))

    def test_with_custom_objects(self):
        class MyObject:
            pass

        my_objects = [MyObject(), MyObject()]
        freq = freq_count(my_objects)
        self.assertEqual(freq[MyObject], 2)

    def test_with_empty_tuple(self):
        self.assertEqual(freq_count((),), Counter())

    def test_with_complex_list(self):
        complex_list = [1, 2.0, 'hello', (1, 2), {1: 2}, lambda: None]
        freq = freq_count(complex_list)
        self.assertEqual(freq, Counter({1: 2, 2.0: 1, 'hello': 1, (1, 2): 1, {1: 2}: 1}))

    def test_with_mixed_types(self):
        mixed_list = [1, 'two', 3, (4, 5), {'six': 7}, None, True]
        freq = freq_count(mixed_list)
        self.assertEqual(freq, Counter({1: 1, 'two': 1, 3: 1, (4, 5): 1, {'six': 7}: 1, None: 1, True: 1}))

if __name__ == '__main__':
    unittest.main()