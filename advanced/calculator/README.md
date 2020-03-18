# Calculator Exercise

## Goals

1. Learning about regular expressions (regex)
2. Recursion
3. Minimal and flexible code

## Introduction

You are about to implement a very advanced calculator, a bit more than a regular pocket calculator.
The calculator will behave very similar to the Python interpreter. All it has to do is getting expressions from the user and calculate their results.

Operations which should be included:

| Addition | Subtraction | Multiplication | Division | Power | Negate | Modulo | Factorial | Average | Max | Min |
|----------|-------------|----------------|----------|-------|--------|--------|-----------|---------|-----|-----|
| +        | -           | *              | /        | ^     | ~      | %      | !         | @       | $   | &   |
| 1        | 1           | 2              | 2        | 3     | 6      | 4      | 7         | 5       | 5   | 5   |

In this table, precedence should be based on the values in the third row. For example, multiplication should be executed before addition, and factorial should be the most "powerful" operator.

The average, max and min operators should get two operands and perform the operation on them. For example:

* 4 @ 2 should return 3, as it's the average between those two values.
* 2 $ 7 should return 7, as 7 is bigger than 2.

Moreover, the calculator should treat parenthesis as yet another operator, where parenthesis should take precendence over all other operators.

## Recommendations & Notes

* Before parsing the string from the user, you should remove all added spaces - they have no meaning in this exercise (you can assume the user won't give you expressions like "1 1+2")
* Calculating the expression should be in a devide-and-conquer method, where in each step other part of the expression is being parsed, taking into account precendence of operations
* When there are no operations to be done, you can just return the result
* **Hightly** recommended: using the `re` module.
* You may assume there are no two operators with the same precedence in the expression without parenthesis between them (e.g. "1 - 2 + 3")
* Parenthesis are an operator, and as such shouldn't be treated differently than other operators in the code.
