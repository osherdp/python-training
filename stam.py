# -*- coding: utf-8 -*-
__author__ = 'Yaron'

import sys
INPUT_FILENAME_ARG_NUM = 1
OUTPUT_FILENAME_ARG_NUM = 2


def add_name_to_line(text_lines, pre_text, succeeding_text):
    """
    This function adds the string received in pre_text to the beginning of each
    line in text_lines list of strings and adds succeeding_text to the end of each line
    """
    for ind in range(len(text_lines)):
        text_lines[ind] = pre_text+' '+text_lines[ind].rstrip('\n')+' '+succeeding_text+'\n'
    return text_lines


def main():
    """
    This python file copies the contents of the file given in the first argument
    into the file given in the second argument while adding my first name before
    each line and last name after the line
    """
    try:
        input_f_name = sys.argv[INPUT_FILENAME_ARG_NUM]
        output_f_name = sys.argv[OUTPUT_FILENAME_ARG_NUM]
        in_file = open(input_f_name, 'r')
        out_file = open(output_f_name, 'w')
    except Exception as e:
        print(e)
        return
    text = in_file.readlines()

    new_text = add_name_to_line(text, 'Yaron', 'Cohen')
    out_file.write(''.join(new_text))


if __name__ == '__main__':
    main()
