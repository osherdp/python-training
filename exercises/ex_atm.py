"""ATM Exercise"""

import sys

FILE_PATH_INDEX = 1  # describe placement of the argument containing file path.
PASSWORD_INDEX = 0
BALANCE_INDEX = 1
END_ATM_SERVICE = "-1"


def store_file_content(file_path):
    """Read file and move atm information to dictionary.
    The lines of the file will contain user's id, balance and password,
    with comma's separating them.

    Args:
        file_path (str): path to atm information file.

    Return:
        dict. with user's id as keys,
        and user's password and balance in a list as values.
    """
    try:
        atm_options = {}
        with open(file_path, 'r') as file_pointer:
            for line in file_pointer:
                line_list = line.rstrip().split(',')
                atm_options.update({line_list[0]: [line_list[1],
                                                   float(line_list[2])]})

        return atm_options

    except FileNotFoundError:
        print(f"Can't access the path to the file you have entered:"
              f"{file_path}")


def get_user_id(atm_info):
    while True:
        user_id_input = input("Enter costumer ID, to turn off the ATM enter "
                              "-1 -> ")
        if user_id_input == END_ATM_SERVICE:
            atm_info = None
            return user_id_input, atm_info
        elif user_id_input in atm_info:
            return user_id_input, atm_info
        else:
            print("Invalid ID")


def atm_service(file_path, atm_options, user_id_input):
    user_option = input("Enter wanted option, to turn off the ATM enter -1"
                        + "\nEnter 'options' to see ATM's options. -> ")
    user_option = user_option.lower()
    if user_option == END_ATM_SERVICE:
        update_file_content(file_path, atm_options)
        atm_options = None
    elif user_option == "options":
        print("The ATM allow the following options to a using costumer:" +
              "\n1. 'check' the balance.\n2. cash 'withdrawal'." +
              "\n3. cash 'deposit'.\n4. 'change' password.")
    else:
        atm_options = check_input(atm_options,
                                  user_option, user_id_input)
    return atm_options


def check_input(atm_info, user_input, user_id):
    """Check user option input, and act accordingly if the input is correct.

    Args:
        atm_info (dict): the dictionary, containing all the atm information.
        user_input (str): the option choice of the user.
                          there are four options- check, withdrawal,
                          deposit and change
        user_id (str): the id of the user, to find him in the dictionary.

    Return:
        The new changed dictionary of atm information.
    """
    if user_input == "check":
        print(f"You'r balance: {atm_info[user_id][BALANCE_INDEX]}")

    elif user_input == "withdrawal":
        atm_info = withdrawal(atm_info, user_id)

    elif user_input == "deposit":
        atm_info = deposit(atm_info, user_id)

    elif user_input == "change":
        check_balance(atm_info, user_id)

    else:
        print("Invalid input")

    return atm_info


def withdrawal(atm_info, user_id):
    """function to withdraw money from atm dict"""
    withdraw = input("Enter how much you want to withdrawal -> ")
    if float(withdraw) > 0:
        atm_info[user_id][BALANCE_INDEX] -= float(withdraw)
        print("You have withdrawn: " + withdraw)
    else:
        print("invalid withdrawal input")
    return atm_info


def deposit(atm_info, user_id):
    """function to deposit money to the atm dict"""
    user_deposit = input("Enter how much you want to deposit -> ")
    if float(user_deposit) > 0:
        atm_info[user_id][BALANCE_INDEX] += float(user_deposit)
        print("Deposit succeeded")
    else:
        print("invalid deposit input")
    return atm_info


def check_balance(atm_info, user_id):
    """function to check user's balance in the atm dict"""
    new_password = input("Enter you'r new password -> ")
    atm_info[user_id][PASSWORD_INDEX] = new_password
    print("Password changed to: " + new_password)


def update_file_content(file_path, atm_info):
    """Move the updated dictionary to the atm information file.

    Args:
        file_path (str): path to atm information file.
        atm_info (dict): the dictionary, containing all the atm
                               information.
    """
    try:
        with open(file_path, 'w') as file_pointer:
            for key in atm_info:
                user_password = atm_info[key][0]
                user_balance = atm_info[key][1]
                file_pointer.write(','.join([str(key), user_password,
                                             str(user_balance)]) + "\n")
        print("Changes saved :)")

    except FileNotFoundError:
        print(f"Can't access the path to the file you have entered:"
              f"{file_path}")


def main():
    file_path = sys.argv[FILE_PATH_INDEX]
    atm_options = store_file_content(file_path)

    user_id_input, atm_options = get_user_id(atm_options)

    while atm_options is not None:
        atm_options = atm_service(file_path, atm_options,
                                  user_id_input)


if __name__ == '__main__':
    main()
