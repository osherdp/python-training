# ATM Exercise

import sys

FILE_PATH = 1
PASSWORD_INDEX = 0
BALANCE_INDEX = 1


def read_file_move_to_dict(file_path):
    """Read file and move atm information to dictionary.

    Args:
        file_path (string): path to atm information file.

    Return:
        A dictionary, the key is each users id.
        the value is a list of user's password and balance.
    """
    try:
        atm_options_dict = {}
        with open(file_path, 'r') as file_pointer:
            for line in file_pointer:
                line_list = line.rstrip().split(',')
                atm_options_dict.update({line_list[0]: [line_list[1],
                                                        float(line_list[2])]})
        return atm_options_dict

    except FileNotFoundError:
        print("The path to the file you have entered was incorrect.")

    except Exception as e:
        print(e)


def check_input_execute(atm_dict, user_input, user_id):
    """Check user option input, and act accordingly, if input is correct.

    Args:
        atm_dict (dictionary): the dictionary, containing all the atm
                               information.
        user_input (string): the option choice of the user.
        user_id (string): the id of the user, to find him in the dictionary.

    Return:
        The new changed dictionary of atm information.
    """
    try:
        # ['check', 'withdrawal', 'deposit', 'change']:
        if user_input == "check":
            print(f"You'r balance: {atm_dict[user_id][BALANCE_INDEX]}")

        elif user_input == "withdrawal":
            withdrawal = input("Enter how much you want to withdrawal -> ")
            if float(withdrawal) > 0:
                atm_dict[user_id][BALANCE_INDEX] -= float(withdrawal)
                print("You have withdrawn: " + withdrawal)

        elif user_input == "deposit":
            deposit = input("Enter how much you want to withdrawal -> ")
            if float(deposit) > 0:
                atm_dict[user_id][BALANCE_INDEX] += float(deposit)
                print("Deposit succeeded")

        elif user_input == "change":
            new_password = input("Enter you'r new password -> ")
            atm_dict[user_id][PASSWORD_INDEX] = new_password
            print("Password changed to: " + new_password)

        else:
            print("Invalid input")

    except ValueError:
        print("Invalid input")

    except Exception as e:
        print(e)

    finally:
        return atm_dict


def read_dict_move_to_file(file_path, atm_dict):
    """Move the updated dictionary to the atm information file.

    Args:
        file_path (string): path to atm information file.
        atm_dict (dictionary): the dictionary, containing all the atm
                               information.
    """
    try:
        with open(file_path, 'w') as file_pointer:
            for key in atm_dict:
                file_pointer.write(','.join([str(key), atm_dict[key][0],
                                             str(atm_dict[key][1])]) + "\n")
        print("Changes saved :)")

    except FileNotFoundError:
        print("Something went wrong, when accessing file")

    except Exception as e:
        print(e)


def main():
    file_path = sys.argv[FILE_PATH]
    atm_options_dict = read_file_move_to_dict(file_path)

    while True:
        user_id_input = input("Enter costumer ID, to turn off the ATM enter "
                              "-1 -> ")
        if user_id_input == -1:
            atm_options_dict = None
            break
        elif user_id_input in atm_options_dict:
            break
        else:
            print("Invalid ID")

    while True and atm_options_dict is not None:
        user_option = input("Enter wanted option, to turn off the ATM enter -1"
                            + "\nEnter 'options' to see ATM's options. -> ")
        user_option = user_option.lower()
        if user_option == "-1":
            read_dict_move_to_file(file_path, atm_options_dict)
            break
        elif user_option == "options":
            print("The ATM allow the following options to a using costumer:" +
                  "\n1. 'check' the balance.\n2. cash 'withdrawal'." +
                  "\n3. cash 'deposit'.\n4. 'change' password.")
        else:
            atm_options_dict = check_input_execute(atm_options_dict,
                                                   user_option, user_id_input)


if __name__ == '__main__':
    main()
