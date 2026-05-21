from concatenate_nested import *
def concatenate_nested(tup1, tup2):
    return tup1 + tup2

class TestConcatenateNested(unittest.TestCase):
    def test_concatenate_simple_tuples(self):
        tup1 = (1, 2, 3)
        tup2 = (4, 5, 6)
        expected = (1, 2, 3, 4, 5, 6)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_concatenate_with_empty_tuples(self):
        tup1 = ()
        tup2 = (4, 5, 6)
        expected = (4, 5, 6)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)
        tup1 = (1, 2, 3)
        tup2 = ()
        self.assertEqual(concatenate_nested(tup1, tup2), tup1)

    def test_concatenate_with_nested_tuples(self):
        tup1 = ((1, 2), (3, 4))
        tup2 = (5, 6)
        expected = ((1, 2), (3, 4), 5, 6)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_concatenate_tuples_of_different_lengths(self):
        tup1 = (1, 2)
        tup2 = (3, 4, 5)
        expected = (1, 2, 3, 4, 5)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_non_tuple_arguments(self):
        with self.assertRaises(TypeError):
            concatenate_nested('tuple', [1, 2, 3])

    def test_hashable_and_unhashable_types(self):
        # This should raise a TypeError because unhashable types (like lists) cannot be added to tuples
        with self.assertRaises(TypeError):
            concatenate_nested((1, (2, [3])), (4, 5))

    def test_concatenate_with_uneven_tuples(self):
        tup1 = (1, 2)
        tup2 = (3,)
        expected = (1, 2, 3)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_empty_tuple_remains_empty(self):
        tup1 = ()
        tup2 = ()
        expected = ()
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_single_element_tuples(self):
        tup1 = (1,)
        tup2 = (2,)
        expected = (1, 2)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

    def test_mixed_hashable_and_unhashable_tuples(self):
        # This should raise a TypeError because the tuple contains an unhashable type (list)
        with self.assertRaises(TypeError):
            concatenate_nested((1, [2]), (3, 4))

    def test_concatenate_tuples_with_complex_elements(self):
        tup1 = ((1, (2, 3)), (4, 5))
        tup2 = ((6, 7), 8)
        expected = ((1, (2, 3)), (4, 5), (6, 7), 8)
        self.assertEqual(concatenate_nested(tup1, tup2), expected)

if __name__ == '__main__':
    unittest.main()