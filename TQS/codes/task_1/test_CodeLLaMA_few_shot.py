from intersperse import *
def test_intersperse_empty_list():
    assert intersperse([], 4) == []


def test_intersperse_single_element_list():
    assert intersperse([1], 4) == [1]


def test_intersperse_double_element_list():
    assert intersperse([1, 2], 4) == [1, 4, 2]


def test_intersperse_triple_element_list():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]


def test_intersperse_multiple_delimiter():
    assert intersperse([1, 2, 3, 4, 5], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5]


def test_intersperse_negetive_delimiter():
    assert intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]


def test_intersperse_large_list():
    numbers = list(range(100))
    delimiter = 4
    result = intersperse(numbers, delimiter)
    assert result == [numbers[0]] + [delimiter] * (len(numbers) - 2) + [numbers[-1]]


def test_intersperse_edge_case():
    numbers = [-1, 0, 1]
    delimiter = 4
    result = intersperse(numbers, delimiter)
    assert result == [-1, 4, 0, 4, 1]


def test_intersperse_with_none():
    numbers = [None, None, None]
    delimiter = 4
    result = intersperse(numbers, delimiter)
    assert result == [None, 4, None, 4, None]


def test_intersperse_with_float():
    numbers = [1.5, 2.7, 3.9]
    delimiter = 4
    result = intersperse(numbers, delimiter)
    assert result == [1.5, 4, 2.7, 4, 3.9]


def test_intersperse_with_complex():
    numbers = [1+2j, 2-3j, 3+4j]
    delimiter = 4
    result = intersperse(numbers, delimiter)
    assert result == [1+2j, 4, 2-3j, 4, 3+4j]


def test_intersperse_with_string():
    numbers = ['a', 'b', 'c']
    delimiter = 'd'
    result = intersperse(numbers, delimiter)
    assert result == ['a', 'd', 'b', 'd', 'c']


def test_intersperse_with_list():
    numbers = [['a'], ['b'], ['c']]
    delimiter = ['d']
    result = intersperse(numbers, delimiter)
    assert result == [['a'], ['d'], ['b'], ['d'], ['c']]