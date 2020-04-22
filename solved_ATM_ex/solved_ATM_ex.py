import os
import sys
import json

ATM_FILE_PLACE = 1
BALANCE_OF_COSTUMER = 'balance'
PASSWORD_OF_COSTUMER = 'password'
COSTUMER_CHOICE_OPTIONS = "1 - View balance \n" \
                          "2 - Withdraw \n" \
                          "3 - Deposit \n" \
                          "4 - Change password \n" \
                          "5 - Exit\n"
SWITCHER = {
    '1': lambda data, identifier: print(data[identifier][
                                            BALANCE_OF_COSTUMER]),
    '2': lambda data, identifier: cash_withdraw(data, identifier),
    '3': lambda data, identifier: cash_deposit(data, identifier),
    '4': lambda data, identifier: change_password(data, identifier)
}


def check_convert_to_float(amount):
    """Check if variable can be converted to float.

    Args:
        amount (str): Costumer's input.

    Returns:
        float: Change the type of the variable 'amount' and return it,
            else if couldn't- return None.
    """
    try:
        return float(amount)

    except ValueError:
        return None


def cash_withdraw(costumers_data, costumer_id):
    """Withdraw amount of money from the ATM .

    Args:
        costumers_data (dict): Bank costumer data.
        costumer_id (str): Costumer's ID.
    """
    amount_to_withdraw = input("Amount to withdraw: ")
    check_amount = check_convert_to_float(amount_to_withdraw)
    balance_now = float(costumers_data[costumer_id][BALANCE_OF_COSTUMER])
    if check_amount and 0 < check_amount <= balance_now:
        new_balance = balance_now - check_amount
        costumers_data[costumer_id][BALANCE_OF_COSTUMER] = new_balance
        update_changes_in_dictionary(costumers_data)

    else:
        print("Failed - check amount\n")


def cash_deposit(costumers_data, costumer_id):
    """Deposit money to the bank.

    Args:
        costumers_data (dict): Bank costumer data.
        costumer_id (str): Costumer's ID.
    """
    amount_to_deposit = input("Amount to deposit: ")
    check_amount = check_convert_to_float(amount_to_deposit)
    if check_amount and check_amount > 0:
        balance_now = float(costumers_data[costumer_id][
                                BALANCE_OF_COSTUMER])
        new_balance = balance_now + check_amount
        costumers_data[costumer_id][BALANCE_OF_COSTUMER] = new_balance
        update_changes_in_dictionary(costumers_data)

    else:
        print("Failed - check amount\n")


def change_password(costumers_data, costumer_id):
    """Change costumer's password.

    Args:
        costumers_data (dict): Bank costumer data.
        costumer_id (str): Costumer's ID.
    """
    new_password = input("New password: ")
    if len(new_password) == 4 and new_password.isdigit():
        costumers_data[costumer_id][PASSWORD_OF_COSTUMER] = new_password
        update_changes_in_dictionary(costumers_data)

    else:
        print("Should be 4 digits.")


def read_costumers_information_from_file(path_of_file):
    """Read costumer's information from file to dictionary.

    Args:
        path_of_file (str): Path of file that contains all bank costumer
            data.

    Returns:
        dict: A nested dictionary of bank costumer data, or None.
    """
    if os.path.isfile(path_of_file):
        with open(path_of_file, 'r') as file_j:
            data = json.load(file_j)
            costumers_data = data
            return costumers_data

    print("File not found")
    return None


def update_changes_in_dictionary(costumers_data):
    """Update changes in the dictionary after costumer's actions.

    Args:
        costumers_data (dict): Bank costumer data.
    """
    with open(sys.argv[ATM_FILE_PLACE], 'w') as atm_file:
        atm_file.write(json.dumps(costumers_data))


def manage_costumer_actions(costumers_data, costumer_id, costumer_password):
    """Manage costumer actions.

     Args:
        costumers_data (dict): Bank costumer data.
        costumer_id (str): Costumer's ID.
        costumer_password (str): Costumer's password.
    """
    if costumer_id in costumers_data and costumers_data[
            costumer_id][PASSWORD_OF_COSTUMER] == costumer_password:
        costumer_choice = input(COSTUMER_CHOICE_OPTIONS)
        while costumer_choice != '5':
            SWITCHER.get(costumer_choice, lambda data, identifier: print(
                "Invalid option"))(costumers_data, costumer_id)
            costumer_choice = input(COSTUMER_CHOICE_OPTIONS)

        print("Thank you.")

    else:
        print("ID or password is not correct. Try again:\n")


def manage_new_costumer(costumers_data):
    """Get a new costumer and act accordingly.

     When the customer ID will be (-1), the ATM will be turned off.

     Args:
         costumers_data (dict): Bank costumer data.
    """
    costumer_id = input("ID: ")
    while costumer_id != '-1':
        costumer_password = input("Password: ")
        manage_costumer_actions(costumers_data, costumer_id,
                                costumer_password)
        costumer_id = input("ID: ")


def main():
    costumers_data = read_costumers_information_from_file(
        path_of_file=sys.argv[ATM_FILE_PLACE])
    if costumers_data:
        manage_new_costumer(costumers_data)


if __name__ == '__main__':
    main()
