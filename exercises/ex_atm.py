import sys

FILE_PATH_INDEX = 1
END_ATM_SERVICE = "-1"
PASSWORD_KEY = "password"
BALANCE_KEY = "balance"


def store_file_content(file_path):
    """Read file and move atm information to dictionary.

    The lines of the file will contain user's id, balance and password,
    with comma's separating them.

    Args:
        file_path (str): path to atm information file.

    Returns:
        dict. with user's id as keys,
            and user's password and balance in another dict as values.
    """
    try:
        atm_options = {}
        with open(file_path, 'r') as file_pointer:
            for line in file_pointer:
                line_list = line.rstrip().split(',')
                atm_options[line_list[0]] = {"password": line_list[1],
                                             "balance": float(line_list[2])}

        return atm_options

    except FileNotFoundError:
        print(f"Can't find the file you have entered:"
              f"{file_path}")


def get_user_id(atm_info):
    """Get user's id to get into atm"""
    while True:
        user_id_input = input("Enter costumer ID, to turn off the ATM enter "
                              "-1 -> ")
        if user_id_input == END_ATM_SERVICE or user_id_input in atm_info:
            return user_id_input

        else:
            print("Invalid ID")


def atm_service(file_path, atm_options, user_id_input):
    """Get user's wanted actions from the atm"""
    user_option = input("Enter wanted option, to turn off the ATM enter -1"
                        + "\nEnter 'options' to see ATM's options. -> ")
    user_option = user_option.lower()
    if user_option == END_ATM_SERVICE:
        update_file_content(file_path, atm_options)

    elif user_option == "options":
        print("The ATM allow the following options to a using costumer:" +
              "\n1 - check the balance.\n2 - cash withdrawal." +
              "\n3 - cash deposit.\n4 - change password.")

    else:
        check_input(atm_options, user_option, user_id_input)
    return user_option


def check_input(atm_info, user_input, user_id):
    """Check user option input, and act accordingly if the input is correct.

    Args:
        atm_info (dict): the dictionary, containing all the atm information.
        user_input (str): the option choice of the user.
            there are four options- 1 to check balance, 2 to withdrawal,
            3 to deposit and 4 to change password
        user_id (str): the id of the user, to find him in the dictionary.
    """
    if user_input.isdigit() and int(user_input) in [1, 2, 3, 4]:
        user_input_num = int(user_input)
        if user_input_num == 1:
            print(f"You'r balance: {atm_info[user_id][BALANCE_KEY]}")

        elif user_input_num == 2:
            withdrawal(atm_info, user_id)

        elif user_input_num == 3:
            deposit(atm_info, user_id)

        elif user_input_num == 4:
            change_password(atm_info, user_id)

    else:
        print("Invalid input")


def withdrawal(atm_info, user_id):
    """Withdraw money from atm dict"""
    withdraw = input("Enter how much you want to withdrawal -> ")
    if float(withdraw) > 0:
        atm_info[user_id][BALANCE_KEY] -= float(withdraw)
        print("You have withdrawn: " + withdraw)

    else:
        print("invalid withdrawal input")


def deposit(atm_info, user_id):
    """Deposit money to the atm dict"""
    user_deposit = input("Enter how much you want to deposit -> ")
    if float(user_deposit) > 0:
        atm_info[user_id][BALANCE_KEY] += float(user_deposit)
        print("Deposit succeeded")

    else:
        print("invalid deposit input")


def change_password(atm_info, user_id):
    """Change user's password in the atm dict"""
    new_password = input("Enter you'r new password -> ")
    atm_info[user_id][PASSWORD_KEY] = new_password
    print("The password has been changed ^-^")


def update_file_content(file_path, atm_info):
    """Move the updated dictionary to the atm information file.

    Args:
        file_path (str): path to atm information file.
        atm_info (dict): the dictionary, containing all the atm
            information.
    """
    try:
        with open(file_path, 'w') as file_pointer:
            for key, value in atm_info.items():
                user_password = value[PASSWORD_KEY]
                user_balance = value[BALANCE_KEY]
                file_pointer.write(','.join([str(key), user_password,
                                             str(user_balance)]) + "\n")
        print("Changes saved :)")

    except FileNotFoundError:
        print(f"Can't find the file you have entered:"
              f"{file_path}")


def main():
    file_path = sys.argv[FILE_PATH_INDEX]
    atm_options = store_file_content(file_path)

    if atm_options is not None:
        while True:
            user_id_input = get_user_id(atm_options)
            if user_id_input == END_ATM_SERVICE:
                break

            while True:
                user_input = atm_service(file_path, atm_options,
                                         user_id_input)
                if user_input == END_ATM_SERVICE:
                    break


if __name__ == '__main__':
    main()
