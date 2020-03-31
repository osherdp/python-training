class ATM:
    def __init__(self, id, password, balance):
        self.__id = id
        self.__password = password
        self.__balance = int(balance)

    def get_id(self):
        return self.__id

    def set_password(self, password):
        self.__password = password

    def get_balance(self):
        return self.__balance

    def withdrawal(self, amount):
        self.__balance = self.__balance - amount

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def __str__(self):
        return "{} {} {}".format(self.__id, self.__password, self.__balance)

