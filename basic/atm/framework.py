import sys
from atm import ATM

CUSTOMERS_FILE_LOCATION = 1
NAME_INDEX = 0
MENU_CHECK = 1
MENU_DEPOSIT = 2
MENU_WITHDRAW = 3
MENU_CHANGE_PASS = 4
WELCOME_MESSAGE = 'Welcome to the ATM! \n ' \
                  'To exit enter -1, ' \
                  'otherwise please enter your customer ID:'
HELLO_MESSAGE = 'Hello {}'
MENU_MESSAGE = 'To check your balance, press 1 \n' \
               'To make a deposit, press 2 \n' \
               'To make a withdrawal, press 3 \n' \
               'To change your password, press 4 \n '


# def get_customers(file):
#     customers = {}
#     for line in file.readlines():
#         data = line.strip().split(';')
#         customers[data[ID_INDEX]] = [data[NAME_INDEX],
#                                      data[PASSWORD_INDEX],
#                                      int(data[BALANCE_INDEX])]
#     return customers


# def check_balance(customers, ID):
#     print('Your balance is: {}'.format(customers[ID][BALANCE_INDEX]))


# def deposit(customers, ID):
#     try:
#         amount = int(input('Enter amount to deposit: '))
#         if amount > 0:
#             customers[ID][BALANCE_INDEX] += amount
#         else:
#             print('Please enter a positive number')
#     except ValueError:
#         print('Please enter an integer')


# def withdraw(customers, ID):
#     try:
#         amount = int(input('Enter amount to withdraw: '))
#         if amount > 0:
#             customers[ID][BALANCE_INDEX] -= amount
#         else:
#             print('Please enter a positive number')
#     except ValueError:
#         print('Please enter an integer')


# def change_password(customers, ID):
#     tries = 0
#     while tries < 3:
#         password = input('Enter old password: ')
#         if password == customers[ID][PASSWORD_INDEX]:
#             customers[ID][PASSWORD_INDEX] = input('Enter new password: ')
#             break
#         else:
#             print('Incorrect password, try again')
#             tries += 1
#     if tries == 3:
#         print('Exceeded number of tries allowed')


# def update_file(customers):
#     with open(customers_file_path, 'w') as customers_file:
#         for key in customers:
#             customers_file.writelines(
#                 CUSTOMER_LINE_FORMAT.format(customers[key][NAME_INDEX],
#                                             customers[key][PASSWORD_INDEX],
#                                             customers[key][BALANCE_INDEX],
#                                             key))


def main():
    atm = ATM()
    customers = atm.get_customers(customers_file_path)
    flag = True
    while flag:
        cust_ID = input(WELCOME_MESSAGE)
        if cust_ID in customers.keys():
            print(HELLO_MESSAGE.format(customers[cust_ID][NAME_INDEX]))
            user_input = input(MENU_MESSAGE)
            if user_input == MENU_CHECK:
                atm.check_balance(customers, cust_ID)
            elif user_input == MENU_DEPOSIT:
                atm.deposit(customers, cust_ID)
            elif user_input == MENU_WITHDRAW:
                atm.withdraw(customers, cust_ID)
            elif user_input == MENU_CHANGE_PASS:
                atm.change_password(customers, cust_ID)
            else:
                print('Invalid choice')
        elif cust_ID == '-1':
            print('Goodbye!')
            flag = False
        else:
            print('ID does not exist')
    atm.update_file(customers, customers_file_path)


if __name__ == '__main__':
    try:
        customers_file_path = sys.argv[CUSTOMERS_FILE_LOCATION]
    except IndexError:
        raise ValueError('No Path Given')
    main()
