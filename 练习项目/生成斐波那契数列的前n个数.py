#生成斐波那契数列的前N个数
number1 = 0
number2 = 1   
number = []
n = int(input("前多少个数字："))
while len(number)<=n:
    number3 = number1+number2
    number.append(number2)
    number1 = number2
    number2 = number3
    if len(number)>=n:
        break
print("前%d个数字"%len(number),number)
