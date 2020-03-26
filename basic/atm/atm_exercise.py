"""atm program which allows users to preform actions on customers."""
PASS_KEY = "atm_password"
BALANCE_KEY = "balance"


def check_balance(customers_data, customer_id):
    """Print the given customer's balance.

    Args:
        customers_data (dict): Dictionary with the atm file's data.
        customer_id (str): The specific customer id to work on.
    """
    balance = customers_data[customer_id][BALANCE_KEY]
    print(f"{customer_id}'s balance is: {balance}")


def get_a_number(message_input):
    """Get a number from the user and return it.

    Args:
        message_input (str): The user input message.

    Returns:
        int: Number given by user.
    """
    while True:
        number = input(message_input + "\n")
        try:
            return float(number)
        except ValueError:
            print("This is not a number, try again.")
            continue


def get_balance(customers_data, customer_id):
    """Return the given customer's balance.

    Args:
        customers_data (dict): Dictionary with the atm file's data.
        customer_id (str): The specific customer id to work on.

    Returns:
        int: The given customer's balance.
    """
    balance = customers_data[customer_id][BALANCE_KEY]
    return float(balance)


def cash_withdrawal(customers_data, customer_id):
    """Deduct the 'amount_to_withdrawal' from the customer's balance.

    Args:
        customers_data (dict): Dictionary with the atm file's data.
        customer_id (str): The specific customer id to work on.
    """
    curr_balance = get_balance(customers_data, customer_id)
    msg = "Enter the amount you want to withdrawal."
    amount_to_withdrawal = get_a_number(msg)
    if amount_to_withdrawal <= curr_balance:
        new_balance = curr_balance - amount_to_withdrawal
        customers_data[customer_id][BALANCE_KEY] = new_balance
        print(f"withdrawal was successful {customer_id} now has {new_balance}$.")
    else:
        print("You cannot draw more money than what you have in the bank.")


def cash_deposit(customers_data, customer_id):
    """Add the 'amount_to_deposit' to the customer's balance.

    Args:
        customers_data (dict): Dictionary with the atm file's data.
        customer_id (str): The specific customer id to work on.
    """
    amount_to_deposit = get_a_number("Enter the amount you want to deposit.")
    new_balance = get_balance(customers_data, customer_id) + amount_to_deposit
    customers_data[customer_id][BALANCE_KEY] = new_balance
    print(f"withdrawal was successful {customer_id} now has {new_balance}$.")


def change_password(customers_data, customer_id):
    """Change the given customer's password.

    Args:
        customers_data (dict): Dictionary with the atm file's data.
        customer_id (str): The specific customer id to work on.
    """
    new_pass = input("Enter a new password.\n")
    customers_data[customer_id][PASS_KEY] = new_pass
    print(f"Password was changed to {new_pass}")


def get_data_from_file(filename):
    """Get bank details from file, arrange and return them in dictionary.

    Args:
        filename (str): The path to the atm details file.

    Returns:
         dict: Dictionary of all customer's data from the file.
    """
    try:
        with open(filename, "r") as atm_file:
            customers = {}
            for line in atm_file:
                customer_id, the_pass, balance = line.split()
                customer = {PASS_KEY: the_pass, BALANCE_KEY: balance}
                customers[customer_id] = customer
        return customers
    except FileNotFoundError as e:
        print(e)
        return -1


def execute_choice(customers_data, customer_id, choice):
    """Execute a function according to the choice given.

    Args:
        customers_data (dict): Dictionary with the atm file's data.
        customer_id (str): The specific customer id to work on.
        choice (str): The user's desired function to execute.
    """
    if choice == "1":
        check_balance(customers_data, customer_id)

    elif choice == "2":
        cash_withdrawal(customers_data, customer_id)

    elif choice == "3":
        cash_deposit(customers_data, customer_id)

    else:
        change_password(customers_data, customer_id)


def update_file(filename, data):
    """Update the file with the data in the given dict 'data'.

    Args:
        filename (str): Path too the atm file.
        data (dict): Dictionary with data from the atm file.
    """
    with open(filename, "w") as atm_file:
        for key in data:
            line = f"{key} {data[key][PASS_KEY]} {data[key][BALANCE_KEY]}\n"
            atm_file.write(line)


def operations_for_customer(data, customer_id):
    """Get desired operation by user and execute it.

    Args:
        data (dict): Dictionary with data from the atm file.
        customer_id (str): The specific customer id to work on.
    """
    while True:
        operation = input("""What operation do you want to do?(-1 to stop)
        1 to check balance
        2 to withdrawal
        3 for cash deposit
        4 to change password\n""")
        if operation == "-1":
            break

        elif operation not in "1234":
            print("you have to enter one of the options, try again.")
            continue
        execute_choice(data, customer_id, operation)


def atm(filename):
    """Perform operations on customers from the given file and update the data.

    Args:
        filename (str): The path to the file with the bank details.
    """
    data = get_data_from_file(filename)
    if data == -1:
        return

    while True:
        msg = "enter the ID of the customer you want (-1 to turn off).\n"
        customer_id = input(msg)
        if customer_id == "-1":
            break
        elif customer_id not in data:
            err_msg = "The ID you entered doesn't exist, try again."
            print(err_msg)
            continue

        operations_for_customer(data, customer_id)

    update_file(filename, data)


def main():
    path = r"C:\Users\keren\Desktop\atmDetails.txt"
    atm(path)


if __name__ == "__main__":
    main()
