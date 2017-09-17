import unittest
from forest.stack import Stack
from forest.interp.operators import SwapOP, ClearStackOP, PopOP, DupOP, ListToStackOP, ReverseStackOP

class StackOperatorTest(unittest.TestCase):
    def setUp(self):
        self.stack = Stack([1, 2])

    def test_swap_op(self):
        left = self.stack.pop()
        right = self.stack.pop()
        out = SwapOP.invoke(left, right, self.stack)
        assert(out[0] == None)
        assert(out[1].mem == [2, 1])

    def test_clear_stack_op(self):
        out = ClearStackOP.invoke(None, None, self.stack)
        assert(out[0] == None)
        assert(out[1].mem == [])

    def test_pop_op(self):
        out = PopOP.invoke(None, None, self.stack)
        assert(out[0] == None)
        assert(out[1].mem == [1])

    def test_dup_op(self):
        out = DupOP.invoke(None, None, self.stack)
        assert(out[0] == None)
        assert(out[1].mem == [1, 2, 2])

    def test_list_to_stack_op(self):
        self.stack = Stack([[1, 2, 3]])
        out = ListToStackOP.invoke(None, None, self.stack)
        assert(out[0] == None)
        assert(len(out[1].mem) == 3)
        assert(out[1].mem[0] == 1)
        assert(out[1].mem[1] == 2)
        assert(out[1].mem[2] == 3)

    def test_reverse_stack_op(self):
        out = ReverseStackOP.invoke(None, None, self.stack)
        assert(out[0] == None)
        assert(out[1].mem[0] == 2)
        assert(out[1].mem[1] == 1)
