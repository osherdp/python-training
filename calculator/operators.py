"""The operators supported by the calculator."""

import math
import operator


class Operator:
    """Representation of a single mathematical operator.

    Attributes:
        operation (function): the function that does the operation.
        precedence (int): the priority of the operation.

    Note:
        Precedence determines which operation goes after another.
    """

    def __init__(self, operation, precedence):
        self.operation = operation
        self.precedence = precedence


def average(num1, num2):
    """Return the average of two numbers (int/float)."""
    return float(num1 + num2) / 2.0


"""A dictionary containing the information about supported operations."""
operators = {
    '+': Operator(operator.add, 1),
    '-': Operator(operator.sub, 1),

    '*': Operator(operator.mul, 2),
    '/': Operator(operator.truediv, 2),

    '^': Operator(math.pow, 3),
    '%': Operator(math.fmod, 4),

    '@': Operator(average, 5),
    '$': Operator(max, 5),
    '&': Operator(min, 5),

    '~': Operator(operator.neg, 6),
    '!': Operator(math.factorial, 7),

    '(': Operator(None, 8),
    ')': Operator(None, 8)
}


def is_operator(symbol: str) -> bool:
    """Return true if operation is supported else false."""
    return symbol in operators
