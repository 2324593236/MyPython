#判断一个数是否是回文数
number1 = input("输入要判断的数：")
number2 = list(number1)
number2 = "".join(number2[::-1])
if number1 == number2:
    print(number1,"是回文数")
else:
    print(number1,"不是回文数")