"""Reads a file, edits it and saves it in a new location."""
import os

FIRST_NAME = "Keren"
LAST_NAME = "Guez"


def check_exists(input_file, output_folder):
    """Checks if paths are valid and prints a message accordingly.

    Args:
        input_file (str): The path to the file that will be edited.
        output_folder (str) : The path to the output folder.
    Returns:
        True : If both paths are valid.
        False : If any path isn't valid.
    """
    if not os.path.exists(input_file):
        print(f"The input file '{input_file}' doesn't exist.")
        return False
    if not os.path.exists(output_folder):
        print(f"The output folder '{output_folder}' doesn't exist.")
        return False
    return True


def stam(filename, output_file):
    """Gets a file, edits it and saves it to a new location.

    Args:
        filename (str): The path to the file that will be edited.
        output_file (str) : The path of the new file to be saved.
    """
    output_dir = os.path.dirname(os.path.abspath(output_file))
    if check_exists(filename, output_dir):
        with open(filename, 'r') as file:
            new_concat_lines = (FIRST_NAME + line[:-1] + LAST_NAME + "\n"
                                for line in file)
            with open(output_file, 'w') as new_file:
                for line in new_concat_lines:
                    new_file.write(line)


def main():
    path = r"C:\Users\keren\Desktop\rooms.txt"
    new_path_to_save = r"C:\Users\keren\Desktop\newfile3.txt"
    stam(path, new_path_to_save)


if __name__ == "__main__":
    main()
