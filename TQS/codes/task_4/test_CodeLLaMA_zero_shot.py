from remove_duplicates import *
def test_remove_duplicates():
    # Test case 1:
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    # Test case 2:
    assert remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]) == [1, 2, 3, 4]
    # Test case 3:
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
    # Test case 4:
    assert remove_duplicates([]) == []
    # Test case 5:
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
```
These tests ensure that the `remove_duplicates` function is working correctly for various inputs. The first test case checks that the function returns the expected output when given a list with duplicates. The second test case ensures that the order of the elements in the input and output lists are the same, as required by the function. The third test case checks that the function works correctly when given a list without any duplicates. The fourth test case ensures that the function returns an empty list when given an empty list as input. The fifth test case checks that the function returns a list with only unique elements when given a list with all duplicate elements.