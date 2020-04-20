"""The script adds firs and last name to the file's rows.
"""
import sys


PATH_TO_ORIGINAL_FILE = 1
PATH_TO_NEW_FILE = 2


def add_name_to_filerows(filename, newfilename):
    """Adds name to file's rows

    Adds a first name at the beginning of each line
    and a last name to the end of each line in the new file.

    Args:
        filename (str): file name ending with '.txt'.
        newfilename (str): file name ending with '.txt'.
    """
    with open(filename, 'r') as file:
        for line in file:
            with open(newfilename, 'a') as newfile:
                newfile.write(f"keren {line.strip()} kayrich\n")


def main():
    """Adds name to the new file's rows.
    """
    filename = sys.argv[PATH_TO_ORIGINAL_FILE]
    newfile = sys.argv[PATH_TO_NEW_FILE]
    add_name_to_filerows(filename, newfile)


if __name__ == '__main__':
    main()
