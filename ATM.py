"""The script simulates ATM.

The script simulates ATM that preforms the following:
balance check, withdraw cash, deposit cash and
password change.
"""
import os
import sys


BALANCE = 1
PASSWORD = 0
ID_INDEX = 0
PATH_TO_FILE = 1
INDEX_START_OF_PASSWORD_AND_BALANCE = 1


def file_to_dic(filename):
    """Insert the ATM  data from the file into the dictionary

    Args:
        filename (str): file name ending with '.txt'

    Returns:
        dictionary: key=id and value=[password, balance]

    """
    atm = {}
    with open(filename, 'r') as file:
        for line in file:
            details = line.strip().split(' ')
            atm[details[ID_INDEX]] = details[INDEX_START_OF_PASSWORD_AND_BALANCE:]

    return atm


def operation_of_atm(id, atm_dic):
    """Performs the desired ATM operation for the inserted id.

    Args:
        id (str): the id for which you want the ATM to work
        atm_dic (dict): dictionary containing all ATM information

    Returns:
        dictionary: dictionary with the updated values
            after performing the desired action
    """
    if id in atm_dic:
        action = input("enter number of action:\n"
                       "1- for check the balance\n"
                       "2- for cash withdrawal\n"
                       "3- for cash deposit\n"
                       "4- for change password\n")

        if action == '1':
            print(f"your balance is: {atm_dic[id][BALANCE]}")

        elif action == '2':
            money = input("enter the amount you want to withdraw\n")
            if int(atm_dic[id][BALANCE]) > int(money):
                atm_dic[id][BALANCE] = str(int(atm_dic[id][BALANCE]) - int(money))
            else:
                print('The account balance is less than the '
                      'then the amount you wanted to withdraw')

        elif action == '3':
            money = input("enter the amount you want to deposit\n")
            atm_dic[id][BALANCE] = str(int(atm_dic[id][BALANCE]) + int(money))

        elif action == '4':
            password = input('enter new password\n')
            atm_dic[id][PASSWORD] = password

        else:
            print('action not detected')

    else:
        print('There is an error in the ID you entered')


def main():
    """Do the ATM operation and save the changes

    will do the desired ATM operation according to an
    ID that has been accepted until receive -1 as an ID.
    all the changes will be saved to the ATM.

    Arg:
        id (int): 9 digits ID (example: 322781145)

    Raises:
        Exception as e: No such file or directory
            if the path to the file not exist will be an error.
    """
    try:
        atm_dic = file_to_dic(sys.argv[PATH_TO_FILE])
        id = input('please enter your ID\n')

        while id != '-1':
            operation_of_atm(id, atm_dic)
            id = input('please enter your ID\n')

        with open(sys.argv[PATH], 'w') as newfile:
            for id in atm_dic:
                newfile.writelines(f"{id} {atm_dic[id][PASSWORD]} "
                                   f"{atm_dic[id][BALANCE]}\n")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
