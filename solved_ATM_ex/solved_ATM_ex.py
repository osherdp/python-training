import os
import sys
import json

ATM_FILE_PLACE = 1
COSTUMER_CHOICE_OPTIONS = "1 - View balance \n2 - Withdraw \n3 - Deposit " \
                          "\n4 - Change password \n5 - Exit\n"

costumer_id = ""
costumer_password = ""


def cash_withdraw(costumers_data):
    """Withdraw amount of money from the ATM .

    Args:
        costumers_data (dictionary): Bank costumer data.

    Returns:
        boolean: True for success withdraw action, False otherwise.
    """
    amount_to_withdrawal = float(input("Amount to withdrawal: "))
    balance_now = float(costumers_data[costumer_id]['balance'])
    if 0 < amount_to_withdrawal <= balance_now:
        new_balance = balance_now - amount_to_withdrawal
        costumers_data[costumer_id]['balance'] = new_balance
        return True

    print("Failed - check amount\n")
    return False


def cash_deposit(costumers_data):
    """Deposit money to the bank.

    Args:
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

    print("Failed - check amount\n")
    return False


def change_password(costumers_data):
    """Change costumer's password.

    Args:
        costumers_data (dictionary): Bank costumer data.

    Returns:
        boolean: True for success changing the password, False otherwise.
    """
    global costumer_password
    new_password = input("New password: ")
    if len(new_password) == 4 and new_password.isdigit():
        costumers_data[costumer_id]['password'] = new_password
        costumer_password = new_password
        return True

    print("Should be 4 digits.")
    return False


def create_dictionary(path_of_file):
    """Create dictionary of bank customer data.

    Args:
        path_of_file (string): Path of file that contains all bank costumer
            data.

    Returns:
        dictionary: A nested dictionary of bank costumer data, or None.
    """
    if os.path.isfile(path_of_file):
        with open(path_of_file, 'r') as file_j:
            data = json.load(file_j)
            costumers_data = data
            return costumers_data

    print("File not found")
    return None


def get_new_costumer():
    """Get a new costumer. """

    global costumer_id, costumer_password
    costumer_id = input("id: ")
    if costumer_id != '-1':
        costumer_password = input("Password: ")


def check_costumer_choice(costumer_choice, costumers_data):
    """Check costumer's choice and act accordingly.

    Args:
        costumer_choice (integer): Costumer choice from 1/2/3/4/5 options,
            references to the action he wants to do in ATM.
        costumers_data (dictionary): Bank costumer data.

    Returns:
        string: An error message if costumer's choice is not in range.
    """
    switcher = {
        1: lambda: print(costumers_data[costumer_id]['balance']),
        2: lambda: cash_withdraw(costumers_data),
        3: lambda: cash_deposit(costumers_data),
        4: lambda: change_password(costumers_data),
        5: lambda: main()
    }

    return switcher.get(costumer_choice, lambda: print("Invalid option"))()


def manage_costumer_actions(costumers_data):
    """Manages costumer actions.

     Args:
        costumers_data (dictionary): Bank costumer data.
    """
    global costumer_password, costumer_id
    while costumer_id != '-1':
        if costumer_id in costumers_data and costumers_data[
                costumer_id]['password'] == costumer_password:
            try:
                costumer_choice = int(input(COSTUMER_CHOICE_OPTIONS))
                check_costumer_choice(costumer_choice, costumers_data)

            except ValueError:
                print("Value Error! your input needs to be digit value\n")

        else:
            print("id or password is not correct. Try again:\n")
            get_new_costumer()


def main():
    get_new_costumer()
    costumers_data = create_dictionary(path_of_file=sys.argv[ATM_FILE_PLACE])
    if costumers_data is not None:
        manage_costumer_actions(costumers_data)

        with open(sys.argv[ATM_FILE_PLACE], 'w') as atm_file:
            atm_file.write(json.dumps(costumers_data))


if __name__ == '__main__':
    main()
