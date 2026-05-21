from typing import List



def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:

    """

    Filter an input list of strings to include only those that start with the given prefix.

    

    >>> filter_by_prefix([], 'a')

    []

    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')

    ['abc', 'array']

    """

    return [x for x in strings if x.startswith(prefix)]