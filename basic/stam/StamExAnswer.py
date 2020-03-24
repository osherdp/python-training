"""This program reads a file, edits it and saves it in a new location"""
import os

FIRST_NAME = "Keren"
LAST_NAME = "Guez"


def add_vals(line):
    """This function concatenates a line with some given text

    Args:
        line (str): a line of text

    Returns:
        str: a new concatenated line

    """
    return FIRST_NAME + line + LAST_NAME


def stam(filename, output_file):
    """The function gets a file, edits it and saves it to a new location

    Args:
        filename (str): the path to the file that will be edited
        output_file (str) : the path of the new file to be saved

    """
    last_backslash = output_file.rfind("\\")
    if os.path.exists(filename) and os.path.exists(output_file[:last_backslash]):
        with open(filename, 'r') as file:
            new_concat_lines_lis = (add_vals(line[:-1])+"\n"
                                    if line[-1:] == "\n"
                                    else add_vals(line)
                                    for line in file)
            with open(output_file, 'w') as new_file:
                for line in new_concat_lines_lis:
                    new_file.write(line)
    else:
        print(f"either the original file path or the output path don't exist")



def main():
    path = r"C:\Users\keren\Desktop\rooms.txt"
    new_path_to_save = r"C:\Users\keren\Desktop\newfile2.txt"
    stam(path, new_path_to_save)


if __name__ == "__main__":
    main()
