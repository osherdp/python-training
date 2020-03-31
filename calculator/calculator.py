"""Advanced calculator interpreter."""

import re

from operators import operators


def _remove_spaces(expression: str) -> str:
    """Remove the additional spaces from a given expression."""
    return ''.join(expression.split())


def _innermost_parentheses(text: list) -> list:
    """Return the text inside the innermost parenthesis."""
    if all(['(' not in text, ')' not in text]):
        return text

    print(text)

    open_paren = text.index('(')
    close_paren = text.index(')')

    print(open_paren, close_paren)
    print(text)

    return _innermost_parentheses(text[open_paren + 1:close_paren])


def max_depth(s):
    current_max = 0
    max = 0
    n = len(s)

    # Traverse the input string
    for i in range(n):
        if s[i] == '(':
            current_max += 1

            if current_max > max:
                max = current_max
        elif s[i] == ')':
            if current_max > 0:
                current_max -= 1
            else:
                return -1

    # finally check for unbalanced string
    if current_max != 0:
        return -1

    return max


def parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield len(stack), string[start + 1: i]


class Parser:
    """Advanced calculator class."""

    def __init__(self, expression: str):
        self.expression = _remove_spaces(expression)

    def split(self):
        supported_operators = ','.join(operators.keys())
        negative_positive_ints = r'[+-]?\d+'
        negative_positive_floats = negative_positive_ints + r'\.?\d+'

        number_or_symbol = re.compile(
            rf'([{supported_operators}]|{negative_positive_floats}'
            rf'|{negative_positive_ints})')

        return re.findall(number_or_symbol, self.expression)


# source = '((81 * 6) /42+ (3-1))'
source = '((81 * 6) /42+ (3.5-1))'
c = Parser(source)
print(c.split())
# print(_innermost_parentheses(c.split()))
print(max_depth(c.split()))
print(list(parenthetic_contents(source)))
