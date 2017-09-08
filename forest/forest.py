import argparse
import sys
import os

# Python is dumb and this is a way to get around their dumbness
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from forest.parser.generated_grammar import ForestParser
from forest.interp import Interpreter
from forest.interp.repl import REPL

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
