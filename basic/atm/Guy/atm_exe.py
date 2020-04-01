"""
#ATM Exercise
## Goals
1. User input.
2. Dictionaries.
3. Functional programing.

## Introduction
Write a program that will simulate an ATM. When the program
will initialize it will read a file containing
all the customers of the bank. The file will specify for
each customer its customer-ID, ATM password,
and the consumer balance (that can be negative).

The ATM will allow the following options to a using costumer:
1. Check the balance.
2. Cash withdrawal.
3. Cash deposit.
4. Change password.

To turn off the ATM, enter `-1` as the customer ID. When the ATM
will be turned off, it will
save the current state of all the bank customers.

## Recommendations & Notes

* Use a simple file for the customers data. Each customer will
be a single line and their information
will come in a known order separated by a comma or a space.
* Use dictionaries to find the user data based on the customer-ID.
"""

PASSWORD = 0
BALANCE = 1


def load_file(filename):
    """
    this function receive input file path - with bank customer data
    load all customers data into a dictionary and return it
    """
    bank_dict = {}
    fd_in = open(filename, 'r')
    for line in fd_in:
        stop_id = line.find(',')
        customer_id = line[0:stop_id:1]
        id_details = line[stop_id + 1:len(line) - 1:1]
        bank_dict[customer_id] = id_details.split(',')
    fd_in.close()
    return bank_dict


def save_file(filename, bank_dict):
    """
    this function receive bank dictionary and destination file
    save all data from dictionary to the file.
    """
    fd_out = open(filename, 'w')
    for item in bank_dict:
        fd_out.write(item + ',' + str(bank_dict[item][PASSWORD]) +
                     ',' + str(bank_dict[item][BALANCE]) + "\n")
    fd_out.close()


def main():
    # txt file should be without spaces and only with ',' between details
    # call a function that reads all text file into dictionary
    filename = r"C:\Users\guyha\PycharmProjects\python-training\basic" \
               r"\atm\Guy\atm.txt"
    bank_dict = load_file(filename)
    # break from while true only if someone entered -1
    user_input_id = raw_input("Welcome to ATM! Please insert your customer-ID"
                              " \nFor Turning-off ATM please enter -1 \n")
    while user_input_id != '-1':
        # check id - if not valid print error
        if not (user_input_id in bank_dict):
            print "Error - not a valid ID \n"
        else:
            user_input_psw = raw_input("Please insert your password \n")
            # verify user by password if not valid print error
            if bank_dict[user_input_id][PASSWORD] != user_input_psw:
                print "Error - not a valid password \n"
            else:
                # after verifying customer id and password
                # get action from user
                # do wanted task according to user input
                user_input_act = raw_input("Please choose one of the following"
                                           " options\n 1.Check the balance.\n"
                                           " 2.Cash withdrawal.\n"
                                           " 3.Cash deposit.\n"
                                           " 4.Change password.\n")
                if user_input_act == '1':
                    print "Your Current Balance account is: {}".\
                        format(bank_dict[user_input_id][BALANCE])
                    print "Have a nice day! \n"
                elif user_input_act == '2':
                    user_input_val = raw_input("Insert value to withdraw \n")
                    bank_dict[user_input_id][BALANCE] = \
                        int(bank_dict[user_input_id][BALANCE]) - \
                        int(user_input_val)
                    print "Your Current Balance account is: {} \n"\
                        .format(bank_dict[user_input_id][BALANCE])
                    print "Have a nice day! \n"
                elif user_input_act == '3':
                    user_input_val = raw_input("Insert value to deposit \n")
                    bank_dict[user_input_id][BALANCE] = \
                        int(bank_dict[user_input_id][BALANCE]) + \
                        int(user_input_val)
                    print "Your Current Balance account is: {} \n".\
                        format(bank_dict[user_input_id][BALANCE])
                    print "Have a nice day! \n"
                elif user_input_act == '4':
                    user_input_val = raw_input("Insert new password \n")
                    bank_dict[user_input_id][PASSWORD] = user_input_val
                    print "Your Password has been changed successfully\n"
                    print "Have a nice day! \n"
                else:
                    print "Error - not a valid action \n"
        user_input_id = raw_input("Welcome to ATM! Please insert your"
                                  " customer-ID \n" +
                                  "For Turning-off ATM please enter -1 \n")
    # save changes to file.
    save_file(filename, bank_dict)
    print "Good Bye!"


if __name__ == '__main__':
    main()
