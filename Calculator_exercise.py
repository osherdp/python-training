"""Calculator exercise"""

import re


def add(peace):
    """Solve all '+' in the expression.

    Send the result back to get replaced by old unsolved expression.

    Args:
        peace (str): The expression from 'subtract'.

    Returns: str - The fully-solved expression received.
    """

    matches = re.findall(r'-?\d+\+-?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            matches2 = re.findall(r'-?\d+', match)
            peace = peace.replace(match,
                                  str(int(matches2[0]) + int(matches2[1])))
        return add(peace)

    else:  # No more '+' -
        return peace


def subtract(peace):
    """solve all '-' in expression and send it to add.

    Args:
        peace (str): The expression from 'multiply'.

    Returns: str - The return from the add function.
    """

    matches = re.findall(r'-?\d+--?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            double_minus = re.findall(r'--', match)
            if len(double_minus) > 0:
                matches2 = re.findall(r'-?\d+', match)
                peace = peace.replace(match,
                                      str(int(matches2[0]) - int(matches2[1])))

            else:
                matches2 = re.findall(r'\d+', match)
                peace = peace.replace(match,
                                      str(int(matches2[0]) - int(matches2[1])))
        return subtract(peace)

    else:  # No more '-' -
        return add(peace)


def multiply(peace):
    """solve all '*' and send expression to subtract.

    Args:
        peace (str): The expression from 'divide'.

    Returns: str - The return from the subtract function.
    """

    matches = re.findall(r'-?\d+\*-?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            matches2 = re.findall(r'-?\d+', match)
            peace = peace.replace(match,
                                  str(int(matches2[0]) * int(matches2[1])))
        return multiply(peace)

    else:  # No more '*' -
        return subtract(peace)


def divide(peace):
    """solve all '/' in the expression and send to multiply.

    Args:
        peace (str): The expression from 'power'.

    Returns: str - The return from the multiply function.
    """

    matches = re.findall(r'-?\d+/-?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            matches2 = re.findall(r'-?\d+', match)
            if matches2[1] != '0':
                peace = peace.replace(match, str(
                    int(matches2[0]) / int(matches2[1])))

            else:
                print("Cannot divide by zero!")
                main()

        return divide(peace)

    else:  # No more '/' -
        return multiply(peace)


def power(peace):
    """solve the '^' in the expression and send it to divide.

    Args:
        peace (str): The expression from 'modulo'.

    Returns: str - The return from the divide function.
    """

    matches = re.findall(r'-?\d+\^-?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            matches2 = re.findall(r'-?\d+', match)
            peace = peace.replace(match,
                                  str(int(matches2[0]) ** int(matches2[1])))
        return power(peace)

    else:  # No more '^' -
        return divide(peace)


def modulo(peace):
    """Find the remainder of num/num2 and send the expression to power.

    Args:
        peace (str): The expression from 'minimum'.

    Returns: str - The return from the power function.
    """

    matches = re.findall(r'-?\d+%-?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            matches2 = re.findall(r'-?\d+', match)
            peace = peace.replace(match,
                                  str(int(matches2[0]) % int(matches2[1])))
        return modulo(peace)

    else:  # No modulo left -
        return power(peace)


def minimum(peace):
    """Find the smaller number of the two and send the expression to modulo.

    Args:
        peace (str): The expression from 'maximum'.

    Returns: str - The return from the modulo function.
    """

    matches = re.findall(r'-?\d+&-?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            matches2 = re.findall(r'-?\d+',  match)
            int_matches = [int(x) for x in matches2]
            peace = peace.replace(match, str(min(int_matches)))
        return minimum(peace)

    else:  # No more '&' -
        return modulo(peace)


def maximum(peace):
    """Find the larger number between the two and send expression to minimum.

    Args:
        peace (str): The expression from 'average'.

    Returns: str - The return from the minimum function.
    """

    matches = re.findall(r'-?\d+\$-?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            matches2 = re.findall(r'-?\d+', match)
            int_matches = [int(x) for x in matches2]
            peace = peace.replace(match, str(max(int_matches)))
        return maximum(peace)

    else:  # No more '$' -
        return minimum(peace)


def average(peace):
    """Find the average of two numbers and send the expression to maximum.

    Args:
        peace (str): The expression from 'negate'.

    Returns: str - The return from the maximum function.
    """

    matches = re.findall(r'-?\d+@-?\d+', peace)
    if len(matches) > 0:
        for match in matches:
            matches2 = re.findall(r'-?\d+', match)
            int_matches = [int(x) for x in matches2]
            peace = peace.replace(match,
                                  str(sum(int_matches)/len(int_matches)))
        return average(peace)

    else:  # No more '@' -
        return maximum(peace)


def negate(peace):
    """Negate the expression after the '~' and send to average.

    Args:
        peace (str): The expression from 'factorial'.

    Returns: str - The return from the average function.
    """

    matches = re.findall(r'~-?\d+', peace)
    for match in matches:
        peace = peace.replace(match,
                              str(-1 * int(re.findall(r'-?\d+', match)[0])))
    return average(peace)


def factorial(peace):
    """Solve factorial expressions and send to the next function in the chain.

    Args:
        peace (str): Inner most parenthesis found in the parenthesis function,
         or the whole equation when no parenthesis were found.

    Returns: The return of the negate function.
    """

    matches = re.findall(r'\d+!', peace)
    for match in matches:
        matches2 = re.findall(r'\d+', match)
        fact_list = [x for x in range(1, int(matches2[0]) + 1)]
        result = 1
        for number in fact_list:
            result = result * number
        peace = peace.replace(match, str(result))
    return negate(peace)


def parenthesis(user_eq):
    """Deal with parenthesis by finding the nested parenthesis first.

    Run recursively until no more parenthesis are found.

    Args:
        user_eq (str): The entered equation without spaces

    Returns: str - The return of the factorial function.
    """

    matches = re.findall(r'\((?:[^()])*\)', user_eq)
    if len(matches) > 0:
        matches2 = re.findall(r'(?<=\().+?(?=\))', matches[0])
        user_eq2 = user_eq.replace(matches[0], str(factorial(matches2[0])))
        return parenthesis(user_eq2)

    else:  # When no Parenthesis were found -
        return factorial(user_eq)


def space_remove(user_eq):
    """Remove white spaces from equation.

    Args:
        user_eq (str): The entered equation

    Returns: str - The return of the parenthesis function.
    """

    user_eq = user_eq.replace(' ', '')
    return parenthesis(user_eq)


def main():
    """Get users equation and sends it through the 'chain' of solving.

    Returns: str - The final result.
    """

    user_eq = input("Enter equation (type 'quit' to exit)\n")
    if user_eq != 'quit':
        print(space_remove(user_eq))
        main()

    else:  # User want to quit -
        print("Good Bye!")
        exit()


if __name__ == '__main__':
    main()
