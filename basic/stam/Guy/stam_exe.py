"""
Goals:
Using files in python.
String manipulation.
"""
"""
Introduction:
In this exercise, you should write a program that receive a file name and will:
Add your first name to the beginning of each line.
Add your last name to the end of each line.
Then you should save the newly created file to a new location.
"""


def add_my_name(filename,destfile, firstname, lastname):
    """
    this function receives a source file name, and first+last name
    creates a new file with first name at the beginning of each line and last name
    at the end of each line.
    this new file location will be according to input destfile
    """
    fd_in = open(filename, 'r')
    fd_out = open(destfile, 'w')
    for line in fd_in:
        """remove \n from each line"""
        fd_out.write(firstname + ' ' + line[0:len(line) - 1:] + ' ' + lastname + "\n")
    fd_out.close()
    fd_in.close()


def main():
    firstname = 'Guy'
    lastname = 'Haramati'
    filename = r"C:\guy\python\alice.txt"
    destfile = r"C:\guy\python\add_my_name.txt"
    print 'My name is {} {}'.format(firstname, lastname)
    add_my_name(filename,destfile, firstname, lastname)


if __name__ == '__main__':
    main()
