from enum import Enum

class OPs(Enum):
    PRINT = 1
    INPUT = 2
    ITERATE = 3
    STRING = 4
    NUMBER = 5
    ADD = 6
    SUB = 7
    MUL = 8
    DIV = 9
    MOD = 10
    EXPONENT = 11
    IF = 12
    EQ = 13
    GT = 14
    LT = 15
    RANGE = 16
    SEPARATE = 17
    ARRAY = 18
    ELSE = 19
    LENGTH = 20
    EOL = 21

opsDict = {
    '.': OPs.PRINT,
    ',': OPs.INPUT,
    'I': OPs.ITERATE,
    '"': OPs.STRING,
    'D': OPs.NUMBER,
    '+': OPs.ADD,
    '-': OPs.SUB,
    '*': OPs.MUL,
    '/': OPs.DIV,
    '%': OPs.MOD,
    '^': OPs.EXPONENT,
    '?': OPs.IF,
    '=': OPs.EQ,
    '>': OPs.GT,
    '<': OPs.LT,
    'R': OPs.RANGE,
    '[': OPs.ARRAY,
    ';': OPs.SEPARATE,
    '#': OPs.ELSE,
    'L': OPs.LENGTH,
    '|': OPs.EOL
}

def get_ops(char):
    return opsDict.get(char)
