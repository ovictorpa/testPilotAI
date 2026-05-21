from TQS.tests_final.task_11.all_prefixes import *
import pytest

def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('a') == ['a']
    assert all_prefixes('') == []