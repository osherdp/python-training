import sys

FILE_NAME = 1
ID = 0
PASSWORD = 1
BALANCE = 2


def update_file(file_name, dictionary):
    """ update the file atm.txt with all the changes in dictionary
    """
    with open(file_name, 'w') as atm_file:
        for key in dictionary:
            temp_dict = dictionary[key]  # temp_dict = {password: balance}
            for pw, bal in temp_dict.items():
                atm_file.write('{} {} {}\n'.format(key, pw, bal))


def change_password(dictionary, consumer_id):
    """
    Ask for a new password and change the dictionary accordingly
    :param dictionary: old_dictionary
    :param consumer_id: the current user's ID
    :return: the updated dictionary
    """
    new_pass = input('Please enter a new password: ')
    temp_dict = dictionary[consumer_id]  # temp_dict = {password: balance} of the current user
    for password, balance in temp_dict.items():
        temp_dict[new_pass] = temp_dict.pop(password)  # update the new password
    dictionary[consumer_id] = temp_dict  # update the dictionary
    return dictionary


def cash_deposit(dictionary, consumer_id):
    """
    Ask for the amount to deposit and change the dictionary accordingly
    If the user enters a negative amount, the ATM informs it
    :param dictionary: old_dictionary
    :param consumer_id: the current user's ID
    :return: the updated dictionary
    """
    cash = input('Please enter the amount of money you wish to deposit: ')
    cash = int(cash)
    if cash < 0:
        print('Can''t do this, please enter a positive number!')
    temp_dict = dictionary[consumer_id]  # temp_dict = {password: balance} of the current user
    for password, balance in temp_dict.items():
        balance += cash  # add the cash amount to his balance
        temp_dict[password] = balance  # update the dictionary
    dictionary[consumer_id] = temp_dict  # update the dictionary
    return dictionary


def cash_withdrawal(dictionary, consumer_id):
    """
    Ask for the amount to withdraw and change the dictionary accordingly
    If the user enters a negative amount, the ATM informs it
    :param dictionary: old_dictionary
    :param consumer_id: current user's ID
    :return: the updated dictionary
    """
    cash = input('Please enter the amount of money you wish to withdraw: ')
    cash = int(cash)
    if cash < 0:
        print('Can''t do this, please enter a positive number! ')
    temp_dict = dictionary[consumer_id]  # temp_dict = {password: balance} of the current user
    for password, balance in temp_dict.items():
        balance -= cash  # sub the cash amount from his balance
        temp_dict[password] = balance  # update the dictionary
    dictionary[consumer_id] = temp_dict  # update the dictionary
    return dictionary


def check_the_balance(dictionary, consumer_id):
    """
    Go through the dictionary and find the user's balance
    :param dictionary: dictionary
    :param consumer_id: current user's ID
    :return: the balance of the account
    """
    temp_dict = dictionary[consumer_id]  # temp_dict = {password: balance} of the current user
    for password, balance in temp_dict.items():
        return balance
    return None  # the program never reaches to this point


def enter_password(dictionary, consumer_id):
    """
    Ask for the user's password. If the user makes 3 mistakes, the function returns False
    Otherwise, return True
    :param dictionary:
    :param consumer_id: current user's ID
    :return: True/False
    """
    times = 3  # the user have 3 tries to enter his password correctly
    while True:
        password = input('Please enter your ATM password: ')
        temp_dict = dictionary[consumer_id]  # temp_dict = {password: balance}
        for pw, balance in temp_dict.items():
            if pw == password:
                print('OK, we proceed ')
                return True
            else:
                print('Wrong password, you have {} more tries'.format(times - 1))
                times -= 1
                if times == 0:
                    return False


def who_are_you(dictionary):
    """
    Ask from the user to enter his ID.
    If the ID exist in the dictionary (in the atm.txt) so return the ID.
    If the ID is -1, return also the ID.
    If the ID doesn't exist in the dictionary, keep asking for an different ID.
    :param dictionary:
    :return: consumer_id (that exist in the file, or -1)
    """
    while True:
        consumer_id = input('Please enter you ID: ')
        if (consumer_id in dictionary) or (consumer_id == '-1'):
            return consumer_id
        else:
            print('Sorry, you are not in the system, please try again! ')


def read_file(file_name):
    """
    Read from the file (atm.txt) line by line, and create dictionary: {ID: {password: balance}}
    I used try and except. If the file doesn't exist, the program won't collapse
    :param file_name:
    :return: dictionary
    """
    try:
        dictionary = {}
        with open(file_name, 'r') as atm_file:
            for line in atm_file:
                my_list = line.split()
                dictionary[my_list[ID]] = {my_list[PASSWORD]: int(my_list[BALANCE])}
        return dictionary
    except Exception as error:
        print(error)


def main():
    """
    1) call read_file(file_name) to create dictionary
    2) call who_are_you(dictionary) to recognize the user
    3) call enter_password(dictionary, consumer_id)
        a) if the password is correct in 3 tries then let the user choose an action
        b) else: Message about it, and go to step 2)
    :return:
    """
    file_name = sys.argv[FILE_NAME]
    dictionary = read_file(file_name)
    while True:
        consumer_id = who_are_you(dictionary)
        if consumer_id == '-1':
            print('Turning off the ATM...')
            break
        if enter_password(dictionary, consumer_id) is True:  # if the password is correct
            while True:
                action = input('Press:\n1 -- see balance\n2 -- cash withdraw\n3 -- cash deposit\n' +
                               '4 -- change password\nSTOP --  if you are done\n')
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
