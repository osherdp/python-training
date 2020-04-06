import sys
import os


def open_file(directory, mode):
    input_file = open(directory, mode)
    return input_file


def main():
    try:
        directory = sys.argv[1]
        if ".txt" in directory:
            pass
        else:
            print(os.listdir(directory))
            file_name = input("Enter file name from list above: ")
            directory += "\\" + file_name

    except IndexError:
        print("Index error")
        directory = input("Enter the file's directory you want to work with:")


    with open(directory) as input_file:
        new_data = ''
        for line in input_file:
            new_data += "Roei " + line.replace("\n", "") + " Zolberg" + "\n"
            print(line)
            print(new_data)

    with open(directory, 'w') as input_file:
        input_file.write(new_data)


if __name__ == '__main__':
    main()
