__author__ = 'Adi'

FIRST_NAME = 'Adi'
LAST_NAME = 'Kadar Levi'


def main():
    try:
        input_file_path = input('please enter text file path\n')
        with open(input_file_path, 'r') as input_file:
            with open('new_text.txt', 'w+') as new_file:
                for line in input_file:
                    new_line = FIRST_NAME + ' ' + format(line[:-1]) + ' ' + LAST_NAME
                    print(new_line)
                    new_file.write(new_line + '\n')
    except Exception as e:
        print(e)


if __name__ == main():
    main()
