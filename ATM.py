# -*- coding: utf-8 -*-
__author__ = 'Yaron'

import sys
INPUT_FILENAME_ARG_NUM = 1


def check_balance(customer_data):
    print('Your balance is {}NIS'.format(customer_data[1]))
    return customer_data


def change_password(customer_data):
    new_pass = input('Type new 4 digit password:\n')
    if len(new_pass) != 4:
        print('Password change failed')
        return customer_data
    customer_data[0] = new_pass
    return customer_data


def cash_withdrawal(customer_data):
    withdrawal_sum = input('How much would you like to withdraw?\n')
    try:
        withdrawal_int_sum = int(withdrawal_sum)
        if withdrawal_int_sum < 0:
            withdrawal_int_sum = 0
            print('Unaccepted value')
    except ValueError:
        withdrawal_int_sum = 0
        print('Unaccepted value')
    customer_sum = int(customer_data[1]) - withdrawal_int_sum
    customer_data[1] = str(customer_sum)
    # print('Your balance is {}NIS'.format(customer_data[1]))
    return customer_data


def cash_deposit(customer_data):
    deposit_sum = input('How much would you like to deposit?\n')
    try:
        deposit_int_sum = int(deposit_sum)
        if deposit_int_sum < 0:
            deposit_int_sum = 0
            print('Unaccepted value')
    except ValueError:
        deposit_int_sum = 0
        print('Unaccepted value')
    customer_sum = int(customer_data[1]) + deposit_int_sum
    customer_data[1] = str(customer_sum)
    # print('Your balance is {}NIS'.format(customer_data[1]))
    return customer_data


OPERATIONS = {'cb': check_balance, 'cw': cash_withdrawal,
              'cd': cash_deposit, 'cp': change_password}


def load_customer_list(input_filename):
    """
    This function extracts the customer list as a dictionary from the input
    file
    """
    with open(input_filename, 'r') as in_file:
        loaded_text = in_file.readlines()

    customer_id = []
    customer_data = []
    for line in loaded_text:
        entry = line.split()
        # print(entry)
        try:
            int(entry[2])  # used solely to verify entry has three values
            # and that the third one is an integer
            customer_id.append(entry[0])
            customer_data.append(entry[1:3])
            # print(customer_data)
        except IndexError or ValueError:
            print('Error loading customer - continuing to next one')

    customer_list = dict(zip(customer_id, customer_data))
    return customer_list


def save_customer_list(output_filename, customer_list):
    """
    This function saves the customer list in output file as a single
    line for each customer
    """
    print('Saving customer file...')
    output_list = ['{} {}\n'.format(key, ' '.join(customer_list.get(key)))
                   for key in customer_list]
    with open(output_filename, 'w') as out_file:
        out_file.writelines(output_list)
    return


def main():
    """
    This is the main program for running an ATM
    """
    try:
        input_f_name = sys.argv[INPUT_FILENAME_ARG_NUM]
    except Exception as e:
        print(e)
        print('This simply means not enough inputs')
        return
    customer_list = load_customer_list(input_f_name)
    # print(customer_list)

    while True:
        entry_id = input('Enter ID\n')
        if entry_id == '-1':
            break
        if not(entry_id in customer_list):
            print('ID not a recognized customer')
            continue
        customer_data = customer_list[entry_id]

        entry_pass = input('Enter password:\n')
        if entry_pass != customer_data[0]:
            print('Wrong password. The police has been informed.')
            continue
        action = input('What action would you like to perform? ('
                       'cb-check balance, cw-cash withdrawal, cd-cash'
                       ' deposit or cp-change password) \n')
        if not (action in OPERATIONS):
            print('Operation not recognized')
            continue
        operation = OPERATIONS.get(action)
        customer_list[entry_id] = operation(customer_data)
        print("Operation complete\n")

    save_customer_list(input_f_name, customer_list)


if __name__ == '__main__':
    main()
