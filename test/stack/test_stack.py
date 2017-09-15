import unittest
from forest.stack import Stack

class StackTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack([])

    def test_push(self):
        self.stack.push(10)
        self.stack.push(9)
        self.stack.push(8)
        assert(self.stack.mem == [10, 9, 8])

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(9)
        assert(self.stack.pop() == 9)
        assert(self.stack.pop() == 10)
        assert(self.stack.mem == [])

    def test_peek(self):
        self.stack.push(10)
        self.stack.push(9)
        assert(self.stack.peek() == 9)
        assert(self.stack.mem == [10, 9])

    def test_clear_stack(self):
        self.stack.push(10)
        self.stack.push(9)
        self.stack.clear_stack()
        assert(self.stack.mem == [])

    def test_remove_all_but_bot(self):
        self.stack.push(10)
        self.stack.push(9)
        self.stack.remove_all_but_bot()
        assert(self.stack.mem == [10])
