import os.path
import sys
import traceback
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Super hacky way to get around Python's shitty import system
for ele in sys.path:
    if '4est/forest' in ele:
        sys.path.remove(ele)

from forest.parser.generated_grammar import ForestParser
from forest.stack import Stack
from forest.interp.repl import REPL
from forest.interp import Interpreter

def main():
    arg_parser = argparse.ArgumentParser(description="Simple code golfing lang.")
    arg_parser.add_argument('--debug', action="store_true", help="enables debug mode")
    arg_parser.add_argument('file', nargs="?", help="4est file to execute")
    args = arg_parser.parse_args()

    parser = ForestParser()

    # If a file hasn't been passed in, then assume this is a REPL session
    if not args.file:
        REPL(args.debug).start()

    else:
        f = open(args.file)
        ast = parser.parse(f.read(), rule_name='start')
        Interpreter(args.debug).interpret(ast)

if __name__ == "__main__":
    main()
