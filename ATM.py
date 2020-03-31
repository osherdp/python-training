__author__ = 'Adi Kadar Levi'

BANK_DATA_PATH = r'C:\Users\Elior Mor Yosef\Documents\GitHub' \
      r'\python-training\python-training\bank.txt'


class ATM:

    def __init__(self):
        self.id_num = 0
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
                self.balance_dict[words[0]] = balances

    def select(self):
        self.choice = input('What would you like to do today?\n'
                            'To check your balance press 1\n'
                            'To deposit money press 2\n'
                            'To withdraw money press 3\n'
                            'To change password press 4\n'
                            'for Exit press -1\n')
        return self.choice

    @staticmethod
    def check_password(user_id, input_password, pass_data):
        while pass_data[user_id] != input_password:
            print('password incorrect\n')
            input_password = input('please enter your password\n')

    def get_balance(self, id_num, balance_data):
        self.balance = balance_data[id_num]
        return float(self.balance)

    @staticmethod
    def withdraw(user_id, amount_to_withdraw, balance_dict):
        balance_dict[user_id] = float(balance_dict
                                      [user_id]) - float(amount_to_withdraw)

    @staticmethod
    def deposit(user_id, amount_to_deposit, balance_dict):
        balance_dict[user_id] = float(amount_to_deposit) + float(balance_dict
                                                                 [user_id])

    @staticmethod
    def change_password(new_password, user_id, pass_dict):
        pass_dict[user_id] = new_password

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
        user.check_password(id_num, user.password, user.pass_dict)

        balance_choice = '1'
        deposit_choice = '2'
        withdraw_choice = '3'
        change_pass_choice = '4'
        exit_choice = '-1'
        user.choice = user.select()
        if user.choice == balance_choice:
            balance = user.get_balance(id_num, user.balance_dict)
            print('your balance is {}'.format(balance))
            print('Thank you for using our sevices\n'
                  'For this action '
                  'you will be charged for 300$ comission\n'
                  'Bye Bye!')

        elif user.choice == deposit_choice:
            amount = input('How much would you like to deposit?\n')
            user.deposit(user.id_num, amount, user.balance_dict)
            user.update_data()
            print('now your balance is {}'.format(user.get_balance
                                                  (id_num,
                                                   user.balance_dict)))

        elif user.choice == withdraw_choice:
            amount = input('How much would you like to withdraw?\n')
            user.withdraw(user.id_num, amount, user.balance_dict)
            user.update_data()
            print('now your balance is {}'.format
                  (user.get_balance(id_num, user.balance_dict)))

        elif user.choice == change_pass_choice:
            new_password = '0'
            while len(new_password) != 4:
                new_password = input('please enter 4 digit password\n')
            user.change_password(new_password, user.id_num, user.pass_dict)
            user.update_data()
            print('password successfully changed')

        elif user.choice == exit_choice:
            print('Bye!')

        else:
            print('invalid input')
    else:
        print('User Not Found')


if __name__ == main():
    main()
