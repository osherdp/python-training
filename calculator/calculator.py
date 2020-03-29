"""Advanced calculator interpreter."""

import re

from operators import operators


def _remove_spaces(expression: str) -> str:
    """Remove the additional spaces from a given expression."""
    return ''.join(expression.split())


# def _innermost_parentheses(text: str) -> str:
#     """Return the text inside the innermost parenthesis."""
#     if all(['(' not in text, ')' not in text]):
#         return text
#
#     open_parentheses = text.index('(')
#     close_parentheses = text.index(')')
#     return _innermost_parentheses(text[open_parentheses + 1:close_parentheses])


class Parser:
    """Advanced calculator class."""

    def __init__(self, expression: str):
        self.expression = _remove_spaces(expression)

    def _split(self):
        supported_operators = ','.join(operators.keys())
        negative_positive_ints = r'[+-]?\d+'
        negative_positive_floats = negative_positive_ints + r'\.?\d+'

        number_or_symbol = re.compile(
            rf'([{supported_operators}]|{negative_positive_floats}|{negative_positive_ints})')

        return re.findall(number_or_symbol, self.expression)


# source = '((81 * 6) /42+ (3-1))'
source = '((81 * 6) /42+ (3.5-1))'
c = Parser(source)
print(c._split())
