from TQS.tests_final.task_8.has_close_elements import *
def test_no_close_elements():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)

def test_close_elements():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)