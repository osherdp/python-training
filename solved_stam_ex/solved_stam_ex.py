"""A program that receive a file name, and add specific words to content.

Add your first name to the beginning of each line,
and your last name to the end of each line.

"""

import sys

PATH_FILE_WITH_CONTENT = 1
PATH_EMPTY_FILE = 2


def main():
    firs_name = 'liel'
    last_name = 'yaakobov'

    try:
        with open(sys.argv[PATH_FILE_WITH_CONTENT], 'r') \
                as pointer_file_with_content:
            with open(sys.argv[PATH_EMPTY_FILE], 'w') as pointer_empty_file:

                for line in pointer_file_with_content:
                    pointer_empty_file.write(f"{firs_name} {line.rstrip()}"
                                             f" {last_name}\n")

    except FileNotFoundError:
        print("The path you entered is not correct. Please check it")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

