from TQS.tests_final.task_2.how_many_times import *
import pytest

def test_empty():
    assert how_many_times('', 'a') == 0

def test_one():
    assert how_many_times('aaa', 'a') == 3

def test_two():
    assert how_many_times('aaaa', 'aa') == 3