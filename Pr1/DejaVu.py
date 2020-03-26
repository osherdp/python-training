NUM_OF_DIGITS = 5


def ask_for_input():
    """ Asking an input from the user
    """
    return input('Please insert a 5 digit number: \n')


def check_digits(user_input):
    """ Check if the number of digits is as requested
    """
    if len(user_input) != NUM_OF_DIGITS:
        return False
    else:
        return True


def check_if_number(user_input):
    """ Check if the user's input is a number (and not a list/string/table)
    """
    if user_input.isdigit():
        return True
    else:
        return False


def print_digits(user_input):
    """ Print the number's digits with space and ,
    """
    new_list = []
    print('The digits of the number are: ', end='')
    for i in range(len(user_input)):
        new_list.append(user_input[i])
        if i != (len(user_input) - 1):
            print('{}, '.format(user_input[i]), end='')
        else:
            print('{}\n'.format(user_input[i]))
    return new_list


def sum_of_digits(user_input):
    """ Calculate the sum of the number's digits
    """
    res = 0
    for i in range(len(user_input)):
        res = res + int(user_input[i])
    return res


def main():
    while True:
        user_input = ask_for_input()
        if check_digits(user_input) and check_if_number(user_input):
            print('You entered the number: {}\n'.format(user_input))
            print_digits(user_input)
            print('The sum of the digits is: {}\n'.format(sum_of_digits(user_input)))
            break
    # assert check_digits('12345') is True
    # assert check_digits('16857') is True
    # assert check_digits('123') is False
    # assert check_digits('345') is False
    # assert check_digits('19876532') is False


if __name__ == "__main__":
    main()
