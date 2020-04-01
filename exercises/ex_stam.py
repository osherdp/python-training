# Stam Exercise

import sys

PATH_ORIGINAL = 1
PATH_DESTINATION = 2
FIRST_NAME = "Shira"
LAST_NAME = "Vaknin"


def add_name(file_path, first_name, last_name, other_path):
    """Add my name to each line in the original file and save in another file.

    Args:
        file_path (string): path to original file.
        first_name (string): my first name.
        last_name (string): my last name.
        other_path (string): path to destination file.
    """
    try:
        with open(file_path, 'r') as file_pointer:
            with open(other_path, 'w') as new_file:
                for line in file_pointer:
                    new_file.write(f"{first_name} {line.rstrip()}"
                                   f" {last_name}\n")

        print("new file saved in:" + other_path)

    except FileNotFoundError:
        print("The path to the file you have entered was incorrect.")

    except Exception as e:
        print(e)


def main():
    if len(sys.argv) < 3:
        print("need to have 2 argument- path to original file," +
              "and path to destination file")

    else:
        file_path = sys.argv[PATH_ORIGINAL]
        file_des_path = sys.argv[PATH_DESTINATION]
        add_name(file_path, FIRST_NAME, LAST_NAME, file_des_path)


if __name__ == '__main__':
    main()
