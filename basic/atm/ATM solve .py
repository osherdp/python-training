__author__ = 'Shaked Manor'
# takes customers information from file' then
# creating objects from class customers with the customers information
# takes input from user, checking his ID ans password and then
# let the customer commit actions on his account

CUSTOMERS_INFORMATION_FILE = r'c:\python\ATM.txt'
END_VALUE = -1
customer_passwords = {}
customer_access_to_class = {}


class customers:
    """defining the actions that a customer can do in is account,
     checking his balance, withdrawal and deposit money and change password"""

    def __init__(self, password, balance):
        self.password = password
        self.balance = balance

    def get_balance(self):
        return self.balance

    def cash_withdrawal(self):
        withdrawal_amount = input('please enter the amount of money you want to withdrawal')
        self.balance -= float(withdrawal_amount)
        print f"the remainder of money in your account is: {self.balance}"

    def cash_deposit(self):
        deposit_amount = input('please enter the amount you want to deposit')
        self.balance += float(deposit_amount)
        print f"the remainder of money in your account is: {self.balance}"

    def change_password(self):
        y = input('please enter new password')
        self.password = str(y)


def users_input():
    """takes users input, ID and password and compares it to the customer_password
    dictionary to confirm its right. then takes the users wanted action and commit it"""
    while True:
        customer_input = input('please enter your customer ID')

        if customer_input == END_VALUE:
            print ('off')
            break

        else:
            try:
                customer_id = str(customer_input)
                customer_access = customer_access_to_class[customer_id]

            except TypeError:
                print ('wrong ID')
                users_input()

            password_input = input('please enter your ATM password')
            str_password = str(password_input)
            if str_password == customer_passwords[customer_id]:
                print 'you can:\n1.Check the balance.\n2.Cash withdrawal.\n3.Cash deposit.\n4.Change password.\n'
                users_action = input('enter the number of the wanted action')
                if users_action == 1:
                    print customer_access.get_balance()

                if users_action == 2:
                    customer_access.cash_withdrawal()

                if users_action == 3:
                    customer_access.cash_deposit()

                if users_action == 4:
                    customer_access.change_password()
                    customer_passwords[customer_id] = customer_access.y

            else:
                print ('wrong password')
                users_input()


if __name__ == '__main__':
    def main():
        """takes the customers information from file(ID, password, balance),
         then placing it un customers() objects.
         also making each ID the key for the value of each password"""

        customers_file = open(CUSTOMERS_INFORMATION_FILE, 'r')
        for line in customers_file:
            line = line.split(',')
            customer_access_to_class[line[0]] = customers(line[1], float(line[2]))
            customer_passwords[line[0]] = line[1]
        users_input()
    main()


