from forest.interp.operators import *
from forest.stack import Stack

class Interpreter():
    def __init__(self, debug=False):
        self.stack = Stack()
        self.debug = debug

    def interpret(self, ast):
        for op in ast:
            self.step(op)

    def step(self, node):
        if self.debug:
            print("Current node: " + node[0])
            print(node)
            self.stack.print_stack()

        if node[0] == ']':
            self.stack.push(EmptyListOP.invoke())

        elif node[0] == 'l':
            res, self.stack = ListToStackOP.invoke(None, None, self.stack)

        elif node[0] == 'd':
            left = self.stack.pop()
            res, self.stack = DecOP.invoke(left, None, self.stack)
            self.stack.push(res)

        elif node[0] == 'i':
            left = self.stack.pop()
            res, self.stack = IncOP.invoke(left, None, self.stack)
            self.stack.push(res)

        elif node[0] == 'P':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = SplitOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == 'J':
            left = self.stack.pop()
            if type(left) == list:
                res, self.stack = JoinOP.invoke(left, None, self.stack)
                self.stack.push(res)
            else:
                right = self.stack.pop()
                res, self.stack = JoinOP.invoke(left, right, self.stack)
                self.stack.push(res)

        elif node[0] == 'L':
            res, self.stack = StackToListOP.invoke(self.stack, None, self.stack)
            self.stack.push(res)

        elif node[0].isnumeric():
            res, self.stack = IntOP.invoke(node[0], None, self.stack)
            self.stack.push(res)

        elif node[0] == 'R':
            res, self.stack == ReverseStackOP.invoke(None, None, self.stack)

        elif node[0] == '"':
            string = node[1]
            if(node[1] == '"'):
                string = ""
            res, self.stack = StringOP.invoke(string, None, self.stack)
            self.stack.push(res)

        elif node[0] == 'T':
            res, self.stack = TruthOP.invoke(None, None, self.stack)
            self.stack.push(res)

        elif node[0] == 'F':
            res, self.stack = FalseOP.invoke(None, None, self.stack)
            self.stack.push()

        elif node[0] == 'O':
            res, self.stack = PopOP.invoke(None, None, self.stack)

        elif node[0] == '.':
            res, self.stack = PrintOP.invoke(None, None, self.stack)

        elif node[0] == 'U':
            DupOP.invoke(None, None, self.stack)

        elif node[0] == 'S':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = SwapOP.invoke(left, right, self.stack)

        elif node[0] == '+':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = AddOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '-':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = SubOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '*':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = MulOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '/':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = DivOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '%':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = ModOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '^':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = ExpOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '=':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = EqOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '!':
            left = self.stack.pop()
            res, self.stack = NotOP.invoke(left, None, self.stack)
            self.stack.push(res)

        elif node[0] == '?':
            if self.stack.peek():
                for op in node[1]:
                    self.step(op)
            else:
                self.step(node[2])

        elif node[0] == '#':
            # The two possiblities is an empty else statement
            # or one that has statements. This guard prevents
            # us from trying to execute code that doesn't exist.
            if len(node) >= 2:
                for op in node[1]:
                    self.step(op)

        elif node[0] == 'I':
            # While the value on the top of the stack is True,
            # step through and execute the "inner body"
            while self.stack.peek():
                for op in node[1]:
                    self.step(op)
            else:
                return

        elif node[0] == 'E':
            return

        elif node[0] == ',':
            res, self.stack = InputOP.invoke(None, None, self.stack)
            self.stack.push(res)

        elif node[0] == 'C':
            res, self.stack = ClearStackOP.invoke(None, None, self.stack)

        elif node[0] == '$':
            res, self.stack = AllButButOP.invoke(None, None, self.stack)

        elif node[0] == '<':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = LtOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '>':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = GtOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '|':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = OrOP.invoke(left, right, self.stack)
            self.stack.push(res)

        elif node[0] == '&':
            left = self.stack.pop()
            right = self.stack.pop()
            res, self.stack = AndOP.invoke(left, right, self.stack)
            self.stack.push(res)

        else:
            raise Exception("Not a parsable node: " + node)
