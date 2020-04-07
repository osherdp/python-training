__author__ = "Sol"


import sys
import os
import shutil
FILE = 1
PATH = 2


def main():
    text_file = sys.argv[FILE]
    path = sys.argv[PATH]
    is_exist(text_file, path)
    add_strings(text_file, path)


def is_exist(text_file, path):
    """
    checks if the text file is a file
    checks if the path exist
    print the appropriate response
    :param text_file: input text file
    :param path: input path
    :return: True/ False
    """
    if os.path.isfile(text_file):
        if os.path.exists(path):
            # if both exist and OK returns True
            return True
        print("The path not exist")
        return False
    print("This is not a text file")
    return False


def add_strings(text_file, path):
    """
    Open the text file and creates the new file.
    Enter the text from the text file into the new file with the
    extra strings
    Change the location of the new file to the right path
    :param text_file: input text file
    :param path: path of the new file
    :return: void
    """
    with open(text_file, 'r') as text_file:
        with open("new_file.txt", 'w+') as new_file:
            for line in text_file:
                text_of_line = line[0: len(line) - 1]  # remove the '\n'
                new_file.write("Sol {} Mirilashvili ".format(text_of_line) + '\n')
    try:
        shutil.move("new_file.txt", path)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
