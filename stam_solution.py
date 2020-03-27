"""Gets a file name, copy it's content with an addition of
   my first name at the beginning of every line and my last
   name at the end and then it saves the new content as a different file."""

import sys
import os

NAME = 1
FILE = sys.argv[NAME]
FIRST_NAME = 'Maya'
LAST_NAME = 'Reuveni'


def get_full_path():
    """Finds and fetches the file full path.
    """
    for root, dirs, files in os.walk(r'C:\Users'):
        for name in files:
            if name == FILE:
                address = os.path.abspath(os.path.join(root, name))
    return address


def edit_text(lines):
    """Gets the file's lines and adds first name at
     the beginning and last name at the end.
    Args:
        lines(list): The original file lines.
    Returns:
        A string that contains the edited content.
    """
    new_lines = []

    for i in lines:
        enter_index = i.find('\n')
        if enter_index != 0:
            line = i[:enter_index-1]
            edited_line = '{} {} {}\n'.format(FIRST_NAME, line, LAST_NAME)
            new_lines.append(edited_line)
        else:
            edited_line = i
            new_lines.append(edited_line)
    return new_lines


def save_new_file(new_lines, address):
    """Saves a new file with the edited content to the location.
      Args:
          new_lines(str): The edited content of the original file.
          address(str): The location of the file.
      """
    new_file_name = '{}_{}'.format(FIRST_NAME, str(FILE))
    new_file_path = os.path.join(address, new_file_name)
    with open(new_file_path, 'w') as new_file:
        new_file.writelines(new_lines)


def main():
    full_file_path = get_full_path()
    with open(full_file_path, 'r') as original_file:
        content = original_file.readlines()
    address = full_file_path[0:(full_file_path.find(str(FILE)) - 1)]
    new_lines = edit_text(content)
    save_new_file(new_lines, address)


if __name__ == '__main__':
    main()
