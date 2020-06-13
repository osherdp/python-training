# Stam Exercise

# Goals

# 1. Using files in python.
# 2. String manipulation.

# Introduction

# In this exercise, you should write a program that receive a file name and will:
# 1. Add your first name to the beginning of each line.
# 2. Add your last name to the end of each line.

# Then you should save the newly created file to a new location.

# Recommendations & Notes

# * Use the `dir()` function on the open file object to see what attributes does it have.
# * Read about `readlines` method of file-objects.
# -----------------------------------------------------------------------------------------

import sys


def stam_func(file):
    # the function receives a file path and
    # makes a new file with my first and last name in the start and end of every line accordingly

    input_file3 = open(file)
    line_by_line_file = input_file3.readline()
    input_file2 = open(r'C:\Users\yaniv\OneDrive\Desktop\python_targil_stam\targil_stam_metukan.txt', 'a')
    while line_by_line_file != '':
        line_by_line_file = input_file3.readline()
        str1 = "yaniv {} starkman".format(line_by_line_file)
        str1 = str1.replace("\n", "")
        input_file2.write(str1 + "\n")
    print("Done")


def main():
    file = sys.argv[1]
    stam_func(file)


if __name__ == "__main__":
    main()
