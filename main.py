from Atm import Atm

FILE_PATH = r'C:\Users\mayar\Desktop\Python\ATM\costumers.txt'


def main():
    atm = Atm(FILE_PATH)
    atm.start_action()


if __name__ == '__main__':
    main()
