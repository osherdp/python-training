"""Calculator module.

This module allows evaluation of strings which represent mathematical
expressions. The supported operators are declared in operators dictionary.
"""
import math
import operator
import re
from collections import namedtuple
from sys import maxsize

ANY_NUMBER = r"-?\d+(?:\.\d+)?"
USER_MSG = "Enter expression to evaluate (enter 'quit' to exit) >>> "

# higher precedence means the operator stronger (will be done first)
Operator = namedtuple("Operator", ["operation", "precedence", "regex"])

OPERATORS = {
    '+': Operator(precedence=1, operation=operator.add,
                  regex=fr"({ANY_NUMBER})\+({ANY_NUMBER})"),
    '-': Operator(precedence=1, operation=operator.sub,
                  regex=fr"({ANY_NUMBER})-({ANY_NUMBER})"),

    '*': Operator(precedence=2, operation=operator.mul,
                  regex=fr"({ANY_NUMBER})\*({ANY_NUMBER})"),
    '/': Operator(precedence=2, operation=operator.truediv,
                  regex=fr"({ANY_NUMBER})/({ANY_NUMBER})"),

    '^': Operator(precedence=3, operation=math.pow,
                  regex=fr"({ANY_NUMBER})\^({ANY_NUMBER})"),
    '%': Operator(precedence=4, operation=math.fmod,
                  regex=fr"({ANY_NUMBER})%({ANY_NUMBER})"),

    '@': Operator(precedence=5, operation=lambda x, y: (x + y) / 2.0,
                  regex=fr"({ANY_NUMBER})@({ANY_NUMBER})"),
    '$': Operator(precedence=5, operation=max,
                  regex=fr"({ANY_NUMBER})\$({ANY_NUMBER})"),
    '&': Operator(precedence=5, operation=min,
                  regex=fr"({ANY_NUMBER})&({ANY_NUMBER})"),

    '~': Operator(precedence=6, operation=operator.neg,
                  regex=fr"~({ANY_NUMBER})"),
    '!': Operator(precedence=7, operation=math.factorial,
                  regex=fr"({ANY_NUMBER})!"),

    '(': Operator(precedence=maxsize, operation=lambda expr: _evaluate(expr),
                  regex=r"\(([^()]*)\)")
}


def operators_info_by_precedence() -> list:
    """Sort the value of each item in OPERATORS by its priority.

    Returns:
        List of Operator named tuples by priority, strong to weak.
    """
    return sorted(OPERATORS.values(), key=operator.attrgetter("precedence"),
                  reverse=True)


def replace_in_expression(operator_regex: str, expression: str,
                          new_expr: str) -> str:
    """Change the old sub expression to a new one according to pattern.

    Args:
        operator_regex: pattern to find a sub expression of the operator.
        expression: the entire expression.
        new_expr: the expression to put instead of the old one.

    Returns:
        A new whole expression, changed according to pattern.
    """
    old_expression = re.search(operator_regex, expression).group()
    return expression.replace(old_expression, new_expr)


def _evaluate(expression: str) -> float:
    """Calculate the value of a mathematical expression."""
    expression = str(re.sub(r"\s+", "", expression))
    operators_by_precedence = operators_info_by_precedence()

    for operator_info in operators_by_precedence:
        operator_regex = operator_info.regex

        try:
            operands = list(re.search(operator_regex, expression).groups())

        except AttributeError:
            continue

        if operator_info.precedence != maxsize:
            operands = list(map(float, operands))

        result = operator_info.operation(*operands)

        expression = replace_in_expression(
            operator_regex, expression, str(result))

        return _evaluate(expression)
    return float(expression)


def main():
    raw_expression = input(USER_MSG)

    while raw_expression.lower() != "quit":
        print(_evaluate(raw_expression))
        raw_expression = input(USER_MSG)


if __name__ == '__main__':
    main()
