__author__ = 'Shaked Manor'


def changing_content(file1, file2):
    """changing original file content by adding  a
    first name at the beginning of each sentence and a lest name at the
    end of each one. and then saving the new content at new file
    Args:
    file1- original file
    file2- new flie """

    with open(file1, 'r') as original_file:
        new_file = open(file2, 'w')
        for line in original_file:
            new_file.write('Shaked {} Manor\n'.format(line))


def checking_new_file(file_name):
    """function that checks if the content with the changes
    that were made placed curectly in the new file
    Arg: file_name- the file name of the new file"""
    file_check = open(file_name, 'r')
    print file_check.read()


def main():
    original = r'c:\python\original file.txt'
    new = r'c:\python\new file.txt'
    changing_content(original, new)
    checking_new_file(new)


if __name__ == '__main__':
    main()