import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from grako.buffering import Buffer
from forest.parser.generated_grammar import ForestParser
from forest.stack import Stack

class Interpreter():
    def __init__(self):
        self.stack = Stack()

    def step(self, ast):
        op = ast[0]

        # Embedded command, process
        if isinstance(op, list):
            print("Found embedded command {}, following".format(op))
            return self.step(ast[0])

        if op == '.':
            to_print = ""
            if ast[1] == 'O':
                to_print = self.stack.pop()

            elif ast[1] == '"':
                i = 2
                while ast[i] != '"':
                    to_print += ast[i]
                    i += 1

            elif ast[1] == "T":
                to_print = "true"

            elif ast[1] == "F":
                to_print = "false"

            # Assume it's an integer now
            elif ast[1].isnumeric():
                    to_print = ast[1]
            else:
                raise Exception("Couldn't find a valid thing to print.")

            print("Result: " + to_print)
            return to_print

        elif op == 'P':
            to_push = ""
            if ast[1] == '"':
                i = 2
                while ast[i] != '"':
                    to_push += ast[i]
                    i += 1

            elif ast[1].isnumeric():
                to_push = ast[1]

            elif ast[1] == "T":
                to_push = "true"

            elif ast[1] == "F":
                to_push = "false"

            else:
                raise Exception("Couldn't find a valid thing to push.")

            self.stack.push(to_push)
            self.stack.print_stack()
            return to_push

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
            except Exception as e:
                print(e)
