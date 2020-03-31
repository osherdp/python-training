import sys
import os

PATH = 1


def open_file(directory, mode):
    input_file = open(directory, mode)
    return input_file


def main():
    try:
        directory = sys.argv[PATH]
        if ".txt" in directory:
            pass
        else:
            print(os.listdir(directory))
            file_name = input("Enter file name from list above: ")
            directory += "\\" + file_name

    except Exception as error_message:
        print(error_message)
        directory = input("Enter the file's directory you want to work with:")

    input_file = open_file(directory, 'r')
    new_data = ''
    for line in input_file:
        new_data += "Roei " + line.replace("\n", "") + " Zolberg" + "\n"
        print(line)
        print(new_data)
    input_file.close()

    input_file = open_file(directory, 'w')
    input_file.write(new_data)
    input_file.close()

    return

if __name__ == '__main__':
    main()
