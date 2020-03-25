# -*- coding: utf-8 -*-
__author__ = 'Yaron'

import sys
INPUT_FILENAME_ARG_NUM = 1
OUTPUT_FILENAME_ARG_NUM = 2


def main():
    """
    This python file copies the contents of the file given in the first argument
    into the file given in the second argument while adding my first name before
    each line and last name after the line
    """
    try:
        input_f_name = sys.argv[INPUT_FILENAME_ARG_NUM]
        output_f_name = sys.argv[OUTPUT_FILENAME_ARG_NUM]
    except Exception as e:
        print(e)
    text = read_file_lines(input_f_name)

    new_text = add_name_to_line(text, 'Yaron', 'Cohen')

    create_file(output_f_name, new_text)
    # try:
    #     input_f_name = sys.argv[INPUT_FILENAME_ARG_NUM]
    #     output_f_name = sys.argv[OUTPUT_FILENAME_ARG_NUM]
    #     in_file = open(input_f_name, 'r')
    #     out_file = open(output_f_name, 'w')
    # except Exception as e:
    #     print(e)
    #
    # for line in in_file:
    #     out_file.write('Yaron '+line.rstrip()+' Cohen\n')


if __name__ == '__main__':
    main()
