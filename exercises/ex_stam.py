# Stam Exercise

import sys
PATH = 1
FIRST_NAME = "Shira"
LAST_NAME = "Vaknin"
PATH_TO_OTHER_FILE = r"Z:\python\my_name.txt"


def add_name(file_path, firs_name, last_name, other_path):
    """
    Get file address add my name to the line and save it in new location.

    Add my first name to the beginning of each line.
    Add my last name to the end of each line.

    Args:
        file_path: a string,
        firs_name:
        last_name:
        other_path:
    """
    try:
        with open(file_path, 'r') as file_pointer:
            with open(other_path, 'w') as new_file:
                for line in file_pointer:
                    new_file.write(firs_name + " " + line.rstrip() + " " + last_name + "\n")
        print("new file saved in:" + other_path)
    except Exception as e:
        print(e)


def main():
    if len(sys.argv) < 2:
        print("need to have 1 argument- path to file")
    else:
        file_path = sys.argv[PATH]
        add_name(file_path, FIRST_NAME, LAST_NAME, PATH_TO_OTHER_FILE)


if __name__ == '__main__':
    main()
