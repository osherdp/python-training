"""Calculator module.

This module allows evaluation of strings which represent mathematical
expressions. The supported operations are declared in operators.py.

Example:
    To use this module, import the evaluate() function:

        from calculator import evaluate

    The parameter of this function is a mathematical expression (str). For
    example, "(1 + (3^-2) * (4! - 5$ 2))". Putting parentheses around the
    entire expression is necessary.

"""

import re

from operators import operators, is_operator


def remove_spaces(expression: str) -> str:
    """Remove the spaces between characters in a string."""
    return ''.join(expression.split())


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
            if any([operator_symbol == "+", operator_symbol == "-"]):
                return float(f"{operator_symbol}{right_operand}")

            return func(operator_symbol, [right_operand])

        elif not right_operand and left_operand:
            return func(operator_symbol, [left_operand])

    return operands_wrapper


def get_inner_parentheses(expression: str) -> str:
    """Return the most inner parentheses in an expression."""
    pattern = re.compile(r"\([^()]*\)")
    without_outer_parentheses = [inner_expr[1:-1] for inner_expr in
                                 pattern.findall(expression)]

    if without_outer_parentheses:
        return without_outer_parentheses[-1]

    return expression


@check_operands
def calculate_sub_expression(operator_symbol, operands):
    """Evaluate an expression.

    Args:
        operands (list): the operands, can be 2 or 1 according to operation.
        operator_symbol (str): a symbol represents the mathematical operation.

    Returns:
        A float, the result of the mathematical operation.
    """
    if len(operands) == 2:
        return operators[operator_symbol].operation(float(operands[0]),
                                                    float(operands[1]))

    return operators[operator_symbol].operation(float(operands[0]))


def get_highest_precedence_operator(expression: str) -> str:
    """Return the highest priority operator in a given expression."""
    without_operands = filter_operands_out(expression)
    return sorted(without_operands, key=lambda ch: operators[ch].precedence,
                  reverse=True)[0]


def filter_operands_out(sub_expression: str) -> list:
    """Remove operands from sub expression, leaves only operators."""
    return [ch for ch in sub_expression if is_operator(ch)]


def parse_sub_expression_by_operator(sub_expression, operator):
    """Analyze a sub expression to its operands, by its operator.

    Args:
        sub_expression (str): the expression to analyze.
        operator (str): the operator of the sub expression.

    Returns:
        A tuple of both operands, left and right.
    """
    any_int_or_float = r"-?\d+(\.\d+)?"

    pattern = re.compile(rf"(?P<left_operand>{any_int_or_float})?\{operator}("
                         rf"?P<right_operand>{any_int_or_float})?")

    matches = pattern.search(sub_expression).groupdict()
    # replace None with ""
    matches = {k: ("" if not v else v) for k, v in matches.items()}

    return matches["left_operand"], matches["right_operand"]


def has_operations(expression: str) -> bool:
    """Return True if the expression has operations in it else, false."""
    return any([True if is_operator(ch) else False for ch in expression])


def is_number(s: str) -> bool:
    """Return true if a string can be a number else, false."""
    try:
        num = float(s)

    except ValueError:
        return False

    return True


def parse_sub_expression(sub_expr: str) -> tuple:
    """Parse an expression according to its highest priority operator.

    Args:
        sub_expr: the part of the expression to parsed.

    Returns:
        The left operand, the operator and the right operand.

    Note:
        The left operand or right operand can be "" if the operator is unary.
    """
    operator = get_highest_precedence_operator(sub_expr)

    left_operand, right_operand = parse_sub_expression_by_operator(
        sub_expr, operator)

    return left_operand, right_operand, operator


def replace_in_expression(old_expr, old_sub_expr, new_sub_expr):
    """Replace sub expression in the entire expression.

    Args:
        old_expr (str): the entire expression.
        old_sub_expr (str): the expression to be replaced.
        new_sub_expr (Str): the new expression to be put in.

    Returns:
        str: the new entire expression.
    """
    if is_number(new_sub_expr):
        return old_expr.replace(f"({old_sub_expr})", new_sub_expr)

    return old_expr.replace(f"{old_sub_expr}", new_sub_expr)


def evaluate(expression: str) -> str:
    """Calculates the value of a mathematical expression."""
    if is_number(expression):
        return expression

    sub_expression = get_inner_parentheses(expression)

    left_operand, right_operand, current_operator = parse_sub_expression(
        sub_expression)

    current_result = calculate_sub_expression(current_operator,
                                              [left_operand, right_operand])

    updated_sub_expression = sub_expression.replace(
        f"{left_operand}{current_operator}{right_operand}",
        str(current_result))

    expression = replace_in_expression(expression, sub_expression,
                                       updated_sub_expression)

    return evaluate(expression)


class Calculator:
    """A class which represents a single calculator.

    Args:
        expression (str): a mathematical expression to evaluate.
            This argument can be with separating spaces.

    Attributes:
        expression (str): the mathematical expression to evaluate.
            Outer parentheses are added in setter.

    Note:
        After the creation of an Calculator instance there is no need to
        create a new one to calculate another expression. Just modify the
        expression property to the new expression.
    """
    def __init__(self, expression=""):
        self.expression = expression

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, expression):
        self._expression = f"({remove_spaces(expression)})"

    def calculate(self):
        return float(evaluate(self._expression))
