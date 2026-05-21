from remove_multiple_spaces import *
class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_remove_single_space(self):
        self.assertEqual(remove_multiple_spaces('hello world'), 'hello world')

    def test_remove_no_spaces(self):
        self.assertEqual(remove_multiple_spaces('helloworld'), 'helloworld')

    def test_remove_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces('hello  world     '), 'hello world')

    def test_remove_extra_spaces(self):
        self.assertEqual(remove_multiple_spaces('   hello  world     '), 'hello world')

    def test_remove_mixed_spaces(self):
        self.assertEqual(remove_multiple_spaces('  hello  world  '), 'hello world')

    def test_remove_tabs(self):
        self.assertEqual(remove_multiple_spaces('\thello\t\tworld\t'), 'hello world')

    def test_remove_newlines(self):
        self.assertEqual(remove_multiple_spaces('hello\nworld\n'), 'helloworld')

    def test_remove_carriage_returns(self):
        self.assertEqual(remove_multiple_spaces('hello\rworld\r'), 'helloworld')