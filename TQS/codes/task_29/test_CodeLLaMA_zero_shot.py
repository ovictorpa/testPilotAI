from concatenate_nested import *
def test_concatenate_nested():
    # Test that concatenating two tuples of integers gives a tuple of integers
    assert concatenate_nested((1, 2), (3, 4)) == (1, 2, 3, 4)

    # Test that concatenating a tuple of integers with a tuple of strings gives a tuple of strings
    assert concatenate_nested((1, 2), ("a", "b")) == ("1", "2", "a", "b")

    # Test that concatenating an empty tuple with a non-empty tuple gives the same result as the non-empty tuple
    assert concatenate_nested((), (1, 2)) == (1, 2)

    # Test that concatenating two tuples of different lengths gives an error
    try:
        concatenate_nested((1, 2), (3, 4, 5))
        assert False
    except TypeError:
        assert True