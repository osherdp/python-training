import sys

CUSTOMERS_FILE_LOCATION = 1
NAME_INDEX = 0
PASSWORD_INDEX = 1
BALANCE_INDEX = 2
ID_INDEX = 3
CUSTOMER_LINE_FORMAT = '{};{};{};{}\n'
WELCOME_MESSAGE = 'Welcome to the ATM! \n ' \
                  'To exit enter -1, ' \
                  'otherwise please enter your customer ID:'
MENU_MESSAGE = 'To check your balance, press 1 \n' \
               'To make a deposit, press 2 \n' \
               'To make a withdrawal, press 3 \n' \
               'To change your password, press 4 \n '


def get_customers(file):
    customers = {}
    for line in file.readlines():
        data = line.strip().split(';')
        customers[data[ID_INDEX]] = [data[NAME_INDEX],
                                     data[PASSWORD_INDEX],
                                     int(data[BALANCE_INDEX])]
    return customers


def check_balance(customers, ID):
    print('Your balance is: {}'.format(customers[ID][BALANCE_INDEX]))


def deposit(customers, ID):
    try:
        amount = int(input('Enter amount to deposit: '))
        if amount > 0:
            customers[ID][BALANCE_INDEX] += amount
        else:
            print('Please enter a positive number')
    except ValueError:
        print('Please enter an integer')


def withdraw(customers, ID):
    try:
        amount = int(input('Enter amount to withdraw: '))
        if amount > 0:
            customers[ID][BALANCE_INDEX] -= amount
        else:
            print('Please enter a positive number')
    except ValueError:
        print('Please enter an integer')


def change_password(customers, ID):
    tries = 0
    while tries < 3:
        password = input('Enter old password: ')
        if password == customers[ID][PASSWORD_INDEX]:
            customers[ID][PASSWORD_INDEX] = input('Enter new password: ')
            break
        else:
            print('Incorrect password, try again')
            tries += 1
    if tries == 3:
        print('Exceeded number of tries allowed')


def update_file(file, customers):
    file.seek(0)
    file.truncate()
    for key in customers:
        file.writelines(
            CUSTOMER_LINE_FORMAT.format(customers[key][NAME_INDEX],
                                        customers[key][PASSWORD_INDEX],
                                        customers[key][BALANCE_INDEX],
                                        key))


def main():
    with open(customers_file_path, 'r+') as customers_file:
        customers = get_customers(customers_file)
        flag = True
        while flag:
            cust_ID = input(WELCOME_MESSAGE)
            if cust_ID in customers.keys():
                print('Hello {}'.format(customers[cust_ID][NAME_INDEX]))
                user_input = input(MENU_MESSAGE)
                if user_input == '1':
                    check_balance(customers, cust_ID)
                elif user_input == '2':
                    deposit(customers, cust_ID)
                elif user_input == '3':
                    withdraw(customers, cust_ID)
                elif user_input == '4':
                    change_password(customers, cust_ID)
                else:
                    print('Invalid choice')
            elif cust_ID == '-1':
                print('Goodbye!')
                flag = False
            else:
                print('ID does not exist')
        update_file(customers_file, customers)


if __name__ == '__main__':
    try:
        customers_file_path = sys.argv[CUSTOMERS_FILE_LOCATION]
    except IndexError:
        raise ValueError('No Path Given')
    main()
