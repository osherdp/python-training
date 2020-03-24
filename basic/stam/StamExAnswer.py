__author__ = "Keren"

FIRST_NAME = "Keren"
LAST_NAME = "Guez"


def add_vals(line):
    """
    Args:
        line: (str) a line of text

    Returns: a new concatenated line with constant values

    """
    return FIRST_NAME + line + LAST_NAME


def stam(filename):
    """ The function gets file path, edits it and saves the new edited file to a new location

    Args:
        filename: (str) the full path to the file that will be edited

    """
    try:
        with open(filename, 'r') as file:
            new_concat_lines_lis = (add_vals(line[:-1])+"\n" if line[-1:] == "\n" else add_vals(line) for line in file)
            new_path_to_save = r"C:\Users\keren\Desktop\newfile.txt"
            with open(new_path_to_save, 'w') as new_file:
                for line in new_concat_lines_lis:
                    print("line "+line, end="")
                    new_file.write(line)
    except Exception as e:
        print(e)


def main():
    path = r"C:\Users\keren\Desktop\rooms.txt"
    stam(path)


if __name__ == "__main__":
    main()
