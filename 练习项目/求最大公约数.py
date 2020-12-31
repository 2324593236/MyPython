#求最大公约数与最小公倍数
def maxys(x,y):
    if x>y:
        z = x
        x = y
        y = z
    for number in range(x,1,-1):
        if x % number == 0 and y % number == 0:
            return number
def minbs(x,y):
    for number in range(1,x*y):
        if number % x == 0 and number % y == 0:
            return number
x = int(input("输入第一个数："))
y = int(input("输入第一个数："))
number1 = maxys(x,y)
number2 = minbs(x,y)
print(number1,x,y)
print(number2,x,y)
