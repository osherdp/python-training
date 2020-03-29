import sys

FILE_NAME = 1
ID = 0
PASSWORD = 1
BALANCE = 2


def update_file(file_name, dictionary):
    PASSWORD = 0
    BALANCE = 1
    with open(file_name, 'w') as atm_file:
        for key in dictionary:
            my_list = dictionary[key]
            atm_file.write('{} {} {}\n'.format(key, my_list[PASSWORD],
                                               my_list[BALANCE]))


def change_password(dictionary, consumer_id):
    PASSWORD = 0
    new_pass = input('Please enter a new password: ')
    my_list = dictionary[consumer_id]
    my_list[PASSWORD] = new_pass
    dictionary[consumer_id] = my_list  # update the dictionary
    return dictionary


def cash_deposit(dictionary, consumer_id):
    BALANCE = 1
    cash = input('Please enter the amount of money you wish to deposit: ')
    cash = int(cash)
    if cash < 0:
        print("Can't do this, please enter a positive number! ")
    my_list = dictionary[consumer_id]
    temp_list = my_list  # create temporary list
    temp_list[BALANCE] += cash  # add the cash amount
    my_list = temp_list
    dictionary[consumer_id] = my_list  # update the dictionary
    return dictionary


def cash_withdrawal(dictionary, consumer_id):
    BALANCE = 1
    cash = input('Please enter the amount of money you wish to withdraw: ')
    cash = int(cash)
    if cash < 0:
        print("Can't do this, please enter a positive number! ")
    my_list = dictionary[consumer_id]
    temp_list = my_list  # create temporary list
    temp_list[BALANCE] -= cash  # sub the cash amount
    my_list = temp_list
    dictionary[consumer_id] = my_list  # update the dictionary
    return dictionary


def check_the_balance(dictionary, consumer_id):
    BALANCE = 1
    my_list = dictionary[consumer_id]
    return my_list[BALANCE]


def verify_password(dictionary, consumer_id):
    PASSWORD = 0
    times = 3  # the user have 3 tries to enter his password correctly
    while True:
        password = input('Please enter your ATM password: ')
        my_list = dictionary[consumer_id]
        if my_list[PASSWORD] == password:
            print('OK, we proceed ')
            return True
        else:
            print('Wrong password, you have {} more tries'
                  .format(times - 1))
            times -= 1
            if times == 0:
                return False


def who_are_you(dictionary):
    while True:
        consumer_id = input('Please enter you ID: ')
        if (consumer_id in dictionary) or (consumer_id == '-1'):
            return consumer_id
        else:
            print('Sorry, you are not in the system, please try again! ')


def read_file(file_name, dictionary):
    try:
        with open(file_name, 'r') as atm_file:
            for line in atm_file:
                my_list = line.split()
                dictionary[my_list[ID]] = \
                    [my_list[PASSWORD], int(my_list[BALANCE])]
                # dictionary = {ID: [password, balance]}
        return dictionary
    except Exception as error:
        print(error)


def main():
    file_name = sys.argv[FILE_NAME]
    dictionary = {}
    dictionary = read_file(file_name, dictionary)
    while True:
        consumer_id = who_are_you(dictionary)
        if consumer_id == '-1':
            print('Turning off the ATM...')
            break
        if verify_password(dictionary, consumer_id) is True:
            while True:
                action = input('Press:\n1 -- see balance\n' +
                               '2 -- cash withdraw\n' +
                               '3-- cash deposit\n' +
                               '4 -- change password\n' +
                               'STOP --  if you are done\n')
                if action == '1':
                    balance = check_the_balance(dictionary, consumer_id)
                    print('Your balance is: {}'.format(balance))

                elif action == '2':
                    dictionary = cash_withdrawal(dictionary, consumer_id)
                    update_file(file_name, dictionary)

                elif action == '3':
                    dictionary = cash_deposit(dictionary, consumer_id)
                    update_file(file_name, dictionary)

                elif action == '4':
                    dictionary = change_password(dictionary, consumer_id)
                    update_file(file_name, dictionary)

                elif action == 'STOP':
                    print('Thank you, have a nice day!')
                    break

                else:
                    print('Wrong action, try again!')

        else:  # if the password was wrong for 3 times
            print('You failed 3 times, go home pretender!')


if __name__ == '__main__':
    main()
