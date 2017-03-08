import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from grako.buffering import Buffer
from forest.parser.generated_grammar import ForestParser
from forest.stack import Stack

class Interpreter():
    def __init__(self):
        self.stack = Stack()

    def step(self, node):
        self.stack.print_stack()
        if node[0] == 'D':
            self.stack.push(int(node[1]))

        elif node[0] == '"':
            self.stack.push(node[1])

        elif node[0] == 'T':
            self.stack.push(True)

        elif node[0] == 'F':
            self.stack.push(False)

        elif node[0] == 'O':
            self.stack.pop()

        elif node[0] == '.':
            print(str(self.stack.peek()))

        elif node[0] == 'U':
            self.stack.push(self.stack.peek())

        elif node[0] == 'S':
            top = self.stack.pop()
            bot = self.stack.pop()
            self.stack.push(top)
            self.stack.push(bot)

        elif node[0] == '+':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left + right)

        elif node[0] == '-':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left - right)

        elif node[0] == '*':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left * right)

        elif node[0] == '/':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left / right)

        elif node[0] == '%':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left % pop)

        elif node[0] == '^':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(pow(left, right))

        elif node[0] == '=':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left == right)

        elif node[0] == '?':
            if self.stack.peek():
                self.step(node[1])
            else:
                self.step(node[2])

        elif node[0] == '#':
            self.step(node[1])

        elif node[0] == 'I':
            while self.stack.peek():
                for op in node[1]:
                    self.step(op)
            else:
                return

        elif node[0] == 'E':
            return

        else:
            raise Exception("Not a parsable node: " + node)

if __name__ == "__main__":
    parser = ForestParser()
    interp = Interpreter()

    while True:
        ui = input("> ")
        if ui == "quit" or ui == "exit":
            break
        else:
            try:
                ast = parser.parse(Buffer(ui, nameguard=False), rule_name='start')
                print("AST:", ast)

                for op in ast:
                    interp.step(op)

                interp.stack.print_stack()

            except Exception as e:
                print("ERROR: " + str(e))
