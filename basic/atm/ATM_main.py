passwords = {}
balances = {}
separator = ','
ID_flag = 'False'
my_file = open('atm_data.txt', 'r').read().split('\n')


def ID_check(current_id):
    """Checks if the ID number exists in database"""
    for line in my_file:
        if line.split(separator)[0] == current_id:
            passwords[current_id] = line.split(separator)[1]
            balances[current_id] = float(line.split(separator)[2])
            return 'True'
        else:
            return 'False'


def password_validation(correct_pass):
    """Checks if the password is correct"""
    user_pass = input("Please enter your password:\n")
    return user_pass == correct_pass


def withdrawal_check(current_id, amount_of_money):
    """Checks if withdrawal amount is a valid input, and if it's possible due to the account balance"""
    try:
        if amount_of_money < 0:
            print("Invalid amount of money, please enter amount > 0")
            return 'False'
        elif amount_of_money < balances[current_id]:
            print("You balance is not sufficient for this withdrawal amount")
            return 'False'
        else:
            return 'True'
    except:
        print("Invalid input")


def deposit_check(current_id, amount_of_money):
    """Checks if withdrawal amount is a valid input, and if it's > 0"""
    try:
        if amount_of_money < 0:
            print("Invalid amount of money, please enter amount > 0")
            return 'False'
        else:
            return 'True'
    except:
        print("Invalid input")


def password_check(new_pass):
    try:
        int(new_pass)
        if len(new_pass) == 4:
            return 'True'
        else:
            print("The password should be a 4 digits number")
            return 'False'
    except:
        print("The password should be a 4 digits number")


def ATM(current_id):
    """Performs ATM operation"""
    choose = input("Please choose from below: \n 1: Check what is your account balance \n 2: Withdraw money \n 3: "
                   "Deposit money \n 4: Change your password \n")
    if choose == '1':
        print(balances[current_id])
    elif choose == '2':
        amount_of_money = float(input("Please enter amount of money you wish to withdraw: \n"))
        if withdrawal_check(current_id, amount_of_money) == 'True':
            balances[current_id] -= amount_of_money
            print(balances[current_id])
        else:
            ATM(current_id)
    elif choose == '3':
        amount_of_money = float(input("Please enter amount of money you wish to deposit: \n"))
        if deposit_check(current_id, amount_of_money) == 'True':
            balances[current_id] += amount_of_money
            print(balances[current_id])
        else:
            ATM(current_id)
    elif choose == '4':
        new_pass = input("Please enter your new password (4 digits): \n")
        print([password_check(new_pass)])
        if password_check(new_pass) == 'True':
            passwords[current_id] = new_pass
        else:
            ATM(current_id)


while ID_flag == 'False':
    current_id = input("Please enter your ID number:\n")
    ID_flag = ID_check(current_id)
    print(passwords)
    if ID_flag == 'False':
        print("Invalid ID number")
    elif password_validation(passwords[current_id]):
        ATM(current_id)

# should fix amount input (from string to number)