import sys
from atm import ATM

CUSTOMERS_FILE_LOCATION = 1
NAME_INDEX = 0
MENU_CHECK = '1'
MENU_DEPOSIT = '2'
MENU_WITHDRAW = '3'
MENU_CHANGE_PASS = '4'
WELCOME_MESSAGE = 'Welcome to the ATM! \n ' \
                  'To exit enter -1, ' \
                  'otherwise please enter your customer ID:'
HELLO_MESSAGE = 'Hello {}'
MENU_MESSAGE = 'To check your balance, press 1 \n' \
               'To make a deposit, press 2 \n' \
               'To make a withdrawal, press 3 \n' \
               'To change your password, press 4 \n '


def main():
    atm = ATM(customers_file_path)
    flag = True
    while flag:
        cust_ID = input(WELCOME_MESSAGE)
        if cust_ID in atm.customers.keys():
            print(HELLO_MESSAGE.format(atm.customers[cust_ID][NAME_INDEX]))
            user_input = input(MENU_MESSAGE)
            if user_input == MENU_CHECK:
                atm.check_balance(cust_ID)
            elif user_input == MENU_DEPOSIT:
                atm.deposit(cust_ID)
            elif user_input == MENU_WITHDRAW:
                atm.withdraw(cust_ID)
            elif user_input == MENU_CHANGE_PASS:
                atm.change_password(cust_ID)
            else:
                print('Invalid choice')
        elif cust_ID == '-1':
            print('Goodbye!')
            flag = False
        else:
            print('ID does not exist')
    atm.update_file()


if __name__ == '__main__':
    try:
        customers_file_path = sys.argv[CUSTOMERS_FILE_LOCATION]
    except IndexError:
        raise ValueError('No Path Given')
    main()
