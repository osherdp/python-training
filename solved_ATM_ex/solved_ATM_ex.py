"""Simulating an ATM. """

import sys

ATM_FILE = 1  # The number 1 refers to the place of the file as a parameter.
COSTUMER_BALANCE_PLACE_IN_DICTIONARY = 1
COSTUMER_PASSWORD_PLACE_IN_DICTIONARY = 0


def cash_withdrawal(costumer_indent, amount_to_withdrawal,
                    costumers_dictionary):
    """Withdrawal from the ATM amount of money.

    Args:
        costumer_indent (string): Costumer id.
        amount_to_withdrawal (float): Amount the costumer wants to withdrawal.
        costumers_dictionary (dictionary): Contains bank costumer data.

    Returns:
        True for success withdrawal action, False otherwise.

    """
    balance_now = float(costumers_dictionary[costumer_indent][
                            COSTUMER_BALANCE_PLACE_IN_DICTIONARY])

    if 0 < amount_to_withdrawal <= balance_now:
        new_balance = balance_now - amount_to_withdrawal
        costumers_dictionary[costumer_indent][
            COSTUMER_BALANCE_PLACE_IN_DICTIONARY] = str(new_balance)
        return True

    return False


def cash_deposit(costumer_indent, amount_to_deposit, costumers_dictionary):
    """Deposit to the bank some of money.

    Args:
        costumer_indent (string): Costumer id.
        amount_to_deposit (float): Amount the costumer wants to deposit.
        costumers_dictionary (dictionary): Contains bank costumer data.

    Returns:
        True for success deposit action, False otherwise.

    """
    if amount_to_deposit > 0:
        balance_now = float(costumers_dictionary[costumer_indent][
                                COSTUMER_BALANCE_PLACE_IN_DICTIONARY])
        new_balance = balance_now + amount_to_deposit
        costumers_dictionary[costumer_indent][
            COSTUMER_BALANCE_PLACE_IN_DICTIONARY] = str(new_balance)
        return True

    return False


def change_password(costumer_indent, new_password, costumers_dictionary):
    """Changing the costumer's ATM password.

    Args:
        costumer_indent (string): Costumer id.
        new_password (string): The new password the costumer wants to change to.
        costumers_dictionary (dictionary): Contains bank costumer data.

    Returns:
        True for success changing the password, False otherwise.

    """
    if len(new_password) == 4 and new_password.isdigit():
        costumers_dictionary[costumer_indent][
            COSTUMER_PASSWORD_PLACE_IN_DICTIONARY] = new_password
        return True

    return False


def fill_dictionary(costumers_dictionary):
    """Filling dictionary with bank customer data.

    Args:
         costumers_dictionary (dictionary): An empty dictionary.

    Returns:
        A full dictionary of bank costumer data, or an exception if the
        file path is not correct.

    """
    try:
        with open(sys.argv[ATM_FILE], 'r') as atm_file:
            for line in atm_file:
                a, *b = line.split()
                costumers_dictionary[a] = b
            return costumers_dictionary

    except FileNotFoundError:
        return "Your file path is incorrect. Please check it."


def main():
    costumers_dictionary = {}
    fill_dictionary(costumers_dictionary)
    print("Welcome to bank!\n")
    costumer_indent = input("Enter your id: ")
    costumer_password = input("Enter your password: ")
    not_finish_actions = True

    while not_finish_actions:
        if costumer_indent in costumers_dictionary and \
                costumers_dictionary[costumer_indent][
                    COSTUMER_PASSWORD_PLACE_IN_DICTIONARY] \
                == costumer_password:

            try:
                print("For checking your balance press 1")
                print("For cash withdrawal press 2")
                print("For cash deposit press 3")
                print("For change password press 4")
                print("To exit press -1")
                costumer_choice = int(input("Pressing: \n"))

                if costumer_choice == 1:
                    print(f"Your balance: "
                          f"{float(costumers_dictionary[costumer_indent][COSTUMER_BALANCE_PLACE_IN_DICTIONARY])}\n")

                elif costumer_choice == 2:
                    amount_to_withdrawal = float(input("Please enter amount "
                                               "you want to withdrawal: \n"))

                    if cash_withdrawal(costumer_indent, amount_to_withdrawal,
                                       costumers_dictionary):
                        print("The action was succeeded\n")

                    else:
                        print("Failed - check your amount\n")

                elif costumer_choice == 3:
                    amount_to_deposit = float(input("Please enter amount you "
                                                    "want to deposit: \n"))

                    if cash_deposit(costumer_indent, amount_to_deposit,
                                    costumers_dictionary):
                        print("The action was succeeded\n")

                    else:
                        print("Failed - check your amount\n")

                elif costumer_choice == 4:
                    new_password = input("Enter a new password: \n")
                    if change_password(costumer_indent, new_password,
                                       costumers_dictionary):
                        print("Password changed")

                    else:
                        print("Not a good password, needs to be 4 digits:")

                elif costumer_choice == -1:
                    not_finish_actions = False

                else:
                    print("Choose 1/2/3/4/-1 option: ")

            except ValueError:
                print("Value Error! your input needs to be digit value\n")

        else:
            print("Your ID or your password is not correct. Please try to "
                  "enter again:\n")
            costumer_indent = input("Enter your id: ")
            costumer_password = input("Enter your password: ")

        with open(sys.argv[ATM_FILE], 'w') as atm_file:
            for line in costumers_dictionary:
                atm_file.write(
                    f"{line} {' '.join(costumers_dictionary[line])}\n")


if __name__ == '__main__':
    main()
