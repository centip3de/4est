import abc
from forest.stack import Stack

class Operator:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def invoke(cls, left, right, stack):
        return (None, None)

class ListToStackOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (None, Stack(stack.pop()))

class AndOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left and right, stack)

class AddOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left + right, stack)

class SubOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left - right, stack)

class DivOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left/right, stack)

class ModOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left%right, stack)

class MulOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left*right, stack)

class IncOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left+1, stack)

class DecOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left - 1, stack)

class JoinOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        if type(left) == list:
            return ("".join([str(x) for x in left]), stack)
        else:
            return (str(left).join([str(x) for x in right]), stack)

class ReverseStackOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (None, Stack(stack.mem[::-1]))

class SplitOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        if(right == ""):
            return (list(left), stack)
        return (left.split(right), stack)

class EmptyListOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return ([], stack)

class TruthOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (True, stack)

class FalseOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (False, stack)

class StringOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (str(left), stack)

class IntOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (int(left), stack)

class ExpOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (pow(left, right), stack)

class EqOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left == right, stack)

class NotOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (not left, stack)

class InputOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        string = "" if left else left
        userInput = input(string)
        return (int(userInput) if userInput.isnumeric() else userInput, stack)

class LtOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left < right, stack)

class GtOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left > right, stack)

class OrOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (left or right, stack)

class SwapOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        stack.push(left)
        stack.push(right)
        return (None, stack)

class StackToListOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (stack.mem, stack)

class ClearStackOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        return (None, Stack([]))

class PopOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        stack.pop()
        return (None, stack)

class PrintOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        print(stack.peek())
        return (None, stack)

class DupOP(Operator):
    @classmethod
    def invoke(cls, left, right, stack):
        stack.push(stack.peek())
        return (None, stack)
