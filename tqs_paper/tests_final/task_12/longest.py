from typing import List, Optional



def longest(strings: List[str]) -> Optional[str]:

    

    """

    Return the longest string from the list of strings.

    If there are multiple strings with the same maximum length, return the first one.

    Return None if the input list is empty.

    

    >>> longest([])

    None

    >>> longest(['a', 'b', 'c'])

    'a'

    >>> longest(['a', 'bb', 'ccc'])

    'ccc'

    """



    if not strings:

        return None

    

    maxlen = max(len(x) for x in strings)

    for s in strings:

        if len(s) == maxlen:

            return s