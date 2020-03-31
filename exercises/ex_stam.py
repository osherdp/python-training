# Stam Exercise

import sys

PATH_ORG = 1
PATH_DES = 2
FIRST_NAME = "Shira"
LAST_NAME = "Vaknin"


def add_name(file_path, first_name, last_name, other_path):
    """Add my name to each line in the original file and save in another file.

    Args:
        file_path: a string, path to original file
        first_name: a string, my first name
        last_name: a string, my last name
        other_path: a string, path to destination file
    """
    try:
        with open(file_path, 'r') as file_pointer:
            with open(other_path, 'w') as new_file:
                for line in file_pointer:
                    new_file.write("{} {} {}\n".
                                   format(first_name,
                                          line.rstrip(), last_name))

        print("new file saved in:" + other_path)

    except(RuntimeError, TypeError, NameError):
        pass


def main():
    if len(sys.argv) < 3:
        print("need to have 2 argument- path to original file," +
              "and path to destination file")
    else:
        file_path = sys.argv[PATH_ORG]
        file_des_path = sys.argv[PATH_DES]
        add_name(file_path, FIRST_NAME, LAST_NAME, file_des_path)


if __name__ == '__main__':
    main()
