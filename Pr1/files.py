FILE_NAME = r'D:\Try.txt'
FILE_NAME1 = r'D:\Try1.txt'


def duplicate(file1, file2):
    with open(file1, 'r') as input_file:
        for line in input_file:
            with open(file2, 'a') as input_file1:
                input_file1.write(line)


def main():
    duplicate(FILE_NAME, FILE_NAME1)


if __name__ == "__main__":
    main()


