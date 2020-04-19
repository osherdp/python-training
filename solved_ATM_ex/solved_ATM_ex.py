"""Simulating an ATM. """

import os
import sys
import json

ATM_FILE_PLACE = 1
COSTUMER_CHOICE_OPTIONS = "For checking balance press  1 \nFor cash " \
                          "withdrawal press 2 \nFor cash deposit press 3 " \
                          "\nFor change password " \
                          "press 4 \nTo finis actions press 5 \n"


def cash_withdrawal(costumer_id, costumers_data):
    """Withdrawal from the ATM amount of money.

    Args:
        costumer_id (string): Costumer id.
        costumers_data (dictionary): Bank costumer data.

    Returns:
        boolean: True for success withdrawal action, False otherwise.
    """
    amount_to_withdrawal = float(input("Amount to withdrawal: "))
    balance_now = float(costumers_data[costumer_id]['balance'])
    if 0 < amount_to_withdrawal <= balance_now:
        new_balance = balance_now - amount_to_withdrawal
        costumers_data[costumer_id]['balance'] = new_balance
        return True

    return False


def cash_deposit(costumer_id, costumers_data):
    """Deposit money to the bank.

    Args:
        costumer_id (string): Costumer id.
        costumers_data (dictionary): Bank costumer data.

    Returns:
        boolean: True for success deposit action, False otherwise.
    """
    amount_to_deposit = float(input("Amount to deposit: "))
    if amount_to_deposit > 0:
        balance_now = float(costumers_data[costumer_id]['balance'])
        new_balance = balance_now + amount_to_deposit
        costumers_data[costumer_id]['balance'] = new_balance
        return True

    return False


def change_password(costumer_id, costumers_data, new_password):
    """Changing costumer's ATM password.

    Args:
        costumer_id (string): Costumer id.
        costumers_data (dictionary): Bank costumer data.
        new_password (string): Password the costumer wants to change to.

    Returns:
        boolean: True for success changing the password, False otherwise.
    """
    if len(new_password) == 4 and new_password.isdigit():
        costumers_data[costumer_id]['password'] = new_password
        password_now = new_password
        return password_now

    return False


def create_dictionary(path_of_file):
    """Create dictionary of bank customer data.

    Args:
        path_of_file (string): Path of file that contains all bank costumer
            data.

    Returns:
        dictionary: A nested dictionary of bank costumer data, or print a
            message and return a None dict if the file path is not correct.
    """
    if os.path.isfile(path_of_file):
        with open(path_of_file, 'r') as file_j:
            data = json.load(file_j)
            costumers_data = data
            return costumers_data

    print("File not found")
    costumers_data = None
    return costumers_data


def check_costumer_choice(costumer_choice, costumers_data, costumer_id,
                          costumer_password):
    """Check costumer choice and act accordingly.

    Args:
        costumer_choice (integer): Costumer choice from 1/2/3/4/5 options,
            references to the action he wants to do in ATM.
        costumers_data (dictionary): Bank costumer data.
        costumer_id (string): Costumer id.
        costumer_password (string): Current costumer password.

    Returns:
        string: Updated password if the choice is 4, or updated id and
            password if the choice is 5.
    """
    if costumer_choice == 1:
        print(f"Balance: {costumers_data[costumer_id]['balance']}")

    elif costumer_choice == 2:
        print("Action succeeded\n" if cash_withdrawal(
            costumer_id, costumers_data) else "Failed - check amount\n")

    elif costumer_choice == 3:
        print(
            "Action succeeded\n" if cash_deposit(costumer_id, costumers_data)
            else "Failed - check amount\n")

    elif costumer_choice == 4:
        new_password = input("New password: ")
        costumer_password = new_password if change_password(
            costumer_id, costumers_data, new_password) else costumer_password
        return costumer_password

    elif costumer_choice == 5:
        costumer_id = input("id: ")
        if costumer_id != '-1':
            costumer_password = input("Password: ")
        return costumer_id, costumer_password

    else:
        print("Please choose 1/2/3/4/5 option: ")


def manage_costumer_actions(costumer_id, costumers_data, costumer_password):
    """Manage costumer actions.

     Args:
        costumers_data (dictionary): Bank costumer data.
        costumer_id (string): Costumer id.
        costumer_password (string): Current costumer password.

    Returns:
        None.
    """
    while costumer_id != '-1':
        if costumer_id in costumers_data and costumers_data[
                costumer_id]['password'] == costumer_password:
            try:
                costumer_choice = int(input(COSTUMER_CHOICE_OPTIONS))
                if costumer_choice == 4:
                    costumer_password = check_costumer_choice(costumer_choice,
                                                              costumers_data,
                                                              costumer_id,
                                                              costumer_password)

                elif costumer_choice == 5:
                    costumer_id, costumer_password = check_costumer_choice(
                        costumer_choice, costumers_data, costumer_id,
                        costumer_password)

                else:
                    check_costumer_choice(costumer_choice, costumers_data,
                                          costumer_id, costumer_password)

            except ValueError:
                print("Value Error! your input needs to be digit value\n")

        else:
            print("ID or password is not correct.Try to enter again:\n")
            costumer_id, costumer_password = input("id: "), input(
                "Password: ")


def main():
    costumers_data = create_dictionary(path_of_file=sys.argv[ATM_FILE_PLACE])
    if costumers_data is not None:
        costumer_id, costumer_password = input("id: "), input("Password: ")
        manage_costumer_actions(costumer_id, costumers_data,
                                costumer_password)

        with open(sys.argv[ATM_FILE_PLACE], 'w') as atm_file:
            atm_file.write(json.dumps(costumers_data))


if __name__ == '__main__':
    main()
