
def delete_old_file(pfile):
    """delete the old file of ATM data
    """
    pfile.seek(0)
    pfile.truncate()
    pfile.seek(0) # I believe this seek is redundant
    return pfile
def file_to_list(file):
    """convert file to list
        """
    text = file.read()
    list_1 = text.split('\n')
    i = 0
    list_2 = []
    while i < len(list_1):
        list_2 = list_2 + list_1[i].split(',')
        i = i + 1
    return list_2
def dictionary_id_password(list):
    """create dictionary id:password from list
                """
    i = 0
    password_dct = {list[i]: list[i + 1] for i in range(0, len(list) - 1, 3)}
    return password_dct
def dictionary_id_money(list):
    """create dictionary id:money from list
            """
    i = 0
    money_dct = {list[i]: list[i + 2] for i in range(0, len(list) - 1, 3)}
    return money_dct
def get_password(id,password):
    """check and change the password
            """
    inncorrect_flag = 1
    while (inncorrect_flag == 1):
        if input('input your password:\n') == password.get(id):
            inncorrect_flag = 0
            if input('Do you want your password?:\n') == 'yes':
                password[id] = input('new password?:\n')
        else:
            print('incorrect password')
            inncorrect_flag = 1

    return  password
def Cash_withdrawal(money):
    """check cash withdrawal
               """
    if input('Do you want to do Cash withdrawal?:\n') == 'yes':
        money[id] = float(money[id]) - float(input('how much Cash withdrawal:\n'))
        print("your balance is", money.get(id))
    return money
def Cash_deposit(money):
    """check cash deposit
                  """
    if input('Do you want to do Cash deposit?:\n') == 'yes':
        money[id] = float(money[id]) + float(input('Cash deposit:\n'))
        print("your balance is", money.get(id))
    return money
def dictionary_to_file(password,money,file):
    """change dictionary back to file
                  """
    l = []
    [l.extend([k, v]) for k, v in password.items()]
    l_1 = l[0:len(l):2]

    l_2 = l[1:len(l):2]

    j = []
    [j.extend([k, v]) for k, v in money.items()]
    j = j[1:len(l):2]
    i = 0
    while i < len(l_1):
        l_1[i] = str(l_1[i]) + ',' +str(l_2[i]) + ',' + str(j[i])
        i += 1
    text = '\n'.join(l_1)
    file = file.write(text)
    return file

    if __name__ == '__main__':
        main()
file = open(r'C:\Users\97254\Documents\GitHub\python-training\basic\atm\file.txt', 'r')
list_file = file_to_list(file)
password = dictionary_id_password(list_file)
money = dictionary_id_money(list_file)
id = input('input your id:\n')
if int(id) != -1:
    update_password = get_password(id,password)
    print("your balance is",money.get(id))
    update_money = Cash_withdrawal(money)
    update_money = Cash_deposit(money)
    file= delete_old_file(open(r'C:\Users\97254\Documents\GitHub\python-training\basic\atm\file.txt', 'a'))
    file = dictionary_to_file(update_password,update_money,file)
else:
    print('close the ATM')

