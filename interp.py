import os.path
import sys
import traceback

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
                traceback.print_exc()

"""
, // Get input
U // Dup input
D0 // Push down 0
= // Compare the input to 0
! // Negate the comparison
I // Iterate until the stack is 0
    O // Pop off that equality
    U // Duplicate the top of the stack so we don't clober shit
    D3 // Push down 3 for comparison
    S // Swap the top two for accurate modulo
    % // Check if the number is divisible by 3, push result on stack
    D0 // Push down 0 for comparison
    = // Pop off the previous 2 and push on equality result
    ? // If the top of the stack is True
        O // Pop off the equality result
        U // Dup the top of the stack so we don't clober
        D5 // Push down 5 for comparison
        % // Modulo the last two numbers (check if divisible by 5)
        S // Swap the top two for accurate modulo
        D0 // Push down 0 for comparison
        = // Perform equality
        ? // If this is also divisible by 5 push "Fizzbuzz"
            O // Pop off the equality result
            "FizzBuzz" // Push FizzBuzz to the top of the stack, to be printed if this is divisible by 3 and 5
        # // If this isn't divisible by 5
            "Fizz" // If this is divisble only by 3, we need to push "Fizz" to the top of the stack
        | // Endif
    # // If this isn't divisible by 3
        O // Pop off the equality result
        U // Dup the top of the stack so we don't clober
        D5 // Push down 5 for comparison
        S // Swap the top two for accurate modulo
        % // Modulo the last two numbers (check if divisible by 5)
        D0 // Push down 0 for comparison
        = // Perform equality
        ? // If this is divisible by 5 push "Buzz"
            O // Pop off the equality result
            "Buzz"
        # // Else
            O // Pop off the equality result
            // Don't push anything, we want to print the number here if it isn't divisible by 5 or 3
        | // End if
    | // End if
    . // Print the output
    $ // Remove all but the bottom of the stack (to clear off everything except the "root" number)
    D1 // Add 1 to subract
    S // Swap so we don't get a negative
    - // Perform the subraction
    U // Dup the result
    D0 // Push down 0
    = // See if the current amount is equal to 0
    ! // Negate the comparison
E // End loop

Minified version:
,UD0=!IOUD3S%D0=?OUD5S%D0=?O"FizzBuzz"#"Fizz"|#OUD5S%D0=?O"Buzz"#O||.$D1S-UD0=!E
"""
