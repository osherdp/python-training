CUSTOMER_ID_PLACE = 0
CUSTOMER_ATM_PASSWORD_PLACE = 1
CUSTOMER_BALANCE_PLACE = 2
customer_dict = {}


def file_into_dict(customer_data_line):
    """ function receives customer data line from the customers file
     and adds it to the customer dictionary
     """
    customer_list = customer_data_line.split()
    customer_dict[customer_list[0]] = customer_list


def correct_password(customer_id, customer_password_input):
    """ function receives customer's ID and password which he inserts himself (input) and
     return if it is the correct password (True/False)
     """
    if customer_password_input == customer_dict[customer_id][CUSTOMER_ATM_PASSWORD_PLACE]:
        return True
    else:
        return False


def check_the_balance(customer_id):
    """ function receives customer's ID
    and returns the customer's balance
    """
    return customer_dict[customer_id][CUSTOMER_BALANCE_PLACE]


def withdrawal(customer_id, withdraw_cash):
    """ function receives customer's ID and how much money he would like to withdraw
    and returns his withdrawal amount from his balance, and new balance
    """
    balance_num = int(check_the_balance(customer_id))
    if withdraw_cash.isnumeric():
        withdraw_cash2 = int(withdraw_cash)
    else:
        return 'error-withdraw cash is not readable'
    new_balance = str(balance_num - withdraw_cash2)
    customer_dict[customer_id][CUSTOMER_BALANCE_PLACE] = new_balance
    return withdraw_cash, new_balance


def deposit(customer_id, deposit_cash):
    """ function receives customer's ID and how much money he would like to depose
    and returns his deposed money, and new balance
    """
    balance_num = int(check_the_balance(customer_id))
    if deposit_cash.isnumeric():
        deposit_cash2 = int(deposit_cash)
    else:
        return 'error-deposit cash is not readable'
    new_balance = str(balance_num + deposit_cash2)
    customer_dict[customer_id][CUSTOMER_BALANCE_PLACE] = new_balance
    return deposit_cash, new_balance


def change_password(customer_id, new_password):
    """ function receives customer's ID and the new password that he wants
    and changes the password to the new one
    """
    customer_dict[customer_id][CUSTOMER_ATM_PASSWORD_PLACE] = new_password


def main():
    customers_file = open(r'C:\customers file for ATM exercise\customers file.txt', 'r')
    for line in customers_file:
        file_into_dict(line)
    customer_id = input("please enter your ID\n")
    while True:
        customer_password = input("please enter your password\n")
        if correct_password(customer_id, customer_password) is True:
            user_act = input("check your balance-1, withdraw money-2, depose money-3, change password-4\n")
            if user_act == "1":
                print(f'your balance is {check_the_balance(customer_id)}')
            if user_act == "2":
                withdraw_cash = input("how much money would you like to withdraw?\n")
                print(f'your withdraw money and new balance {withdrawal(customer_id, withdraw_cash)}')
            if user_act == "3":
                withdraw_cash = input("how much money would you like to depose?\n")
                print(f'your deposit money and new balance {deposit(customer_id, withdraw_cash)}')
            if user_act == "4":
                new_password = input("enter your new password\n")
                change_password(customer_id, new_password)
                print("your password has changed successfully")
            user_act2 = input("would you like to do anything else? 1-yes 2-no\n")
            if user_act2 == '2':
                break
        else:
            print("incorrect password, try again")
2

if __name__ == '__main__':
    main()









