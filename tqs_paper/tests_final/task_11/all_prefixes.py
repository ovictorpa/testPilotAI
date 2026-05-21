from typing import List



def all_prefixes(string: str) -> List[str]:

    

    """

    Return a list of all prefixes of the input string, from shortest to longest.

    

    >>> all_prefixes('abc')

    ['a', 'ab', 'abc']

    """



    result = []

    for i in range(len(string)):

        result.append(string[:i + 1])

    return result