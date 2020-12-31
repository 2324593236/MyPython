###从1到N求和
number = int(input("输入N的值"))
sum = 0
if number:
    if number>=0:
        for i in range(number+1):
            sum += i
        print(sum)
    else:
        print("请正确输入")