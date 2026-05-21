from how_many_times import *
def test_empty_string():
    assert how_many_times('', 'a') == 0


def test_no_occurrences():
    assert how_many_times('banana', 'z') == 0


def test_one_occurrence():
    assert how_many_times('banana', 'a') == 2


def test_overlapping_occurrences():
    assert how_many_times('bananas', 'ans') == 1