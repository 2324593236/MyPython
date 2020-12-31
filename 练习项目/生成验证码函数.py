import random
import re
def password(self):
    while True:
        list1 = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ")
        values = [random.choice(list1) for i in range(self)]
        string = ''
        for i in values:
            string += i
        if bool(re.search(r'\d',string)) and bool(re.search(r'[a-z]',string)) and bool(re.search(r'[A-Z]',string)):
            return(string)
            break
        else:
            continue

number = input("验证码位数：")
if number != '':
    print(password(int(number)))
