import sys
import os


FILE_NAME = 1
PATH = 2


def main():
    file_name = sys.argv[FILE_NAME]
    with open(file_name, 'r') as input_file:
        for line in input_file:
            print(line,)
    directory = sys.argv[PATH]
    print(os.listdir(directory))
    # print(type(os.listdir(directory)))


if __name__ == "__main__":
    main()
