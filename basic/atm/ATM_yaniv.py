# each line in the file should be: id,password,balance

import sys

file = sys.argv[1]

# from ATM import Bankclient

class Bankclient ():
    def __init__(self, balance, password):
        self.balance = float (balance)
        self.password = password

    def Getbalance(self):
        return self.balance

    def Getpassword(self):
        return self.password

    def withdrawal(self, withdrawal):
        self.balance = self.balance - withdrawal

    def deposit(self, deposit):
        self.balance = self.balance + deposit

    def change_password(self, password):
        self.password = password

    def str_info(self):
        return "Bank client data is: balance:{} password: {}".format(self.Getbalance(), self.Getpassword())



def create_database(file1):
    # receives a file and returns a dictionary
    # the dictionary keys are id and the values are Bankclient objects

    password = {}
    balance = {}

    input_file = open (file1)
    line_by_line_file = 0
    while line_by_line_file != '':
        line_by_line_file = input_file.readline ()
        line_by_line_file_split = line_by_line_file.split(",")
        if len(line_by_line_file_split) == 3:
            line_by_line_file_split[2] = line_by_line_file_split[2].replace("\n", "")
            balance[line_by_line_file_split[0]] = line_by_line_file_split[2]
            password[line_by_line_file_split[0]] = line_by_line_file_split[1]

    all_clients = {}
    for key in balance:
        all_clients[key] = Bankclient (balance[key], password[key])
    return all_clients


def save_database(all_clients, file1):

    # saves the data to the txt file when the ATM is turned off
    # receives a dictionary and a file

    str_save = ""
    for key in all_clients:
        str_save = str_save + (
            "{},{},{}\n".format(key, all_clients[key].Getpassword(), str((all_clients[key].Getbalance()))))
    print (str_save)
    overwrite_file = open(file1, 'w')
    overwrite_file.write(str_save)


def main():
    file1 = sys.argv[1]
    all_clients = create_database (file)
    id_input = ""
    action_input = ""
    info_input = ""
    list1 = ["1", "2", "3", "4"]

    while id_input != "-1":
        print("hello, insert ID")
        id_input = input("")
        if id_input == "-1":
            break
        print ("enter option number (1-4):\n1-Check the balance.\n2-Cash withdrawal.\n3-Cash deposit.\n4-Change "
               "password.")
        try:
            action_input = input("")
            if action_input not in list1:
                print("action number must be between 1-4")

            if action_input == "1":
                print("your balance is:{}".format(all_clients[id_input].Getbalance()))

            if action_input == "2":
                try:
                    print("insert amount to withdrawal")
                    info_input = input('')
                    all_clients[id_input].withdrawal(float(info_input))
                    print("your balance is:{}".format(all_clients[id_input].Getbalance()))
                except:
                    print("input must be number")

            if action_input == "3":
                try:
                    print("insert amount to deposit")
                    info_input = input ('')
                    all_clients[id_input].deposit(float(info_input))
                    print("your balance is:{}".format(all_clients[id_input].Getbalance()))
                except:
                    print("input must be number")

            if action_input == "4":
                print("insert new password")
                info_input = input('')
                all_clients[id_input].change_password(info_input)
                print("your new password is:{}".format(all_clients[id_input].Getpassword()))

        except:
            print("id is not exist")
    save_database(all_clients, file)


if __name__ == "__main__":
    main()
