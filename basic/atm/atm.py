class ATM:
    NAME_INDEX = 0
    PASSWORD_INDEX = 1
    BALANCE_INDEX = 2
    ID_INDEX = 3
    CUSTOMER_LINE_FORMAT = '{};{};{};{}\n'

    def __init__(self, file_path):
        self.file_path = file_path
        self.customers = self.get_customers()

    def get_customers(self):
        with open(self.file_path, 'r') as file:
            customers = {}
            for line in file.readlines():
                data = line.strip().split(';')
                customers[data[self.ID_INDEX]] = [data[self.NAME_INDEX],
                                                  data[self.PASSWORD_INDEX],
                                                  int(data[
                                                          self.BALANCE_INDEX])]
        return customers

    def check_balance(self, ID):
        print('Your balance is: {}'.format(
            self.customers[ID][self.BALANCE_INDEX]))

    def deposit(self, ID):
        try:
            amount = int(input('Enter amount to deposit: '))
            if amount > 0:
                self.customers[ID][self.BALANCE_INDEX] += amount
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter an integer')

    def withdraw(self, ID):
        try:
            amount = int(input('Enter amount to withdraw: '))
            if amount > 0:
                self.customers[ID][self.BALANCE_INDEX] -= amount
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter an integer')

    def change_password(self, ID):
        tries = 0
        while tries < 3:
            password = input('Enter old password: ')
            if password == self.customers[ID][self.PASSWORD_INDEX]:
                self.customers[ID][self.PASSWORD_INDEX] = input(
                    'Enter new password: ')
                break
            else:
                print('Incorrect password, try again')
                tries += 1
        if tries == 3:
            print('Exceeded number of tries allowed')

    def update_file(self):
        with open(self.file_path, 'w') as customers_file:
            for key in self.customers:
                customers_file.writelines(self.CUSTOMER_LINE_FORMAT.format(
                    self.customers[key][self.NAME_INDEX],
                    self.customers[key][self.PASSWORD_INDEX],
                    self.customers[key][self.BALANCE_INDEX],
                    key))
