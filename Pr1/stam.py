import sys


FILE_NAME = 1


def write_first_name(file_name, first_name):
    with open(file_name, 'a') as first_name_input:
        first_name_input.write(first_name + ', ')


def write_last_name(file_name, last_name):
    with open(file_name, 'a') as last_name_input:
        last_name_input.write(last_name)


def receive_first_name():
    return input('Please enter your first name: ')


def receive_last_name():
    return input('Please enter your last name: ')


def main():
    file_name = sys.argv[FILE_NAME]
    # first_name = receive_first_name()
    # last_name = receive_last_name()
    write_first_name(file_name, 'Idan')
    write_last_name(file_name, 'Sokolovsky')


if __name__ == "__main__":
    main()