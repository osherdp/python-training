"""Simulating an ATM. """

import sys

ATM_FILE = 1
DICTIONARY = {}


def check_the_balance(costumer_id_st):
    """Check the state of costumer's money in the bank.

    Args:
    costumer_id_st(string): costumer id.
    """
    balance = ''
    for i in DICTIONARY.keys():
        if costumer_id_st in i:
            balance = DICTIONARY[i][1]
    return balance


def cash_withdrawal(costumer_id_st, amount_to_withdrawal):
    """Withdrawal from the ATM amount of money.

    Args:
    costumer_id_st(string): costumer id.
    amount_to_withdrawal(integer): amount the costumer wants to withdrawal.
    """
    balance_now = int(check_the_balance(costumer_id_st))
    if balance_now >= amount_to_withdrawal:
        new_balance = balance_now - amount_to_withdrawal
        for i in DICTIONARY:
            if costumer_id_st in i:
                DICTIONARY[i][1] = str(new_balance)
        return f"you have now: {new_balance}"
    return f"You have now {balance_now}. " \
           f"it's impossible to withdrawal more money than what you have"


def cash_deposit(costumer_id_st, amount_to_deposit):
    """deposit to the bank some of money.

    Args:
    costumer_id_st(string): costumer id.
    amount_to_deposit(integer): amount the costumer wants to deposit.
    """
    if amount_to_deposit > 0:
        balance_now = int(check_the_balance(costumer_id_st))
        new_balance = balance_now + amount_to_deposit
        for i in DICTIONARY:
            if costumer_id_st in i:
                DICTIONARY[i][1] = str(new_balance)
        return f"you have now {new_balance}"
    return "the amount is not good"


def change_password(costumer_id_st, new_password):
    """Changing the costumer's ATM password.

    Args:
    costumer_id_st(string): costumer id.
    new_password(integer): the new password the costumer wants to change to.
    """
    new_password_st = str(new_password)
    if len(new_password_st) == 4:
        for i in DICTIONARY:
            if costumer_id_st in i:
                DICTIONARY[i][0] = str(new_password_st)
                return "password changed"
    return "The password needs to be four digits."


def main():
    try:
        with open(sys.argv[ATM_FILE], 'r') as atm_file:
            for line in atm_file:
                list_details = line.split()[1:]
                DICTIONARY[line.split()[0]] = list_details

        print("welcome to bank!\n")
        costumer_id = int(input("enter your id:\n"))

        while costumer_id != -1:
            costumer_id_st = str(costumer_id)
            if costumer_id_st.isdigit() and len(costumer_id_st) == 9 and \
                    DICTIONARY.get(costumer_id_st):
                print("for checking your balance press 1")
                print("for cash withdrawal press 2")
                print("for cash deposit press 3")
                print("for change password press 4")
                costumer_choice = int(input("pressing: "))

                if costumer_choice == 1:
                    print(f"your balance is: "
                          f"{check_the_balance(costumer_id_st)}")
                elif costumer_choice == 2:
                    amount_to_withdrawal = int(input("please enter the "
                                                     "amount "                                                  
                                                     "to withdrawal: "))
                    print(cash_withdrawal(costumer_id_st,
                                          amount_to_withdrawal))
                elif costumer_choice == 3:
                    amount_to_deposit = int(input("please enter "
                                                  "the amount you want"
                                                  " to deposit: "))
                    print(cash_deposit(costumer_id_st, amount_to_deposit))
                elif costumer_choice == 4:
                    new_password = int(input("enter a new password: "))
                    print(change_password(costumer_id_st, new_password))
                else:
                    print("choose 1/2/3/4 ")
                costumer_id = int(input("enter your id:\n"))
            else:
                costumer_id = int(input("the id isn't exists/isn't right, "
                                        "enter a new one:\n"))

        with open(sys.argv[ATM_FILE], 'w') as atm_file:
            for i in DICTIONARY:
                atm_file.write(f"{i} {' '.join(DICTIONARY[i])}\n")

    except FileNotFoundError:
        print("Your file path is incorrect. Please check it.")
    except ValueError:
        print("Value Error! you need to enter an int value")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
