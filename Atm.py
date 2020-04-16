from pip._vendor.distlib.compat import raw_input

from Costumer import Costumer

COSTUMERS_DICTIONARY = {}
FILE_PATH = r'C:\Users\mayar\Desktop\Python\ATM\costumers.txt'
CONSUMER = ''


def get_current_consumer():
    consumer_id = raw_input('To turn off insert -1\nPlease enter your id:\n')
    global CONSUMER
    if int(consumer_id) != -1:
        try:
            CONSUMER = COSTUMERS_DICTIONARY[consumer_id.strip()]
            return True
        except:
            print("No account for the inserted id, please try again")
            get_current_consumer()
    else:
        return False


def check_password():
    is_valid = False
    for i in range(3):
        entered_password = raw_input('To move on, please enter your password:\n')
        if entered_password == CONSUMER.password:
            is_valid = True
            break
        else:
            print("The inserted password was wrong")
    return is_valid


def update_details():
    lines = []
    for consumer in COSTUMERS_DICTIONARY.values():
        lines.append(consumer.__str__())
    with open(FILE_PATH, 'w') as set_new_file:
        set_new_file.writelines(lines)


def check_balance():
    print("Your balance is now:\n" + CONSUMER.get_balance())


def cash_withdrawal():
    is_valid = False
    while not is_valid:
        requested_sum = raw_input('Please enter the sum you wish to withdrawal:\n')
        consumer_balance = int(CONSUMER.get_balance())
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
            CONSUMER.set_balance(str(new_balance))
            print("Your balance is now:\n" + str(new_balance))
    return is_valid


def cash_deposit():
    inserted_sum = raw_input('Please enter the sum you wish to deposit:\n')
    consumer_balance = CONSUMER.get_balance()
    new_balance = int(consumer_balance) + int(inserted_sum)
    CONSUMER.set_balance(str(new_balance))
    print("Your balance is now:\n" + str(new_balance))
    return True


def change_password():
    is_valid = False
    if CONSUMER.password == raw_input('Please enter current password:\n'):
        new_password = raw_input('Enter new password:\n')
        while not is_valid:
            if new_password == raw_input('Enter new password again:\n'):
                CONSUMER.set_password(new_password)
                is_valid = True
            else:
                print("try again")
    else:
        print("Wrong password, try again")
        change_password()
    return is_valid


def get_desired_operation():
    has_changed = False
    print('Hi! welcome to your account, choose your act: ')
    operation_number = raw_input('1 Check balance\n'
                                 '2 Cash withdrawal\n'
                                 '3 Cash deposit\n'
                                 '4 Change password\n')

    operation_number = int(operation_number.strip())
    if operation_number == 1:
        check_balance()
    elif operation_number == 2:
        has_changed = cash_withdrawal()
    elif operation_number == 3:
        has_changed = cash_deposit()
    elif operation_number == 4:
        has_changed = change_password()
    else:
        print("the requested operation doesn't exist, please try again")
        get_desired_operation()
    return has_changed


def main():
    has_data_changed = False
    with open(FILE_PATH, 'r') as file:
        costumers = [i[:i.find('\n')] for i in file.readlines()]
    costumers = [i.split(',') for i in costumers]
    global COSTUMERS_DICTIONARY
    for i in costumers:
        if i[0] and i[1] and i[2]:
            costumer = Costumer(i[0], i[1], i[2])
            _id = i[0]
            COSTUMERS_DICTIONARY[_id] = costumer
    while get_current_consumer():
        if check_password():
            has_data_changed = get_desired_operation()
            print('Thanks you for using our services!')
    if has_data_changed:
        update_details()


if __name__ == '__main__':
    main()
