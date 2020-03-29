import os


def main():
    file_to = r'C:\Users\nimro\Documents\python_test\homework_name.txt'

    while True:
        file_name = input('enter file-  ')

        if os.path.isfile(file_name):
            read_file = open(file_name, 'r')
            for line in read_file:
                with open(file_to, 'a') as write_file:
                    write_file.write('nimrod    ' + line.replace('\n', '') + '    satt' + '\n')
            print('Done')
            break


if __name__ == '__main__':
    main()
