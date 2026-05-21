from TQS.tests_final.task_14.filter_by_prefix import *
class TestFilterByPrefix:
    def test_empty_input(self):
        assert filter_by_prefix([], "a") == []
    
    def test_non_matching_prefix(self):
        assert filter_by_prefix(["abc", "bcd", "cde", "array"], "z") == []
    
    def test_matching_prefix(self):
        assert filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]

if __name__ == "__main__":
    unittest.main()