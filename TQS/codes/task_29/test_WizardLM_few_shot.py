from concatenate_nested import *
def concatenate_nested(tup1, tup2):
    return tup1 + tup2

class TestConcatenateNested(unittest.TestCase):
    def test_concatenate_two_tuples(self):
        tup1 = (1, 2, 3)
        tup2 = (4, 5)
        expected = (1, 2, 3, 4, 5)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_concatenate_empty_tuple_and_non_empty(self):
        tup1 = ()
        tup2 = (7, 8, 9)
        expected = (7, 8, 9)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_concatenate_tuples_with_common_element(self):
        tup1 = ('a', 'b', 'c')
        tup2 = ('c', 'd', 'e')
        expected = ('a', 'b', 'c', 'd', 'e')
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_concatenate_tuples_with_mixed_hashable_unhashable(self):
        from collections import namedtuple
        Person = namedtuple('Person', ['name', 'age'])
        tup1 = (Person('Alice', 30), Person('Bob', 25))
        tup2 = (Person('Charlie', 35),)
        expected = (Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35))
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_empty_tuple_plus_empty_tuple(self):
        tup1 = ()
        tup2 = ()
        expected = ()
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_non_empty_tuple_plus_empty_tuple(self):
        tup1 = (10, 20, 30)
        tup2 = ()
        expected = (10, 20, 30)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_duplicates_in_input_tuples(self):
        tup1 = (1, 2, 2)
        tup2 = (2, 3)
        expected = (1, 2, 2, 2, 3)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_concatenating_single_element_tuples(self):
        tup1 = (42,)
        tup2 = (99,)
        expected = (42, 99)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

if __name__ == '__main__':
    unittest.main()