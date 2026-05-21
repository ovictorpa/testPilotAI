from remove_duplicates import *
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep the order of the elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] == 1]