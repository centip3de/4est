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
            self.stack.push(node[1])

        elif node[0] == '"':
            self.stack.push(node[1])

        elif node[0] == 'T':
            self.stack.push(node[0])

        elif node[0] == 'F':
            self.stack.push(node[0])

        elif node[0] == 'O':
            self.stack.pop()

        elif node[0] == '.':
            print(self.stack.peek())

        elif node[0] == 'U':
            self.stack.push(self.stack.peek())

        elif node[0] == 'S':
            top = self.stack.pop()
            bot = self.stack.pop()
            self.stack.push(top)
            self.stack.push(bot)

        elif node[0] == '+':
            left = int(self.stack.pop())
            right = int(self.stack.pop())
            self.stack.push(left + right)

        elif node[0] == '-':
            left = int(self.stack.pop())
            right = int(self.stack.pop())
            self.stack.push(left - right)

        elif node[0] == '*':
            left = int(self.stack.pop())
            right = int(self.stack.pop())
            self.stack.push(left * right)

        elif node[0] == '/':
            left = int(self.stack.pop())
            right = int(self.stack.pop())
            self.stack.push(left / right)

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
