from Costumer import Costumer
from pip._vendor.distlib.compat import raw_input


class Atm:
    def __init__(self, file_path):
        self.costumers = {}
        self.consumer = ''
        self.need_update = False
        self.file_path = file_path
        self.on = True

    def start_action(self):
        self.update_costumers()
        self.get_consumer()
        while self.on:

            if self.check_password():
                self.get_desired_operation()
                print('Thanks you for using our services!')
                self.get_consumer()
        if self.need_update:
            self.update_details()

    def update_costumers(self):
        consumer_id = 0
        password = 1
        balance = 2
        with open(self.file_path, 'r') as file:
            costumers = [i[:i.find('\n')] for i in file.readlines()]
        costumers = [i.split(',') for i in costumers]
        for i in costumers:
            if i[consumer_id] and i[password] and i[balance]:
                costumer = Costumer(i[consumer_id], i[password], i[balance])
                _id = i[consumer_id]
                self.costumers[_id] = costumer
        print(self.costumers)

    def get_consumer(self):
        consumer_id = raw_input('To turn off insert -1\nPlease enter your id:\n')
        if int(consumer_id) != -1:
            try:
                self.consumer = self.costumers[consumer_id.strip()]
            except:
                print("No account for the inserted id, please try again")
                self.get_consumer()
        else:
            self.on = False

    def check_password(self):
        max_mistakes = 3
        for i in range(max_mistakes):
            entered_password = raw_input('To move on, please enter your password:\n')
            if entered_password == self.consumer.password:
                return True
                break
            else:
                print("The inserted password was wrong")

    def update_details(self):
        lines = []
        for consumer in self.costumers.values():
            lines.append(consumer.__str__())
        with open(self.file_path, 'w') as set_new_file:
            set_new_file.writelines(lines)

    def get_desired_operation(self):
        check_balance = 1
        cash_withdrawal = 2
        cash_deposit = 3
        change_password = 4
        print('Hi! welcome to your account, choose your act: ')
        operation_number = raw_input('1 Check balance\n'
                                     '2 Cash withdrawal\n'
                                     '3 Cash deposit\n'
                                     '4 Change password\n')

        operation_number = int(operation_number.strip())
        if operation_number == check_balance:
            self.check_balance()
        elif operation_number == cash_withdrawal:
            self.cash_withdrawal()
        elif operation_number == cash_deposit:
            self.cash_deposit()
        elif operation_number == change_password:
            self.change_password()
        else:
            print("the requested operation doesn't exist, please try again")
            self.get_desired_operation()

    def check_balance(self):
        print("Your balance is now:\n" + self.consumer.get_balance())

    def cash_withdrawal(self):
        is_valid = False
        while not is_valid:
            requested_sum = raw_input('Please enter the sum you wish to withdrawal:\n')
            consumer_balance = int(self.consumer.get_balance())
            if consumer_balance <= 0:
                print("Sorry, there's no option to withdrawal cash, please go to your branch")
                is_valid = True
            elif consumer_balance - int(requested_sum.strip()) < 0:
                print("Sorry,  no option to withdrawal that amount of cash, try a smaller amount")
                is_valid = False
            else:
                print("The cash will come out from below")
                is_valid = True
                new_balance = consumer_balance - int(requested_sum.strip())
                self.consumer.set_balance(str(new_balance))
                print("Your balance is now:\n" + str(new_balance))
                self.need_update = True

    def cash_deposit(self):
        inserted_sum = raw_input('Please enter the sum you wish to deposit:\n')
        consumer_balance = self.consumer.get_balance()
        new_balance = int(consumer_balance) + int(inserted_sum)
        self.consumer.set_balance(str(new_balance))
        print("Your balance is now:\n" + str(new_balance))
        self.need_update = True

    def change_password(self):
        is_valid = False
        if self.consumer.password == raw_input('Please enter current password:\n'):
            new_password = raw_input('Enter new password:\n')
            while not is_valid:
                if new_password == raw_input('Enter new password again:\n'):
                    self.consumer.set_password(new_password)
                    is_valid = True
                else:
                    print("try again")
        else:
            print("Wrong password, try again")
            self.change_password()
        self.need_update = is_valid
