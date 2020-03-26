import sys


FILE_NAME = 1
FILE_NAME_NEW = "D:/Python Training/Pr1/stam_new.txt"


def write_to_file(file_name, FILE_NAME_NEW, first_name, last_name):
    """ Read from file stam.txt line by line, and write to file stam_new.txt with the first and last name
    """

    try: # if stam.txt exist
        with open(file_name, 'r') as orig_data:
            for line in orig_data:
                # print(line.strip())
                line = line.strip()
                with open(FILE_NAME_NEW, 'a') as new_file:
                    new_file.write(first_name + ' ' + line.replace("\n", " ") + ' ' + last_name + '\n')
    except Exception as err:  # if stam.txt doesn't exist
        print(err)  # print the error


def receive_first_name():
    return input('Please enter your first name: ')


def receive_last_name():
    return input('Please enter your last name: ')


def main():
    file_name = sys.argv[FILE_NAME]
    first_name = receive_first_name()
    last_name = receive_last_name()
    write_to_file(file_name, FILE_NAME_NEW, first_name, last_name)


if __name__ == "__main__":
    main()