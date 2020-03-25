import sys

HOMEWORK_FILE_NAME = 1
SOLUTIONS_FILE_NAME = 2
PATH = 3


def write_to_solution(solution_file_name, result, line):
    try:
        with open(solution_file_name, 'a') as solution_file:
            if result is not None:
                solution_file.write(line.replace("\n", " ") + ' = ' + str(result) + '\n')
    except Exception as err:  # if solutions.txt doesn't exist
        print(err)


def solve_the_equation(equation_list, solution_file_name):
    try:
        if equation_list[1] == '+':
            return int(equation_list[0]) + int(equation_list[2])
        elif equation_list[1] == '-':
            return int(equation_list[0]) - int(equation_list[2])
        elif equation_list[1] == '*':
            return int(equation_list[0]) * int(equation_list[2])
        elif equation_list[1] == '/':
            return float(int(equation_list[0]) / int(equation_list[2]))
        else:
            with open(solution_file_name, 'a') as solution_file:
                solution_file.write('Unknown sign ' + '\n')
    except Exception as err:  # if one of the numbers is not valid
        with open(solution_file_name, 'a') as solution_file:
            solution_file.write(str(err) + '\n')


def read_from_homework(homework_file, solution_file_name):
    try:  # if homework.txt exist
        with open(homework_file, 'r') as homework_file:
            for line in homework_file:
                equation_list = line.split()  # create list from the string
                result = solve_the_equation(equation_list, solution_file_name)
                write_to_solution(solution_file_name, result, line)
    except Exception as err:  # if homework.txt doesn't exist
        print(err)


def main():
    homework_file_name = sys.argv[HOMEWORK_FILE_NAME]
    solution_file_name = sys.argv[SOLUTIONS_FILE_NAME]
    read_from_homework(homework_file_name, solution_file_name)


if __name__ == "__main__":
    main()
