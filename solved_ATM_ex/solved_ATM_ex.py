"""Simulating an ATM. """

import os
import sys
import json

ATM_FILE_PLACE = 1


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
        return new_password

    return False


def create_dictionary(path_of_file):
    """Create dictionary of bank customer data.

    Args:
        path_of_file (string): Path of the file that contains all bank
            costumer data.

    Returns:
        dictionary: A nested dictionary of bank costumer data, or print a
            message and exit if the file path is not correct.
    """

    if os.path.isfile(path_of_file):
        with open(path_of_file, 'r') as file_j:
            data = json.load(file_j)
            costumers_data = data
            return costumers_data

    print("Your file path is incorrect. Please check it.")
    quit()


def main():
    costumers_data = create_dictionary(path_of_file=sys.argv[ATM_FILE_PLACE])
    costumer_id = input("Welcome to the bank\n\nEnter your id: \n")
    costumer_password = input("Enter your password: \n")
    while costumer_id != '-1':
        if costumer_id in costumers_data and costumers_data[
                costumer_id]['password'] == costumer_password:

            try:
                costumer_choice = int(input("For checking your balance press"
                                            " 1 \nFor cash withdrawal press 2"
                                            "\nFor cash deposit"
                                            " press 3 \nFor change password "
                                            "press 4 \nTo finish "
                                            "actions press 5 \n"))
                if costumer_choice == 1:
                    print(
                        f"Balance: {costumers_data[costumer_id]['balance']}")

                elif costumer_choice == 2:
                    if cash_withdrawal(costumer_id, costumers_data):
                        print("The action was succeeded\n")

                    else:
                        print("Failed - check your amount\n")

                elif costumer_choice == 3:
                    if cash_deposit(costumer_id, costumers_data):
                        print("The action was succeeded\n")

                    else:
                        print("Failed - check your amount\n")

                elif costumer_choice == 4:
                    new_password = input("Enter a new password: ")
                    if change_password(costumer_id, costumers_data,
                                       new_password):
                        costumer_password = new_password
                        print("Password changed")

                    else:
                        print("Not a good password,it needs to be 4 digits.")

                elif costumer_choice == 5:
                    costumer_id = input("Enter your id: ")
                    if costumer_id != '-1':
                        costumer_password = input("Enter your password: ")

                else:
                    print("Choose 1/2/3/4/5 option: ")

            except ValueError:
                print("Value Error! your input needs to be digit value\n")

        else:
            print("Your ID or your password is not correct. Please try to "
                  "enter again:\n")
            costumer_id = input("Enter your id: ")
            costumer_password = input("Enter your password: ")

    data = json.dumps(costumers_data)
    with open(sys.argv[ATM_FILE_PLACE], 'w') as atm_file:
        atm_file.write(data)


if __name__ == '__main__':
    main()
