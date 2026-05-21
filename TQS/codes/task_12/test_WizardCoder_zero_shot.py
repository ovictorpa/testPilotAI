from longest import *
def test_longest():
    assert longest([]) == None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['abcde', 'fghij', 'klmno', 'pqrstu']) == 'pqrstu'
    assert longest(['ab', 'cd', 'efg', 'hij'] == 'fg'
    
test_longest()