passwords = {}
balances = {}
separator = ','
ID_flag = 'False'
current_id = 0
my_file = open('atm_data.txt', 'r+')
# my_file_content = my_file.read().split('\n')
my_file_content = my_file.readlines()


def ID_check(current_id):
    """Checks if the ID number exists in database"""
    for line in my_file_content:
        if current_id in balances.keys():
            return 'True'
        elif line.split(separator)[0] == current_id:
            passwords[current_id] = line.split(separator)[1]
            balances[current_id] = float(line.split(separator)[2])
            return 'True'


def password_validation(correct_pass):
    """Checks if the password is correct"""
    user_pass = input("Please enter your password:\n")
    try:
        int(user_pass)
        if user_pass == correct_pass:
            return 'True'
        else:
            print("Wrong password")
    except:
        print("Invalid input")


def withdrawal_check(current_id, amount_of_money):
    """Checks if withdrawal amount is a valid input, and if it's possible due to the account balance"""
    try:
        if amount_of_money < 0:
            print("Invalid amount of money, please enter amount > 0")
            return 'False'
        elif amount_of_money > balances[current_id]:
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
    """Check if new password input is by the rules"""
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
        if password_check(new_pass) == 'True':
            passwords[current_id] = new_pass
            print("Your new password is: {}".format(new_pass))
        else:
            ATM(current_id)


def save_data():
    """Saves new ATM data to file"""
    line_num = 0
    for id_num in balances.keys():
        for line in my_file_content:
            if line.split(separator)[0] == id_num:
                new_line = id_num + separator + passwords[id_num] + separator + str(balances[id_num])
                my_file_content[line_num] = new_line + '\n'
                #  = new_line
                line_num += 1
    with open('atm_data.txt', 'w') as my_file:
        my_file.writelines(my_file_content)


while ID_flag != 'True' or current_id != '-1':
    current_id = input("Please enter your ID number:\n")
    if current_id == '-1':
        break
    ID_flag = ID_check(current_id)
    password_flag = 'False'
    if ID_flag != 'True':
        print("Invalid ID number")
    else:
        while password_flag == 'False':
            if password_validation(passwords[current_id]) == 'True':
                ATM(current_id)
                password_flag = 'True'

save_data()