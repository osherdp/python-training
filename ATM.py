import os
import sys


def file_to_dic(filename):
    atm = {}
    with open(filename, 'r') as file:
        for line in file:
            details = line.split(' ')
            atm[details[0]] = details[1:]

    return atm


def atm_machine(id, atm_dic):
    if atm_dic.get(ID):
        action = input("enter action- check the balance\\"
                       "cash withdrawal\\cash deposit"
                       "\\change password")

        if action == 'check the balance':
            print(f"your balance is: {atm_dic[id][2]}")

        elif action == 'cash withdrawal':
            money = input("enter the amount you want to withdraw")
            atm_dic[id][2] = atm_dic[id][2] - money

        elif action == 'cash deposit':
            money = input("enter the amount you want to deposit")
            atm_dic[id][2] = atm_dic[id][2] + money

        elif action == 'change password':
            password = input('enter new password')
            atm_dic[id][1] = password

        else:
            print('action not detected')

    else:
        print('there is an error i the ID you etered')


def main():
    if os.path.isfile(sys.argv[1]):
        atm_dic = file_to_dic(sys.argv[1])
        id = input('please enter your ID')
        while id != -1:
            atm_machine(id, atm_dic)
            id = input('please enter your ID')
    else:
        print('file not found')


if __name__ == '__main__':
    main()
