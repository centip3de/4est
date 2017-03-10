from forest.stack import Stack
from forest.interp import Interpreter
from forest.parser.generated_grammar import ForestParser
from grako.buffering import Buffer

class REPL():
    def __init__(self, debug):
        self.debug = debug
        self.stack = Stack()
        self.interp = Interpreter(debug)
        self.parser = ForestParser()

    def start(self):
        while True:
            ui = input("> ")
            if ui == "quit" or ui == "exit":
                break
            else:
                try:
                    ast = self.parser.parse(Buffer(ui, nameguard=False), rule_name='start')

                    if self.debug:
                        print("AST:", ast)

                    self.interp.interpret(ast)

                    if self.debug:
                        self.interp.stack.print_stack()

                except Exception as e:
                    print("ERROR: " + str(e))
                    traceback.print_exc()

