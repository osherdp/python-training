def add_first_and_last_name(old_line):
    """ recieve str line from the text file and
    return it with first name at the beginning and last name at the end
    """
    first_name = 'Yoav'
    last_name = 'Doron'
    new_line = first_name + ' ' + old_line + ' ' + last_name
    return new_line


old_file = open(r'C:\text files stam ecercise\stam exercise old file.txt', 'r')
new_file = open(r'C:\text files stam ecercise\stam exercise new file.txt', 'a',)
# add to the empty file the lines from the old file, according to the exercise demands
for line in old_file:
    new_file.write(add_first_and_last_name(line))


