#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.buffering import Buffer
from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS, generic_main  # noqa


KEYWORDS = {}


class ForestBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(ForestBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class ForestParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=False,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=ForestBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(ForestParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @graken()
    def _start_(self):

        def block0():
            self._statements_()
        self._positive_closure(block0)

    @graken()
    def _statements_(self):
        with self._choice():
            with self._option():
                self._numeric_stmt_()
            with self._option():
                self._if_stmt_()
            with self._option():
                self._print_stmt_()
            with self._option():
                self._equality_stmt_()
            with self._option():
                self._input_stmt_()
            with self._option():
                self._push_stmt_()
            self._error('no available options')

    @graken()
    def _print_stmt_(self):
        self._token('.')
        self._cut()
        with self._group():
            with self._choice():
                with self._option():
                    self._string_()
                with self._option():
                    self._number_()
                with self._option():
                    self._boolean_()
                with self._option():
                    self._array_()
                with self._option():
                    self._input_stmt_()
                with self._option():
                    self._equality_stmt_()
                with self._option():
                    self._pop_stmt_()
                self._error('no available options')

    @graken()
    def _input_stmt_(self):
        self._token(',')

    @graken()
    def _push_stmt_(self):
        self._token('P')
        self._cut()
        with self._group():
            with self._choice():
                with self._option():
                    self._string_()
                with self._option():
                    self._number_()
                with self._option():
                    self._boolean_()
                with self._option():
                    self._array_()
                with self._option():
                    self._equality_stmt_()
                with self._option():
                    self._input_stmt_()
                with self._option():
                    self._numeric_stmt_()
                self._error('no available options')

    @graken()
    def _numeric_stmt_(self):
        with self._choice():
            with self._option():
                self._add_op_()
            with self._option():
                self._sub_op_()
            with self._option():
                self._div_op_()
            with self._option():
                self._exp_op_()
            with self._option():
                self._mul_op_()
            with self._option():
                self._mod_op_()
            self._error('no available options')

    @graken()
    def _pop_stmt_(self):
        self._token('O')

    @graken()
    def _if_stmt_(self):
        self._if_term_()
        self._else_term_()

    @graken()
    def _if_term_(self):
        self._token('?')
        self._cut()
        with self._group():
            with self._choice():
                with self._option():
                    self._equality_stmt_()
                with self._option():
                    self._boolean_()
                self._error('no available options')
        self._statements_()

    @graken()
    def _else_term_(self):
        self._token('#')
        self._cut()
        with self._group():
            self._statements_()

    @graken()
    def _equality_stmt_(self):
        with self._choice():
            with self._option():
                self._string_()
                self._token('=')
                self._string_()
            with self._option():
                self._pop_stmt_()
                self._token('=')
                self._string_()
            with self._option():
                self._input_stmt_()
                self._token('=')
                self._string_()
            with self._option():
                self._number_()
                self._num_eq_term_()
                self._number_()
            with self._option():
                self._pop_stmt_()
                self._num_eq_term_()
                self._number_()
            with self._option():
                self._input_stmt_()
                self._num_eq_term_()
                self._number_()
            with self._option():
                self._array_()
                self._token('=')
                self._array_()
            with self._option():
                self._pop_stmt_()
                self._token('=')
                self._array_()
            self._error('no available options')

    @graken()
    def _num_eq_term_(self):
        with self._choice():
            with self._option():
                self._token('=')
            with self._option():
                self._token('>')
            with self._option():
                self._token('<')
            self._error('expecting one of: < = >')

    @graken()
    def _add_op_(self):
        self._number_()
        self._token('+')
        self._cut()
        self._number_()

    @graken()
    def _sub_op_(self):
        self._number_()
        self._token('-')
        self._cut()
        self._number_()

    @graken()
    def _div_op_(self):
        self._number_()
        self._token('/')
        self._cut()
        self._number_()

    @graken()
    def _mul_op_(self):
        self._number_()
        self._token('*')
        self._cut()
        self._number_()

    @graken()
    def _mod_op_(self):
        self._number_()
        self._token('%')
        self._cut()
        self._number_()

    @graken()
    def _exp_op_(self):
        self._number_()
        self._token('^')
        self._cut()
        self._number_()

    @graken()
    def _array_(self):
        self._token('[')
        self._cut()

        def block0():
            self._array_term_()
        self._positive_closure(block0)

    @graken()
    def _array_term_(self):
        with self._group():
            with self._choice():
                with self._option():
                    self._number_()
                with self._option():
                    self._string_()
                self._error('no available options')
        self._token(';')

    @graken()
    def _boolean_(self):
        with self._choice():
            with self._option():
                self._token('T')
            with self._option():
                self._token('F')
            self._error('expecting one of: F T')

    @graken()
    def _string_(self):
        self._token('"')
        self._cut()
        self._letter_with_space_()
        self._token('"')

    @graken()
    def _letter_with_space_(self):
        self._pattern(r'[a-zA-Z ]+')

    @graken()
    def _number_(self):
        self._pattern(r'\d+')


class ForestSemantics(object):
    def start(self, ast):
        return ast

    def statements(self, ast):
        return ast

    def print_stmt(self, ast):
        return ast

    def input_stmt(self, ast):
        return ast

    def push_stmt(self, ast):
        return ast

    def numeric_stmt(self, ast):
        return ast

    def pop_stmt(self, ast):
        return ast

    def if_stmt(self, ast):
        return ast

    def if_term(self, ast):
        return ast

    def else_term(self, ast):
        return ast

    def equality_stmt(self, ast):
        return ast

    def num_eq_term(self, ast):
        return ast

    def add_op(self, ast):
        return ast

    def sub_op(self, ast):
        return ast

    def div_op(self, ast):
        return ast

    def mul_op(self, ast):
        return ast

    def mod_op(self, ast):
        return ast

    def exp_op(self, ast):
        return ast

    def array(self, ast):
        return ast

    def array_term(self, ast):
        return ast

    def boolean(self, ast):
        return ast

    def string(self, ast):
        return ast

    def letter_with_space(self, ast):
        return ast

    def number(self, ast):
        return ast


def main(filename, startrule, **kwargs):
    with open(filename) as f:
        text = f.read()
    parser = ForestParser()
    return parser.parse(text, startrule, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    from grako.util import asjson

    ast = generic_main(main, ForestParser, name='Forest')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(asjson(ast), indent=2))
    print()
