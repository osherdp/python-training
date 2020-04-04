import os
import sys


def correct_parameter(path):
    """

    Arg:
        path- the path received as parameter to the script

    Returns:
        True if the path is a file, False otherwise

    """
    if not os.path.isfile(path):
        print("your file not foud")
        return False

    return True


def add_name_to_filerows(filename, newfilename):
    """

    Args:
        filename(.txt file)- the path to the original file, first parameter
        newfilename(.txt file)- the path to the new file, second parameter

    Returns:
        the function adds a first name at the beginning of each line
        and a last name to the end of each line.

    """
    with open(filename, 'r') as file:
        for line in file:
            with open(newfilename, 'a') as newfile:
                newfile.write(f"keren {line.strip()} kayrich\n")


def main():
    """

    Args:
        filename (.txt file): the path to the original file
            example:
                C:\Users\User\Desktop\stam.txt
        newfile (.txt file): the path to the new file
            example:
                C:\Users\User\Desktop\newstam1.txt

    :return:
        if filename is a file,
        adds a first name at the beginning of each line and
        a last name to the end of each line in the file newfile.
        else, an error message will be printed.

    """
    filename = sys.argv[1]
    newfile = sys.argv[2]
    if correct_parameter(filename):
        add_name_to_filerows(filename, newfile)

    else:
        print("please check your parameters")


if __name__ == '__main__':
    main()
