"""Reads a file, edits it and saves it in a new location."""
import sys

INPUT_FILE = 1
OUTPUT_FILE = 2
LAST_NAME = "Guez"
FIRST_NAME = "Keren"


def stam(filename, output_file):
    """Get a file, edit it and save it to a new location.

    Args:
        filename (str): The path to the file that will be edited.
        output_file (str) : The path of the new file to be saved.
    """
    with open(filename, 'r') as file:
        with open(output_file, 'w') as new_file:
            for line in file:
                new_line = f"{FIRST_NAME}{line[:-1]}{LAST_NAME}\n"
                new_file.write(new_line)


def main():
    """Initialize input and output paths and call stam function."""
    try:
        path = sys.argv[INPUT_FILE]
        new_path_to_save = sys.argv[OUTPUT_FILE]
        stam(path, new_path_to_save)

    except IndexError:
        print("Wrong numbers of parameters in script(should be 2).")

    except FileNotFoundError as e:
        print(f"The path '{e.filename}' was not found")


if __name__ == "__main__":
    main()


