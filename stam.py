# -*- coding: utf-8 -*-
__author__ = 'Yaron'

import sys
INPUT_FILENAME_ARG_NUM = 1
OUTPUT_FILENAME_ARG_NUM = 2
FIRST_NAME = 'Yaron'
LAST_NAME = 'Cohen'


def add_name_to_line(text_lines, pre_text, succeeding_text):
    """
    This function adds the string received in pre_text to the beginning of each
    line in text_lines list of strings and adds succeeding_text to
    the end of each line
    """
    out_text = ['{} {} {}\n'.format(pre_text, line.rstrip('\n'),
                                    succeeding_text)
                for line in text_lines]
    return out_text


def main():
    """
    This python file copies the contents of the file given in the first
    argument into the file given in the second argument while adding
    my first name before each line and last name after the line
    """
    try:
        input_f_name = sys.argv[INPUT_FILENAME_ARG_NUM]
        output_f_name = sys.argv[OUTPUT_FILENAME_ARG_NUM]
    except Exception as e:
        print(e)
        print('This simply means not enough inputs')
        return
    with open(input_f_name, 'r') as in_file:
        text = in_file.readlines()

    new_text = add_name_to_line(text, FIRST_NAME, LAST_NAME)

    with open(output_f_name, 'w') as out_file:
        out_file.writelines(new_text)


if __name__ == '__main__':
    main()
