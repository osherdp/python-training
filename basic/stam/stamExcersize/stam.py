import sys

ORIGINAL_FILE_LOCATION = 1
NEW_LINE_FORMAT = 'Maya {} Gal-Yam\n'
NEW_FILE_NAME = 'newfile.txt'


# def get_file():
#     """gets the files passed in if args are valid"""
#     try:
#         originalfile_path = sys.argv[ORIGINAL_FILE_LOCATION]
#         if path.exists(originalfile_path) and path.isfile(originalfile_path):
#             file_to_get = open(originalfile_path, 'r')
#         else:
#             print("Given path isn't a file")
#             sys.exit()
#     except IndexError:
#         print('No path given')
#         sys.exit()
#     return file_to_get
#
#
# def create_new():
#     """opens/creates new file in the working directory"""
#     newfile_path = path.join(os.getcwd(), NEW_FILE_NAME)
#     file_to_create = open(newfile_path, 'w')
#     return file_to_create


def manipulate(original, new):
    for line in original.readlines():
        new_line = NEW_LINE_FORMAT.format(line.strip())
        new.writelines(new_line)


def main():
    try:
        with open(originalfile_path, 'r') as original_file:
            with open(NEW_FILE_NAME, 'w') as new_file:
                manipulate(original_file, new_file)
    except Exception as e:
        print(e)
        sys.exit()


if __name__ == '__main__':
    try:
        originalfile_path = sys.argv[ORIGINAL_FILE_LOCATION]
    except IndexError:
        raise ValueError('No Path Given')
    main()
