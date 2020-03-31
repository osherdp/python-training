class ATM:
    NAME_INDEX = 0
    PASSWORD_INDEX = 1
    BALANCE_INDEX = 2
    ID_INDEX = 3
    CUSTOMER_LINE_FORMAT = '{};{};{};{}\n'

    def get_customers(self, file_path):
        with open(file_path, 'r') as file:
            customers = {}
            for line in file.readlines():
                data = line.strip().split(';')
                customers[data[self.ID_INDEX]] = [data[self.NAME_INDEX],
                                                  data[self.PASSWORD_INDEX],
                                                  int(data[self.BALANCE_INDEX])]
        return customers

    def check_balance(self, customers, ID):
        print('Your balance is: {}'.format(customers[ID][self.BALANCE_INDEX]))

    def deposit(self, customers, ID):
        try:
            amount = int(input('Enter amount to deposit: '))
            if amount > 0:
                customers[ID][self.BALANCE_INDEX] += amount
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter an integer')

    def withdraw(self, customers, ID):
        try:
            amount = int(input('Enter amount to withdraw: '))
            if amount > 0:
                customers[ID][self.BALANCE_INDEX] -= amount
            else:
                print('Please enter a positive number')
        except ValueError:
            print('Please enter an integer')

    def change_password(self, customers, ID):
        tries = 0
        while tries < 3:
            password = input('Enter old password: ')
            if password == customers[ID][self.PASSWORD_INDEX]:
                customers[ID][self.PASSWORD_INDEX] = input(
                    'Enter new password: ')
                break
            else:
                print('Incorrect password, try again')
                tries += 1
        if tries == 3:
            print('Exceeded number of tries allowed')

    def update_file(self, customers, file_path):
        with open(file_path, 'w') as customers_file:
            for key in customers:
                customers_file.writelines(self.CUSTOMER_LINE_FORMAT.format(
                    customers[key][self.NAME_INDEX],
                    customers[key][self.PASSWORD_INDEX],
                    customers[key][self.BALANCE_INDEX],
                    key))
