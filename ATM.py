__author__ = 'Adi Kadar Levi'


class ATM:
    def __init__(self):
        self.id_num = 0
        self.password = 0
        self.balance = 0
        self.__pass_dict = {}
        self.__bal_dict = {}

    def get_passwords_dictionary(self):
        bank_data_path = r'C:\Users\Elior Mor Yosef\Documents\GitHub' \
                         r'\python-training\python-training\bank.txt'

        with open(bank_data_path, 'r') as bank_data:
            for line in bank_data:
                words = line.split()
                self.__pass_dict[words[0]] = words[1]
        return self.__pass_dict

    def get_balance_dictionary(self):
        bank_data_path = r'C:\Users\Elior Mor Yosef\Documents\GitHub' \
                         r'\python-training\python-training\bank.txt'

        with open(bank_data_path, 'r') as bank_data:
            for line in bank_data:
                words = line.split()
                self.__bal_dict[words[0]] = words[2]
        return self.__bal_dict

    def check_id(self, id_input):
        if id_input not in self.get_passwords_dictionary().keys():
            print('User Not Found')
            return False
        return True

    @staticmethod
    def check_password(user_id, input_password, pass_data):
        while pass_data[user_id] != input_password:
            print('password incorrect\n')
            input_password = input('please enter your password\n')

    def get_balance(self, id_num, balance_data):
        self.balance = balance_data[id_num]
        return float(self.balance)
        pass

    @staticmethod
    def set_withdraw(user_id, amount_to_withdraw, pass_dict,
                     balance_dict):
        bank_data_path = r'C:\Users\Elior Mor Yosef\Documents\GitHub' \
                         r'\python-training\python-training\bank.txt'

        balance_dict[user_id] = float(balance_dict
                                      [user_id]) - float(amount_to_withdraw)

        with open(bank_data_path, 'w') as new_bank:
            for key in pass_dict:
                print(key, pass_dict[key], balance_dict[key], file=new_bank)
        pass

    @staticmethod
    def set_deposit(user_id, amount_to_deposit, pass_dict,
                    balance_dict):
        bank_data_path = r'C:\Users\Elior Mor Yosef\Documents\GitHub' \
                         r'\python-training\python-training\bank.txt'
        balance_dict[user_id] = float(amount_to_deposit) + float(balance_dict
                                                                 [user_id])

        with open(bank_data_path, 'w') as new_bank:
            for key in pass_dict:
                print(key, pass_dict[key], balance_dict[key], file=new_bank)
        pass

    @staticmethod
    def set_change_password(new_password, user_id, pass_dict, balance_dict):
        bank_data_path = r'C:\Users\Elior Mor Yosef\Documents\GitHub' \
                         r'\python-training\python-training\bank.txt'

        pass_dict[user_id] = new_password
        with open(bank_data_path, 'w') as new_bank:
            for key in pass_dict:
                print(key, pass_dict[key], balance_dict[key], file=new_bank)
        pass


def main():
    user = ATM()

    pass_dict = user.get_passwords_dictionary()
    bal_dict = user.get_balance_dictionary()
    print('hello and welcome to The Thieves ATM!')
    id_num = input('please enter you ID number\n')
    if user.check_id(id_num):
        password = input('please enter your password\n')
        user.check_password(id_num, password, pass_dict)
        print('What would you like to do today?\n'
              'To check your balance press 1\n'
              'To deposit money press 2\n'
              'To withdraw money press 3\n'
              'To change password press 4\n'
              'for Exit press -1\n')
        choose = input('\n')
        while choose != '-1':
            if choose == '1':
                balance = user.get_balance(id_num, bal_dict)
                print('your balance is {}'.format(balance))
                print('Thank you for using our sevices\n'
                      'For this action '
                      'you will be charged for 300$ comission\n'
                      'Bye Bye!')
                break

            elif choose == '2':
                amount = input('How much would you like to deposit?\n')
                user.set_deposit(id_num, amount, pass_dict, bal_dict)
                print('now your balance is {}'.format(user.get_balance
                                                      (id_num, bal_dict)))
                break
            elif choose == '3':
                amount = input('How much would you like to withdraw?\n')
                user.set_withdraw(id_num, amount, pass_dict, bal_dict)
                print('now your balance is {}'.format
                      (user.get_balance(id_num, bal_dict)))
                break
            elif choose == '4':
                new_password = '0'
                while len(new_password) != 4:
                    new_password = input('please enter 4 digit password\n')
                user.set_change_password(new_password, id_num, pass_dict,
                                         bal_dict)
                print('password successfully changed')
                break
            else:
                print('invalid input')
                break


if __name__ == main():
    main()
