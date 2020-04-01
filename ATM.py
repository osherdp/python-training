__author__ = 'Adi Kadar Levi'

BANK_DATA_PATH = r'C:\Users\Elior Mor Yosef\Documents\GitHub' \
      r'\python-training\python-training\bank.txt'
BALANCE_CHOICE = '1'
DEPOSIT_CHOICE = '2'
WITHDRAW_CHOICE = '3'
CHANGE_PASSWORD_CHOICE = '4'
EXIT_CHOICE = '-1'


class ATM:

    def __init__(self):
        self.id_num = '0'
        self.password = 0
        self.balance = 0
        self.choice = '0'
        self.pass_dict = {}
        self.balance_dict = {}

        with open(BANK_DATA_PATH, 'r') as bank_data:
            for line in bank_data:
                words = line.split()
                id_numbers = words[0]
                passwords = words[1]
                balances = words[2]
                self.pass_dict[id_numbers] = passwords
                self.balance_dict[id_numbers] = float(balances)

    def select(self):
        self.choice = input('What would you like to do today?\n'
                            'To check your balance press 1\n'
                            'To deposit money press 2\n'
                            'To withdraw money press 3\n'
                            'To change password press 4\n'
                            'for Exit press -1\n')
        if self.choice == BALANCE_CHOICE:
            balance = self.balance_dict[self.id_num]
            print('your balance is {}'.format(balance))
            print('Thank you for using our services\n'
                  'For this action '
                  'you will be charged for 300$ commission\n'
                  'Bye Bye!')

        elif self.choice == DEPOSIT_CHOICE:
            amount = input('How much would you like to deposit?\n')
            while not amount.isnumeric():
                amount = input('invalid input\n  please enter the'
                               ' amount you would like to deposit\n')
            self.deposit(float(amount))
            print('The money was successfully deposited\n')
            self.update_data()
            self.get_balance()

        elif self.choice == WITHDRAW_CHOICE:
            amount = input('How much would you like to withdraw?\n')
            while not amount.isnumeric():
                amount = input('invalid input\n  please enter the'
                               ' amount you would like to withdraw\n')
            self.withdraw(float(amount))
            print('The money was successfully withdrawn\n')
            self.update_data()
            self.get_balance()

        elif self.choice == CHANGE_PASSWORD_CHOICE:
            new_password = '0'
            while len(new_password) != 4:
                new_password = input('please enter 4 digit password\n')
            self.change_password(new_password)
            self.update_data()
            print('password successfully changed')

        elif self.choice == EXIT_CHOICE:
            print('Bye!')

        else:
            print('invalid input')

    def get_balance(self):
        self.balance = self.balance_dict[self.id_num]
        print('Now your balance is {} $'.format(self.balance))

    def check_password(self, input_password):
        while self.pass_dict[format(self.id_num)] != input_password:
            print('password incorrect\n')
            input_password = input('please enter your password\n')

    def withdraw(self, amount_to_withdraw):
        self.balance_dict[self.id_num] = self.balance_dict[
                                             self.id_num] - \
                                         amount_to_withdraw

    def deposit(self, amount_to_deposit):
        self.balance_dict[self.id_num] = self.balance_dict[
                                             self.id_num] +\
                                         amount_to_deposit

    def change_password(self, new_password):
        self.pass_dict[self.id_num] = new_password

    def update_data(self):
        with open(BANK_DATA_PATH, 'w') as new_bank:
            for key in self.pass_dict:
                new_bank.write(f"{key} {self.pass_dict[key]} "
                               f"{self.balance_dict[key]}\n")


def main():
    user = ATM()
    print('hello and welcome to The Thieves ATM!')
    id_num = input('please enter you ID number\n')
    if id_num in user.pass_dict.keys():
        user.id_num = id_num
        user.password = input('please enter your password\n')
        user.check_password(user.password)
        user.select()

    else:
        print('User Not Found')


if __name__ == main():
    main()
