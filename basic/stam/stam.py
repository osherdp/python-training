import sys

__author__ = 'Nurick'


def clear_file(path):
    """delete a file content"""
    with open(path, 'w') as fh:
        fh.write('')


def main():
    """take file name from argument and copies it to file name in second
    argument in addition - adds 'first_name' to the beginning םf each line
    and 'last_name' to the end of each line """
    path = '/'.join(sys.argv[0].split('/')[:-1]) + '/'
    try:
        org_file_name = sys.argv[1]
    except IndexError:
        print(Exception)
        org_file_name = 'README.md'
    try:
        new_file_name = sys.argv[2]
    except IndexError:
        new_file_name = 'solution.md'

    org_file = path + org_file_name
    new_file = path + new_file_name

    first_name = 'Yuval'
    last_name = 'Nurick'

    clear_file(new_file)
    with open(org_file, 'r') as ofh:
        with open(new_file, 'a') as nfh:
            for line in ofh:
                nfh.write(first_name + ' ' + line.rstrip() + ' ' + last_name
                          + '\n')


if __name__ == '__main__':
    main()
