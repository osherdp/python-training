import sys


def add_my_first_last(recive_list):
    ret_list = []
    first = "Yuval"
    last = "virniki"
    for i in recive_list:
        i = i[:-1]
        i = first + i
        i += last
        ret_list += [i]
    return ret_list


file_name = sys.argv[1]
output_path = sys.argv[2]
lines_lst = []
with open(file_name, "r") as input_f:
    lines_lst = input_f.readlines()
lines_lst = add_my_first_last(lines_lst)
with open(output_path, "w+") as output_f:
    for line in lines_lst:
        output_f.write(line + "\n")
