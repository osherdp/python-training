
"""A script that gets a file name, copy it's content with an addition of my first name at the beginning of every
line and my last name at the end and then it saves the new content as a different file."""

import sys
import os


NAME = 1
FILE = sys.argv[NAME]


def main():
    full_file_path = get_full_path()
    with open(full_file_path, 'r') as original_file:
        content = original_file.read()
    address = full_file_path[0:(full_file_path.find(str(FILE)) - 1)]
    lines = content.split('\n')
    new_lines = edit_text(lines)
    print(new_lines, address)


def get_full_path():
    """Finds and fetches the file full path.
    """
    if os.path.isfile(FILE):
        for root, dirs, files in os.walk(r'C:\Users'):
            for name in files:
                if name == FILE:
                    address = os.path.abspath(os.path.join(root, name))
        return address
    else:
        print("The requested file doesn't exist")


def edit_text(lines):
    """Gets the file's lines and adds first name at the beginning and last name at the end.
    Args:
        lines(list): The original file lines.
    Returns:
        A string that contains the edited content.
    """
    new_lines = ''
    for i in lines:
        if i:
            edited_line = 'Maya' + ' ' + i + ' ' + 'Reuveni'
            new_lines = new_lines + '\n' + edited_line
        else:
            edited_line = i
            new_lines = new_lines + '\n' + edited_line
    return new_lines


def save_new_file(new_lines, address):
    """Saves a new file with the edited content to the location.
      Args:
          new_lines(str): The edited content of the original file.
          address(str): The location of the file.
      """
    new_file_name = 'Maya_' + str(FILE)
    new_file_path = os.path.join(address, new_file_name)
    new_file = open(new_file_path, 'w')
    new_file.write(new_lines)
    new_file.close()


if __name__ == '__main__':
    main()
