__author__ = 'Adi Kadar Levi'
BANK_DATA_PATH = r'C:\Users\Elior Mor Yosef\Documents\GitHub' \
                 r'\python-training\python-training\bank.txt'


def passwords_dictionary():
    pass_dict = {}
    with open(BANK_DATA_PATH, 'r') as bank_data:
        for line in bank_data:
            words = line.split()
            pass_dict[words[0]] = words[1]
    return pass_dict


def balance_dictionary():
    balance_dict = {}
    with open(BANK_DATA_PATH, 'r') as bank_data:
        for line in bank_data:
            words = line.split()
            balance_dict[words[0]] = words[2]
    return balance_dict


def check_id(id_input):
    if id_input not in passwords_dictionary().keys():
        print('User Not Found')
        return False
    else:
        return True


def check_password(user_id, input_password, pass_data):
    while pass_data[user_id] != input_password:
        print('password incorrect\n')
        input_password = input('please enter your password\n')


def check_balance(id_num, balance_data):
    balance = balance_data[id_num]
    return float(balance)
    pass


def withdraw(user_id, amount_to_withdraw, pass_dict, balance_dict):
    balance_dict[user_id] = float(balance_dict[user_id]) -\
                            float(amount_to_withdraw)
    with open(BANK_DATA_PATH, 'w') as new_bank:
        for key in pass_dict:
            print(key, pass_dict[key], balance_dict[key], file=new_bank)
    pass


def deposit(user_id, amount_to_deposit, pass_dict, balance_dict):
    balance_dict[user_id] = float(amount_to_deposit) + \
                            float(balance_dict[user_id])
    with open(BANK_DATA_PATH, 'w') as new_bank:
        for key in pass_dict:
            print(key, pass_dict[key], balance_dict[key], file=new_bank)
    pass


def change_password(new_password, user_id, pass_dict, balance_dict):
    pass_dict[user_id] = new_password
    with open(BANK_DATA_PATH, 'w') as new_bank:
        for key in pass_dict:
            print(key, pass_dict[key], balance_dict[key], file=new_bank)
    pass


def main():
    pass_dict = passwords_dictionary()
    bal_dict = balance_dictionary()
    print('hello and welcome to The Thieves ATM!')
    id_num = input('please enter you ID number\n')
    if check_id(id_num):
        password = input('please enter your password\n')
        check_password(id_num, password, pass_dict)
        print('What would you like to do today?\n'
              'To check your balance press 1\n'
              'To deposit money press 2\n'
              'To withdraw money press 3\n'
              'To change password press 4\n'
              'for Exit press -1\n')
        choose = input('\n')
        while choose != '-1':
            if choose == '1':
                balance = check_balance(id_num, bal_dict)
                print('your balance is {}' .format(balance))
                print('Thank you for using our sevices\n'
                      'For this action '
                      'you will be charged for 300$ comission\n'
                      'Bye Bye!')
                break

            elif choose == '2':
                amount = input('How much would you like to deposit?\n')
                deposit(id_num, amount, pass_dict, bal_dict)
                print('now your balance is {}'.format(check_balance
                                                      (id_num, bal_dict)))
                break
            elif choose == '3':
                amount = input('How much would you like to withdraw?\n')
                withdraw(id_num, amount, pass_dict, bal_dict)
                print('now your balance is {}'.format
                      (check_balance(id_num, bal_dict)))
                break
            elif choose == '4':
                new_password = '0'
                while len(new_password) != 4:
                    new_password = input('please enter 4 digit password\n')
                change_password(new_password, id_num, pass_dict, bal_dict)
                print('password successfully changed')
                break
            else:
                print('invalid input')
                break


if __name__ == main():
    main()
