import sys
import os


HOMEWORK_FILE_NAME = 1
SOLUTIONS_FILE_NAME = 2
PATH = 3


def write_to_solution(solution_file_name, result, line, flag):
    with open(solution_file_name, 'a') as solution_file:
        if flag is True:
            solution_file.write(line.replace("\n", " ") + ' = ' + str(result) + '\n')
        elif flag is False:
            solution_file.write('Something is wrong with the equation\n')


def solve_the_equation(equation_list):
    if equation_list[1] == '+':
        return int(equation_list[0]) + int(equation_list[2]), True
    elif equation_list[1] == '-':
        return int(equation_list[0]) - int(equation_list[2]), True
    elif equation_list[1] == '*':
        return int(equation_list[0]) * int(equation_list[2]), True
    elif equation_list[1] == '/':
        if int(equation_list[2]) != 0:
            return float(int(equation_list[0]) / int(equation_list[2])), True
        else:  # the user divided by zero
            return 0, False
    else:  # the user gave an unknown sign
        return 0, False


def read_from_homework(homework_file, solution_file_name):
    with open(homework_file, 'r') as homework_file:
        for line in homework_file:
            equation_list = line.split()  # create list from the string
            if check_numbers(equation_list):  # if the numbers are really numbers
                [result, flag] = solve_the_equation(equation_list)
                write_to_solution(solution_file_name, result, line, flag)
            else:  # if the numbers are wrong we don't even solve the eq, and flag will be False
                flag = False
                result = 0
                write_to_solution(solution_file_name, result, line, flag)


def check_file(directory, file_name):
    files_in_path = os.listdir(directory)  # files_in_path is a list containing all the files in the directory
    for file in files_in_path:
        if file_name == file:  # if file_name matches one of the files in the directory then return True
            return True
    return False


def check_numbers(equation_list):
    if equation_list[0].isdigit() and equation_list[2].isdigit():
        return True
    else:
        return False


def main():
    homework_file_name = sys.argv[HOMEWORK_FILE_NAME]
    solution_file_name = sys.argv[SOLUTIONS_FILE_NAME]
    directory = sys.argv[PATH]
    if not check_file(directory, homework_file_name) or not check_file(directory, solution_file_name):
        print('There is no such file in the directory')
    else:  # homework.txt and solutions.txt exist
        read_from_homework(homework_file_name, solution_file_name)


if __name__ == "__main__":
    main()

