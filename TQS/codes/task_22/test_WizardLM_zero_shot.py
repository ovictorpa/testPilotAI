from freq_count import *
import unittest
from collections import Counter

def freq_count(list1):
    return collections.Counter(list1)

class TestFreqCountFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_count([]), Counter())

    def test_single_element(self):
        self.assertEqual(freq_count(['a']), Counter({'a': 1}))

    def test_multiple_elements(self):
        self.assertEqual(freq_count(['apple', 'banana', 'apple']), Counter({'apple': 2, 'banana': 1}))

    def test_case_insensitive(self):
        self.assertEqual(freq_count(['apple', 'Banana', 'APPLE']), Counter({'apple': 3}))

    def test_all_elements_same(self):
        self.assertEqual(freq_count([42, 42, 42]), Counter({42: 3}))

    def test_with_duplicates(self):
        self.assertEqual(freq_count(['apple', 'banana', 'apple']), Counter({'apple': 2, 'banana': 1}))

    def test_with_none_values(self):
        self.assertIsInstance(freq_count([None, None, 'orange']), Counter)
        self.assertEqual(freq_count([None, None, 'orange']), Counter({None: 2, 'orange': 1}))

    def test_with_mixed_types(self):
        self.assertEqual(freq_count(['apple', 42, (1, 2), {'key': 'value'}]), Counter({'apple': 1, 42: 1, (1, 2): 1, {'key': 'value'}: 1}))

    def test_performance(self):
        large_list = list(range(1000)) + list(range(1000))  # A list with 2000 integers
        counter = freq_count(large_list)
        self.assertEqual(len(counter), 2)
        self.assertIn(0, counter)
        self.assertIn(1000, counter)

    def test_with_unicode_strings(self):
        self.assertEqual(freq_count(['hello', 'hÃ©llo', 'world']), Counter({'hello': 2, 'hÃ©llo': 1, 'world': 1}))

    def test_with_custom_objects(self):
        class CustomObject:
            def __eq__(self, other):
                return self.attribute == other.attribute
            def __hash__(self):
                return hash(self.attribute)
            def __repr__(self):
                return f'CustomObject({self.attribute})'
            def __init__(self, attribute):
                self.attribute = attribute
        obj1 = CustomObject('test')
        obj2 = CustomObject('test')
        obj3 = CustomObject('other')
        self.assertEqual(freq_count([obj1, obj2, obj3]), Counter({CustomObject('test'): 2, CustomObject('other'): 1}))

if __name__ == '__main__':
    unittest.main()