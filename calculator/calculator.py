"""Calculator module.

This module allows evaluation of strings which represent mathematical
expressions. The supported operators are declared in operators dictionary.
"""
import re
import math
import operator
from sys import maxsize
from functools import partial
from collections import namedtuple

ANY_NUMBER = r"[-+]?\d+(?:\.\d+)?"

# higher precedence means the operator is stronger (will be done first)
Operator = namedtuple("Operator", ["operation", "precedence", "regex"])

OPERATORS = [
    Operator(precedence=1, operation=operator.add,
             regex=fr"({ANY_NUMBER})\+({ANY_NUMBER})"),
    Operator(precedence=1, operation=operator.sub,
             regex=fr"({ANY_NUMBER})-({ANY_NUMBER})"),
    Operator(precedence=2, operation=operator.mul,
             regex=fr"({ANY_NUMBER})\*({ANY_NUMBER})"),
    Operator(precedence=2, operation=operator.truediv,
             regex=fr"({ANY_NUMBER})/({ANY_NUMBER})"),
    Operator(precedence=3, operation=math.pow,
             regex=fr"({ANY_NUMBER})\^({ANY_NUMBER})"),
    Operator(precedence=4, operation=math.fmod,
             regex=fr"({ANY_NUMBER})%({ANY_NUMBER})"),
    Operator(precedence=5, operation=lambda x, y: (x + y) / 2.0,
             regex=fr"({ANY_NUMBER})@({ANY_NUMBER})"),
    Operator(precedence=5, operation=max,
             regex=fr"({ANY_NUMBER})\$({ANY_NUMBER})"),
    Operator(precedence=5, operation=min,
             regex=fr"({ANY_NUMBER})&({ANY_NUMBER})"),
    Operator(precedence=6, operation=operator.neg,
             regex=fr"~({ANY_NUMBER})"),
    Operator(precedence=7, operation=math.factorial,
             regex=fr"({ANY_NUMBER})!"),
    Operator(precedence=maxsize, operation=lambda expr: evaluate(expr),
             regex=r"\(([^()]*)\)")
]


def evaluate(expression: str) -> float:
    """Calculate the value of a mathematical expression.

    Args:
        expression (str): the entire mathematical expression to calculate.

    Returns:
         float. The calculated result of the given expression.
    """
    expression = expression.replace(" ", "")
    operators_by_precedence = sorted(OPERATORS, reverse=True,
                                     key=operator.attrgetter("precedence"))

    for operator_info in operators_by_precedence:
        operator_regex = operator_info.regex

        search_result = re.search(operator_regex, str(expression))

        if search_result is not None:
            operands = search_result.groups()

            if all(re.fullmatch(ANY_NUMBER, op) for op in operands):
                operands = [float(op) for op in operands]

            operation_result = operator_info.operation(*operands)

            new_sub_expr = str(operation_result)

            if operation_result > 0:
                new_sub_expr = f"+{operation_result}"

            old_expression = search_result.group()
            expression = expression.replace(old_expression, new_sub_expr)

            return evaluate(expression)

    return float(expression)


def main():
    msg_user = "Enter expression to evaluate ('quit' to exit) >>> "

    for expression in iter(partial(input, msg_user), "quit"):
        print(evaluate(expression))


if __name__ == '__main__':
    main()