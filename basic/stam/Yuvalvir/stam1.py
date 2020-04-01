import sys
import os


def add_my_first_last(w2):
    first = "Yuval"
    last = "virniki"
    for i in w2:
        i[:-2]
        i += first
        i[-1::-1]
        i += last
    return w2


file_name = sys.argv[1]
output_path = sys.argv[2]
if file_name == output_path:
    x = "r"
else:
    x = "r+"
file_name = open(file_name, x)
w = []
for line in file_name:
    w.append(file_name.readlines())
add_my_first_last(w)
output_path = open(output_path, 'w+')
z = 1
for line in output_path:
    if len(w) < z:
        output_path.write(w[z])
        z += 1
file_name.close()
output_path.close()
