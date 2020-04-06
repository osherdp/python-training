"""Advanced calculator interpreter."""

import re

from operators import operators


def expression_by_inner_parentheses(total_expression: str,
                                    parsed: list) -> list:
    """Parse the given expression by parentheses by most inner parentheses.

    Args:
        total_expression: the expression to parse.
        parsed: list of all parsed expression items, by order of precedence.

    Returns:
        A list of expression items ordered by most inner parentheses.
    """
    non_nested_parentheses = r'\(([^(\)]*)\)'

    if '(' not in total_expression:
        return parsed

    current_inner_parentheses = re.findall(non_nested_parentheses,
                                           total_expression)

    parsed.extend(current_inner_parentheses)

    total_expression = re.sub(non_nested_parentheses, '',
                              total_expression)  # removes already found

    return expression_by_inner_parentheses(total_expression, parsed)


def evaluate_parentheses(expression: str, parsed_expression: list) -> str:
    if not parsed_expression:
        return expression

    current_sub_expression = parsed_expression.pop()

    operator, operator_index = find_operator_in_sub_expression(
        current_sub_expression)

    if not operator and operator_index == -1:
        return expression

    operand1, operand2 = current_sub_expression.split(operator)

    operation_result = evaluate_sub_expression(operator, operand1, operand2)

    new_expression = expression.replace(f"({current_sub_expression})",
                                        str(operation_result))

    return evaluate_parentheses(new_expression, parsed_expression)


def evaluate_sub_expression(operator_symbol, left_operand, right_operand):
    if left_operand and right_operand:
        return operators[operator_symbol].operation(float(left_operand),
                                                    float(right_operand))

    elif not left_operand and right_operand:
        return operators[operator_symbol].operation(float(right_operand))

    elif not right_operand and left_operand:
        return operators[operator_symbol].operation(float(left_operand))


def find_operator_in_sub_expression(sub_expression: str) -> str:
    for potential_operator in operators:
        try:
            operator_index = sub_expression.find(potential_operator)
            return sub_expression[operator_index]

        except ValueError:
            continue

    return ""


def remove_outer_parentheses(expression: str) -> str:
    if all([expression[0] == "(", expression[-1] == ")"]):
        return expression[1:-1]


def remove_spaces(expression: str) -> str:
    return ''.join(expression.split())


class Calculator:
    """Advanced calculator class."""

    def __init__(self, expression: str):
        self.expression = remove_outer_parentheses(remove_spaces(expression))

    def _parse(self, formula):
        parsed_expression = expression_by_inner_parentheses(formula, [])

        return list(filter(None, (expr.strip() for expr in
                                  parsed_expression)))[::-1]  # low to high

    def evaluate(self):
        parentheses_calculation = evaluate_parentheses(
            self.expression, self._parse(self.expression))

        print(parentheses_calculation)

        while "(" in parentheses_calculation:
            parentheses_calculation = evaluate_parentheses(
                self.expression, self._parse(parentheses_calculation))

        print(parentheses_calculation)

# source = '((81 * 6) /42+ (3-1))'
source = '((81 * 6) /42 $ (5*(3.5 @ 7)-1))'
c = Calculator(source)
print(c.evaluate())
