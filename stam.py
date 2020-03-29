__author__ = 'Adi'

FIRST_NAME = 'Adi'
LAST_NAME = 'Kadar Levi'


def main():
    try:
        input_file_path: str = input('please enter text file path\n')
        with open(input_file_path, 'r') as input_file:
            with open('new_text.txt', 'w+') as new_file:
                for line in input_file:
                    new_line = ' {} {} {}'.format(FIRST_NAME, line.strip(),  LAST_NAME)
                    print(new_line)
                    new_file.writelines(new_line)
    except FileNotFoundError:
        print('Empty Path')
    except Exception as e:
        print(e)


if __name__ == main():
    main()
