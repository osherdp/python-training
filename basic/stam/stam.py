import sys
import os


def main():
    """take file name from argument and copies it to file name in second
    argument in addition - adds 'first_name' to the beginning םf each line
    and 'last_name' to the end of each line """
    path = os.path.dirname(sys.argv[0]) + '/'
    try:
        org_file_name = sys.argv[1]
    except IndexError:
        print('Not enough input arguments, using README.MD as input file')
        org_file_name = 'README.md'
    try:
        new_file_name = sys.argv[2]
    except IndexError:
        print('Not enough input arguments, using solution.md as output file')
        new_file_name = 'solution.md'

    org_file = path + org_file_name
    new_file = path + new_file_name

    first_name = 'Yuval'
    last_name = 'Nurick'

    # ofh is original file handler and nfh is new file  handler
    with open(org_file, 'r') as ofh:
        with open(new_file, 'w') as nfh:
            for line in ofh:
                nfh.write(f'{first_name} {line.rstrip()} {last_name}\n')


if __name__ == '__main__':
    main()
