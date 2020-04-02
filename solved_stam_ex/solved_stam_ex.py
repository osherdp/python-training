"""A program that receive a file name, and add specific words to content. """

import sys

FIRST_NAME = 'liel'
PATH_EMPTY_FILE = 2
LAST_NAME = 'yaakobov'
PATH_CONTENT_FILE = 1


def main():
    try:
        with open(sys.argv[PATH_CONTENT_FILE], 'r') as content_file:
            with open(sys.argv[PATH_EMPTY_FILE], 'w') as empty_file:
                for line in content_file:
                    empty_file.write(f"{FIRST_NAME} {line.rstrip()}"
                                     f" {LAST_NAME}\n")

    except FileNotFoundError:
        print("The path you entered is not correct. Please check it")


if __name__ == '__main__':
    main()
