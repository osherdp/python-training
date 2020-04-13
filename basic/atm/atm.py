__author__ = 'Anat'

import sys

from pip._vendor.distlib.compat import raw_input

ID_POSITION_LINE = 0
PASSWORD_POSITION_LINE = 1
BALANCE_POSITION_LINE = 2
PASSWORD_POSITION_LIST = 0
BALANCE_POSITION_LIST = 1


def read_file(path):
    customer = {}
    with open(path, 'r') as file:
        for line in file:
            customer_info = line.split()
            id_file = customer_info[ID_POSITION_LINE]
            password = customer_info[PASSWORD_POSITION_LINE]
            try:
                balance = float(customer_info[BALANCE_POSITION_LINE])
                customer[id_file] = [password, balance]
            except TypeError:
                print("problem in balance")
    return customer


def check_balance(customer_info):
    print(customer_info[BALANCE_POSITION_LIST])


def cash_withdrawal(cash, customer_info):
    try:
        cash_new = float(cash)
        customer_info[BALANCE_POSITION_LIST] -= cash_new
    except ValueError:
        print("problem in cash input")


def cash_deposit(cash, customer_info):
    try:
        cash_new = float(cash)
        customer_info[BALANCE_POSITION_LIST] += cash_new
    except ValueError:
        print("problem in cash input")


def change_password(password, customer_info):
    if isinstance(password, str):
        customer_info[PASSWORD_POSITION_LIST] = password
    else:
        print("password in wrong format")


def save(path, customer):
    file_contant = ''
    new_line = ''
    with open(path, 'r') as file:
        for line in file:
            customer_info = line.split()
            id = customer_info[ID_POSITION_LINE]
            password_file = customer_info[PASSWORD_POSITION_LINE]
            balance_file = customer_info[BALANCE_POSITION_LINE]
            balance_value = str(customer[id][BALANCE_POSITION_LIST])
            password_value = str(customer[id][PASSWORD_POSITION_LIST])
            if password_value != password_file:
                line = line.replace(password_file, password_value)
            if balance_value != balance_file:
                line = line.replace(balance_file, balance_value)
            file_contant += line
    with open(path, 'w') as file:
        pass
    with open(path, 'w') as file:
        file.write(file_contant)


def password_check(password, customer_info):
    if password == customer_info[PASSWORD_POSITION_LIST]:
        return True
    return False


def main():
    path = sys.argv[1]
    customer = read_file(path)
    id = raw_input("enter id")
    while id != '-1':
        try:
            password_entered = input("enter password")
            if password_check(password_entered, customer[id]):
                check_balance(customer[id])
                cash = input("enter cash to withdraw")
                cash_withdrawal(cash, customer[id])
                cash = input("enter cash to deposit")
                cash_deposit(cash, customer[id])
                password_new = input("enter new password")
                change_password(password_new, customer[id])
            else:
                print("wrong password")
            id = input("enter id")
        except KeyError:
            print("no such id")
            id = input("enter id")
    if id == '-1':
        save(path, customer)


if __name__ == '__main__':
    main()
