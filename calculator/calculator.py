"""Calculator module.

This module allows evaluation of strings which represent mathematical
expressions. The supported operations are declared in operators dictionary.

Example:
    To use this module, import the evaluate() function:

        from calculator import evaluate

    The parameter of this function is a mathematical expression (str). For
    example, "1 + (3^-2) * (4! - 5$ 2)".
"""

import re
import math
import operator
from sys import maxsize

any_number_regex = r"-?\d+(\.\d+)?"


class Operator:
    """Representation of a single mathematical operator.

    Attributes:
        operation (function): the function that does the operation.
        precedence (int): the priority of the operation.
        regex (str): regex to find a pattern which suits to the operator.

    Note:
        Precedence determines which operation goes after another.
    """

    def __init__(self, operation, precedence, regex):
        self.operation = operation
        self.precedence = precedence
        self.regex = re.compile(regex)


def average(num1, num2):
    """Return the average of two numbers (int/float).

    Note:
        Same as using mean() from statistics module.
    """
    return float(num1 + num2) / 2.0


def remove_spaces(expression: str) -> str:
    """Remove the spaces between characters in a string."""
    return ''.join(expression.split())


def get_sub_expression_by_symbol(symbol: str, expression: str) -> str:
    """Find the sub expression the current operator.

    Args:
        symbol: the current operator symbol.
        expression: the entire expression to search.

    Returns:
         The desired sub expression of the operator. If nothing is found
         returns an empty string.
    """
    match = operators[symbol].regex.search(expression)

    if not match:
        return ""

    return match.group()


def check_operands(func):
    """Check the existence of the operands.

    Args:
        func (function): the function to operate on.

    Returns:
        function: the function wrapper.
    """

    def operands_wrapper(operator_symbol, operands):
        left_operand, right_operand = operands

        if left_operand and right_operand:
            return func(operator_symbol, operands)

        elif not left_operand and right_operand:
            # if any([operator_symbol == "+", operator_symbol == "-"]):
            #     return float(f"{operator_symbol}{right_operand}")
            return func(operator_symbol, [right_operand])

        elif not right_operand and left_operand:
            return func(operator_symbol, [left_operand])

    return operands_wrapper


@check_operands
def calculate_sub_expression(symbol: str, operands: list) -> float:
    """Evaluate an expression.

    Args:
        operands (list): the operands, can be 2 or 1 according to operation.
        symbol (str): a symbol represents the mathematical operation.

    Returns:
        A float, the result of the mathematical operation.

    Note:
        Brackets need a string operand (_evaluate() takes a string) and the
        others a float (factorial and negate).
    """
    if len(operands) == 2:
        return operators[symbol].operation(float(operands[0]),
                                           float(operands[1]))

    operand = operands[0]
    operation_to_do = operators[symbol].operation

    if operation_to_do is not _evaluate:
        operand = float(operands[0])

    return operation_to_do(operand)


def parse_sub_expression(symbol: str, sub_expr: str) -> list:
    """Analyze a sub expression to its operands, by its operator.

    Args:
        symbol: the operator of the sub expression.
        sub_expr: the expression to analyze.

    Returns:
        A list of both operands, left and right.
    """
    parsed_expr = sub_expr.split(symbol)

    if symbol == "(":
        parsed_expr[1] = parsed_expr[1][:-1]  # removes ")"

    return parsed_expr


def has_operations(expression: str) -> bool:
    """Return True if the expression has operations in it else, false."""
    for symbol in get_operators_by_precedence():
        if operators[symbol].regex.search(expression):
            return True

    return False


def _evaluate(expression: str) -> float:
    """Calculate the value of a mathematical expression."""
    for operator_symbol in get_operators_by_precedence():
        if not has_operations(expression):
            return float(expression)

        sub_expression = get_sub_expression_by_symbol(operator_symbol,
                                                      expression)
        if not sub_expression:
            continue

        operands = parse_sub_expression(operator_symbol, sub_expression)
        result = calculate_sub_expression(operator_symbol, operands)

        new_expression = expression.replace(sub_expression, str(result))
        return _evaluate(new_expression)


def evaluate(expression: str) -> float:
    """Evaluates a mathematical equation.

    Note:
        This is a wrapper function used to remove spaces from the given
        expression.
    """
    return _evaluate(remove_spaces(expression))


# dictionary containing the information about supported operations.
operators = {
    '+': Operator(operator.add, 1,
                  fr"{any_number_regex}\+{any_number_regex}"),
    '-': Operator(operator.sub, 1,
                  fr"{any_number_regex}-{any_number_regex}"),

    '*': Operator(operator.mul, 2,
                  fr"{any_number_regex}\*{any_number_regex}"),
    '/': Operator(operator.truediv, 2,
                  fr"{any_number_regex}/{any_number_regex}"),

    '^': Operator(math.pow, 3,
                  fr"{any_number_regex}\^{any_number_regex}"),
    '%': Operator(math.fmod, 4,
                  fr"{any_number_regex}%{any_number_regex}"),

    '@': Operator(average, 5,
                  fr"{any_number_regex}@{any_number_regex}"),
    '$': Operator(max, 5,
                  fr"{any_number_regex}\${any_number_regex}"),
    '&': Operator(min, 5,
                  fr"{any_number_regex}&{any_number_regex}"),

    '~': Operator(operator.neg, 6, fr"~{any_number_regex}"),
    '!': Operator(math.factorial, 7, fr"{any_number_regex}!"),

    '(': Operator(_evaluate, maxsize, r"\([^()]*\)")
}


def get_operators_by_precedence() -> list:
    """Return all supported operators by their priority."""
    return sorted(operators, key=lambda ch: operators[ch].precedence,
                  reverse=True)
