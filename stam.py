import sys
import os

"""
:return 
True if the path is a file,
otherwise return false
arg:
path- the path received as parameter to the script
"""


def correct_parameter(path):
    if not os.path.isfile(path):
        print("your file not foud")
        return False

    return True


"""
the function adds a first name at the beginning of each line
and a last name to the end of each line.
args:
filename- the path to the original file
newfilename- the path to the new file
"""


def add_name(filename, newfilename):
    with open(filename, 'r') as file:
        for line in file:
            with open(newfilename, 'a') as newfile:
                newfile.write(f"keren {line.strip()} kayrich\n")


def main():
    filename = sys.argv[1]
    newfile = sys.argv[2]
    if correct_parameter(filename):
        add_name(filename, newfile)
        with open(newfile, 'r') as file:
            print(file.read())
    else:
        print("please check your parameters")


if __name__ == '__main__':
    main()
