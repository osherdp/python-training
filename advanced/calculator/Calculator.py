class Calc:
    lst_operators = ["*", "/", "^", "-", "+"]

    def __init__(self, exercise):
        """
        Initializing method, gets a string value that represent exercise and
        organize it to a usable list and check its format.
        :param exercise:  String object that represent exercise.
        """
        self._lst_exercise = self._organize_input(exercise)
        self._organize_with_signed_numbers()
        self._check_input()

    @staticmethod
    def _organize_input(exercise):
        """
        Organized the calculation to a list when numbers and operators are separated.
        Removes all the spaces that was inserted.
        :return: Organized list.
        """
        if type(exercise) != str:
            raise TypeError("Calc object gets only string as exercise. not '%s'" % exercise.__class__.__name__)

        exercise.replace(" ", "")

        lst_exercise = []
        part_of_exercise = ""
        for char in exercise:

            if char in Calc.lst_operators:
                if part_of_exercise:
                    lst_exercise.append(part_of_exercise)

                part_of_exercise = ""
                lst_exercise.append(char)

            # Getting the number values that are made of digits and a dot possibly.
            else:
                part_of_exercise += char

        lst_exercise.append(part_of_exercise)

        return lst_exercise

    def _organize_with_signed_numbers(self):
        """
        Organize the list of exercise while implement a way that maneges get answer to a calculation with signed
        numbers like so: ['-', '5', '+', '3', '*', '-', '3'] ==> ['-5', '+', '3', '*', '-3']
        :return:
        """
        # If the signed number is the first number.
        if self._lst_exercise[0] in Calc.lst_operators:
            self._lst_exercise[1] = self._lst_exercise[0] + self._lst_exercise[1]
            self._lst_exercise = self._lst_exercise[1:]

        # Checks when there are 2 operators one after another. The list changes while the loop running,
        # therefor we need a Index error for indication.
        index = 0
        end_of_list = False
        while not end_of_list:
            try:
                if self._lst_exercise[index] in Calc.lst_operators and self._lst_exercise[index + 1] in Calc.lst_operators:
                    self._lst_exercise[index + 2] = self._lst_exercise[index + 1] + self._lst_exercise[index + 2]
                    self._lst_exercise.pop(index + 1)
                index += 1

            except IndexError:
                end_of_list = True

    def _check_input(self):
        """
        Checks the values of the list and check if the calculation input is valid.
        The wanted format is [number, operator, number, operator, number] - must starts and ends with a number.
        :return:
        """
        input_is_ok = True

        for index in range(len(self._lst_exercise)):
            if index % 2 == 0:
                try:
                    float(self._lst_exercise[index])
                except ValueError:
                    input_is_ok = False
                    break

            else:
                if self._lst_exercise[index] not in Calc.lst_operators:
                    input_is_ok = False
                    break

        if not input_is_ok:
            raise SyntaxError("The calculation writing format is not valid.")

    def find_solution(self):
        """
        Recourse method, find a solution for the calculation, every time sends a new Calc object according
        to the 'strongest operator'.
        :return:
        """

        if len(self._lst_exercise) == 1:
            return self._lst_exercise[0]

        elif len(self._lst_exercise) == 3:
            return self._simple_calc()

        # Find the first strongest operator - the first math function that need to be done.
        strong_op_index = self._strongest_op_index()
        first_from_exercise = Calc("".join(self._lst_exercise[strong_op_index - 1:strong_op_index + 2]))

        # Recourse the function with the first calculation and adds to a list. for example
        # self._lst_exercise = ['1', '+', ['2',  '*', '3'], '-', '5']
        self._lst_exercise = self._lst_exercise[:strong_op_index - 1] + [first_from_exercise.find_solution()] + self._lst_exercise[strong_op_index + 2:]

        return self.find_solution()

    def _simple_calc(self):
        """
        Returns the solution to simple calculations -
        When list is only - [num1, operator, num2].
        :return The answer - float.
        """
        num1 = float(self._lst_exercise[0])
        operator = self._lst_exercise[1]
        num2 = float(self._lst_exercise[2])
        answer = 0

        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2
        elif operator == "/":
            answer = num1 / num2
        elif operator == "^":
            answer = num1 ** num2

        return str(answer)

    def _strongest_op_index(self):
        """
        :return: The index of the first 'strongest' operator - according to math order of operations.
        """
        lst_ex = self._lst_exercise
        strongest_index = 0

        if "^" in lst_ex:
            strongest_index = lst_ex.index("^")

        elif "*" in lst_ex or "/" in lst_ex:
            for value in lst_ex:
                if value == "*" or value == "/":
                    strongest_index = lst_ex.index(value)
                    break

        # Plus or minus
        else:
            for value in lst_ex:
                if value == "+" or value == "-":
                    strongest_index = lst_ex.index(value)
                    break

        return strongest_index


def main():
    """
    User interface - getting calculations and sending answers in loop.
    """

    exit_flag = True
    print("Welcome")

    while exit_flag:
        exercise = input("enter calculation or enter 'exit':\n")

        if exercise == 'exit':
            exit_flag = False
            print("bye")

        else:
            new_calc = Calc(exercise)
            print(new_calc.find_solution())


if __name__ == '__main__':
    main()
