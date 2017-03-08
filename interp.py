import os.path
import sys
import traceback
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from grako.buffering import Buffer
from forest.parser.generated_grammar import ForestParser
from forest.stack import Stack

class Interpreter():
    def __init__(self, debug=False):
        self.stack = Stack()
        self.debug = debug

    def step(self, node):
        if self.debug:
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
            self.stack.push(left % right)

        elif node[0] == '^':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(pow(left, right))

        elif node[0] == '=':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left == right)

        elif node[0] == '!':
            val = self.stack.pop()
            self.stack.push(not val)

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
            user_input = input("")
            if user_input.isnumeric():
                user_input = int(user_input)

            self.stack.push(user_input)

        elif node[0] == 'C':
            self.stack.clear_stack()

        elif node[0] == '$':
            self.stack.remove_all_but_bot()

        else:
            raise Exception("Not a parsable node: " + node)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Simple code golfing lang.")
    arg_parser.add_argument('--debug', action="store_true", help="enables debug mode")
    args = arg_parser.parse_args()

    parser = ForestParser()
    interp = Interpreter(args.debug)

    while True:
        ui = input("> ")
        if ui == "quit" or ui == "exit":
            break
        else:
            try:
                ast = parser.parse(Buffer(ui, nameguard=False), rule_name='start')

                if args.debug:
                    print("AST:", ast)

                for op in ast:
                    interp.step(op)

                if args.debug:
                    interp.stack.print_stack()

            except Exception as e:
                print("ERROR: " + str(e))
                traceback.print_exc()
