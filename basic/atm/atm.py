#def  dictionary(old):
   # text= old.read()
  # list_1 = text.split('/n')
   # update_id = id(list_1[0])
   #  return
def deleteContent(pfile):

    pfile.seek(0)
    pfile.truncate()
    pfile.seek(0) # I believe this seek is redundant
    return pfile


file = open(r'C:\Users\97254\Documents\GitHub\python-training\basic\atm\file.txt', 'r')

text= file.read()
list_1 = text.split('\n')

i = 0
list_2 = []
while i< len(list_1):
    list_2 = list_2 + list_1[i].split(',')
    i = i+1
i = 0
password_dct = {list_2[i]: list_2[i + 1] for i in range(0, len(list_2)-1, 3)}
money_dct = {list_2[i]: list_2[i + 2] for i in range(0, len(list_2)-1, 3)}


id = input('input your id:\n')
#password = password_dct.get(id)
money = money_dct.get(id)

count = 0
inncorrect_flag = 1
while(inncorrect_flag == 1):
    if input('input your password:\n') == password_dct.get(id) :
         inncorrect_flag = 0
         if input('Do you want your password?:\n') == 'yes':
             password_dct[id] = input('new password?:\n')
         print("your balance is",money_dct.get(id))
         if input('Do you want to do Cash withdrawal?:\n') == 'yes':
             money_dct[id] = float(money_dct[id])- float(input('how much Cash withdrawal:\n'))
             print("your balance is", money_dct.get(id))
         if input('Do you want to do Cash withdrawal?:\n') == 'yes':
             money_dct[id] = float(money_dct[id]) + float(input('Cash deposit:\n'))
             print("your balance is", money_dct.get(id))

    else:
         print('incorrect password')
         inncorrect_flag = 1
         count = count + 1
         if (count == 3):
             print('You entered the wrong password three times')
             break

#I = password_dct.items()
l=[]
[l.extend([k,v]) for k,v in password_dct.items()]
l_1=l[0:len(l):2]

l_2=l[1:len(l):2]

j=[]
[j.extend([k,v]) for k,v in money_dct.items()]
j=j[1:len(l):2]
while i < len(l_1):
    l_1[i] = l_1[i] + ',' + l_2[i] + ',' + j[i]
    i += 1
text_2 = '\n'.join(l_1)

file= deleteContent(open(r'C:\Users\97254\Documents\GitHub\python-training\basic\atm\file.txt', 'a'))
file = file.write(text_2)
print(text_2)
