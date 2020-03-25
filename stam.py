__author__ = 'Adi'


def main():
    input_file = open(r'C:\..., text.txt', 'r')
    new_file = open('new_text.txt', 'w+')
    # line = None
    for line in input_file:
        new_line = 'Adi ' + line[:-1] + ' Kadar Levi'
        print(new_line)
        new_file.write(new_line + '\n')

    input_file.close()
    new_file.close()


if __name__ == main():
    main()
