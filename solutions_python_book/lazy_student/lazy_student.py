FILE_HOME_WORK_NAME = "home_work.txt"
FILE_SOLUTION_NAME = "solutions.txt"


def main():
    try:
        with open(FILE_HOME_WORK_NAME, "r") as f_read:
            all_exercises = f_read.readlines()

        with open(FILE_SOLUTION_NAME, "w") as f_write:
            for line in all_exercises:
                if check_line(line):
                    exercise_lst = line[:-1].split(" ")
                    try:
                        result = str(simple_calc(exercise_lst))
                        f_write.write(result + "\n")
                    except ZeroDivisionError as e:
                        f_write.write("The exercise is not valid, you cant divide by zero: %s" % line)
                else:
                    f_write.write("The exercise was not written write!: %s" % line)
    except IOError as e:
        print("The path of the home work file is not correct try again", e)


def check_line(line):
    """
    Have to be in this format: "num,space,operator,space,num,\n"
    :param line: string exercise
    :return: boolean value.
    """
    # check if there is an operator, if so what it is and what's its index.
    op_list = ["+", "-", "*", "/"]
    op_index = None
    for char in line:
        if char in op_list:
            op_index = line.index(char)
            break
    if op_index is None or op_index == 0 or op_index == len(line) - 1:
        return False

    # checks for the spaces
    if line[op_index - 1] != " " or line[op_index + 1] != " ":
        return False

    # checks if there is more spaces then needed
    line_lst = line.split(" ")
    if len(line_lst) != 3:
        return False

    # checks if the first and last remaining values are integers.
    try:
        int(line_lst[0])
        int(line_lst[2])
    except ValueError:
        return False
    return True


def simple_calc(exercise_lst):
    num1 = int(exercise_lst[0])
    op = exercise_lst[1]
    num2 = int(exercise_lst[2])
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2


if __name__ == '__main__':
    main()

