from forest.stack import Stack

class Interpreter():
    def __init__(self, debug=False):
        self.stack = Stack()
        self.debug = debug

    def interpret(self, ast):
        print(ast)
        for op in ast:
            self.step(op)

    def step(self, node):
        if self.debug:
            print("Current node: " + node[0])
            print(node)
            self.stack.print_stack()

        if node[0] == ']':
            self.stack.push([])

        elif node[0] == 'd':
            left = self.stack.pop()
            self.stack.push(left - 1)

        elif node[0] == 'i':
            left = self.stack.pop()
            self.stack.push(left + 1)

        elif node[0] == 'P':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left.split(right))

        elif node[0] == 'J':
            left = self.stack.pop()

            if type(left) == list:
                self.stack.push("".join([str(x) for x in left]))

            else:
                right = self.stack.pop()
                if type(right) == list:
                    self.stack.push(str(left).join(right))

                else:
                    raise Exception("Non compatible types for join were used.")

        elif node[0] == 'L':
            stackList = []
            for i in range(len(self.stack.mem)):
                stackList.append(self.stack.pop())

            self.stack.push(stackList[::-1])

        elif node[0] == 'D':
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

        elif node[0] == '<':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left < right)

        elif node[0] == '>':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left > right)

        elif node[0] == '|':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left or right)

        elif node[0] == '&':
            left = self.stack.pop()
            right = self.stack.pop()
            self.stack.push(left and right)

        else:
            raise Exception("Not a parsable node: " + node)


