import re
import math
from statistics import mean

from pip._vendor.msgpack.fallback import xrange


class Calculator:
    def __init__(self, exercise):
        self.__operations_regex_dict = {1: r'\(\d+[!%^+/*\-~$&@]\d+\)+',
                                        2: r'\!',
                                        3: r'[$&@]',
                                        4: r'%',
                                        5: r'\^',
                                        6: r'[/*]',
                                        7: r'[-+]'}
        self.exercise = exercise.strip()
        self.solved = ''
        print(self.arrange)

    @property
    def arrange(self):
        self.solved = re.search(r'(!\d+)|(([~!]\d+)?\d+[-()%^/*+$&@]([~!]\d+)?\d+)', self.exercise)
        if self.solved is None:
            return self.exercise
        exercise = self.exercise
        for operation in self.__operations_regex_dict.values():
            if self.__operations_regex_dict[1] == operation:
                reg = str(operation)
                exp = re.search(reg, exercise)
            elif self.__operations_regex_dict[2] == operation:
                reg = str(operation) + r'\d+'
                exp = re.search(reg, exercise)
            else:
                reg = r'(\~\d+)?\d+' + str(operation) + r'(\~\d+)?\d+'
                exp = re.search(reg, exercise)
            if exp is not None:
                exe = exp.group()
                sign = re.search(r'[!^%+/*$&@]', exe)
                operation = exe
                exe = exe.replace(r'(', '')
                exe = exe.replace(r')', '')
                self.solved = (exe, sign.group())
                result = self.solve()
                self.exercise = self.exercise.replace(operation, str(result))
                return self.arrange

    def solve(self):
        exercise = self.solved
        operation = exercise[0]
        sign = exercise[1]
        self.solved = operation.split(sign)
        for i in xrange(len(self.solved)):
            self.solved[i] = self.solved[i].replace(r'~', '-')
        if sign == '&':
            return self.min()
        elif sign == '*':
            return self.multiplication()
        elif sign == '%':
            return self.modulo()
        elif sign == '+':
            return self.addition()
        elif sign == '-':
            return self.subtraction()
        elif sign == '!':
            return self.factorial()
        elif sign == '^':
            return self.power()
        elif sign == '@':
            return self.avg()
        elif sign == '$':
            return self.max()
        elif sign == '/':
            return self.division()

    def factorial(self):
        expression = self.solved
        x = int(expression[1])
        return math.factorial(x)

    def max(self):
        expression = self.solved
        x = int(expression[0])
        y = int(expression[1])
        return max(x, y)

    def min(self):
        expression = self.solved
        x = int(expression[0])
        y = int(expression[1])
        return min(x, y)

    def avg(self):
        expression = self.solved
        x = [int(expression[0]), int(expression[1])]
        return mean(x)

    def modulo(self):
        expression = self.solved
        x = int(expression[0])
        y = int(expression[1])
        return math.fmod(x, y)

    def power(self):
        expression = self.solved
        x = int(expression[0])
        y = int(expression[1])
        return math.pow(x, y)

    def division(self):
        expression = self.solved
        x = int(expression[0])
        y = int(expression[1])
        return x / y

    def multiplication(self):
        expression = self.solved
        x = int(expression[0])
        y = int(expression[1])
        return x * y

    def subtraction(self):
        expression = self.solved
        x = int(expression[0])
        y = int(expression[1])
        result = str(abs(x) - abs(y))
        result = result.replace(r'-', '~')
        return result

    def addition(self):
        expression = self.solved
        x = int(expression[0])
        y = int(expression[1])
        return x + y
