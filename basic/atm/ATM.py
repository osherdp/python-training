class ATM:
    PATH_SAVING_FILE = "ATM_data_base.txt"

    def __init__(self):
        self._accounts_dict = {}
        with open(ATM.PATH_SAVING_FILE, "r") as f:

            account_lst = f.readlines()
        for account in account_lst:
            account = account.split()
            self._accounts_dict[account[0]] = [account[1], int(account[2])]

    def get_account_dict(self):
        return self._accounts_dict

    def check_password(self, id_number, password):
        return self._accounts_dict[id_number][0] == password

    def check_the_balance(self, id_number):
        return self._accounts_dict[id_number][1]

    def cash_deposit(self, id_number, deposit):
        self._accounts_dict[id_number][1] += deposit

    def cash_withdrawal(self, id_number, withdrawal):
        self._accounts_dict[id_number][1] -= withdrawal

    def change_password(self, id_number, new_password):
        self._accounts_dict[id_number][0] = new_password

    def save_changes_to_file(self):
        with open(ATM.PATH_SAVING_FILE, "w") as f:
            for account in self._accounts_dict:
                f.write("%s %s %d\n" % (account, self._accounts_dict[account][0], self._accounts_dict[account][1]))


def log_in_atm(atm):
    """
    The function identify the user and checks is password.
    :param atm: An ATM object.
    """
    id_number = ""
    requested_to_exit = False
    while not requested_to_exit:
        id_number = input("Welcome, enter id number\n")
        if id_number in atm.get_account_dict():

            password = input("Enter password\n")
            if atm.check_password(id_number, password):
                requested_to_exit = True
            else:
                print("The password is not correct, try again.")
        else:
            print("This id is not in the system, try again.")

    main_menu(atm, id_number)


def main_menu(atm, id_number):
    """
    The main menu of the ATM, allowing multiple options to the user.
    :param atm: An ATM object.
    :param id_number: The id number of the user.
    """
    choice_flag = False
    while not choice_flag:
        choice = input("Hello,\n enter 1 - to check the balance\nEnter 2 - to deposit cash\n"
                       "Enter 3 - for cash withdrawal\nEnter 4 - to change password\nEnter -1 - to exit ATM.\n")
        if choice == '1':
            print("Your balance is", atm.check_the_balance(id_number))

        elif choice == '2':
            deposit = int(input("Enter the amount of money you want to deposit.\n"))
            atm.cash_deposit(id_number, deposit)
            print("The deposit went successfully. Your balance is", atm.check_the_balance(id_number))

        elif choice == '3':
            withdrawal = int(input("Enter the amount of money you want to withdrawal.\n"))
            atm.cash_withdrawal(id_number, withdrawal)
            print("The withdrawal went successfully. Your balance is", atm.check_the_balance(id_number))

        elif choice == '4':
            old_password_flag = False
            while not old_password_flag:
                old_password = input("Please enter your old password, enter -1 to exit.\n")
                if atm.check_password(id_number, old_password):
                    new_password = int(input("Enter your new password\n"))
                    atm.change_password(id_number, new_password)
                    print("The had changed successfully.")
                    old_password_flag = True
                elif old_password == '-1':
                    old_password_flag = True
                else:
                    print("Your password is not correct")

        elif choice == '-1':
            atm.save_changes_to_file()
            print("Bye")
            choice_flag = True
        else:
            print("\nYour choice is not valid, try again.")


if __name__ == '__main__':
    new_atm = ATM()
    log_in_atm(new_atm)
