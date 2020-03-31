class Costumer(object):
    def __init__(self, _id, password, balance):
        self.id = _id
        self.password = password
        self.balance = balance

    def set_password(self, new_password):
        self.password = new_password

    def get_balance(self):
        return self.balance

    def set_balance(self, updated_bal):
        self.balance = updated_bal

    def __str__(self):
        return "{},{},{}\n".format(self.id, self.password, self.balance)
