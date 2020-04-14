# The purpose of this file is to answer the STAM exercise.

import os
import shutil
import sys


FILE_INDEX = 1
PATH_INDEX = 2


def main():
    original_text_file = sys.argv[FILE_INDEX]
    path_of_new_file = sys.argv[PATH_INDEX]
    if is_exist(original_text_file, path_of_new_file):
        add_strings(original_text_file, path_of_new_file)


def is_exist(text_file, path):
    """
    checks if the text file and the path exist
    :param text_file: input text file
    :param path: input path
    :return: True/ False
    """
    return text_file and path


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
                text_of_line = line[:-1]  # remove the '\n'
                new_file.write("Sol {} Mirilashvili ".format(text_of_line) + '\n')
    try:
        shutil.move("new_file.txt", path)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
