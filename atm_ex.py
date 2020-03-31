import atm


def start_atm(line):
    user = atm.ATM(line.split()[0], line.split()[1], line.split()[2])
    action = 0
    while action != -1:
        action = input("enter number: \n"
                       "1 - Check the balance\n"
                       "2 - Cash withdrawal\n"
                       "3 - Cash deposit\n"
                       "4 - Change password\n"
                       "-1 - exit\n")
        action = int(action)
        if action == 1:
            print("your balance: {}".format(user.get_balance()))
        if action == 2:
            amount = input("enter amount\n")
            if amount.isdigit():
                user.withdrawal(int(amount))
            else:
                print("not a number")
        if action == 3:
            amount = input("enter amount\n")
            if amount.isdigit():
                user.deposit(int(amount))
            else:
                print("not a number")
        if action == 4:
            user.set_password(input("set password"))
    return user


def main():
    user = None
    lines = ''
    input_password = input("enter password \n")
    file_read = open(r'C:\Users\nimro\Documents\python_test\atm\users.txt', 'r')
    for line in file_read:
        row = line.replace('\n', '')
        words = row.split()
        if words[1] == input_password:
            user = start_atm(row)
            lines = lines + user.__str__() + '\n'
        else:
            lines = lines + line

    if user is not None:
        with open(r'C:\Users\nimro\Documents\python_test\atm\users.txt', 'w') as write_file:
            write_file.write(lines)
        print("Done!")
    else:
        print("wrong password")


if __name__ == '__main__':
    main()
