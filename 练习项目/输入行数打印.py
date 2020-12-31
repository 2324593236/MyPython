number = int(input("请输入行数："))
for y in range(number) :
    for x in range(y+1):
        print("*",end = '')
    print()

for y in range(number):
    for x in range(number):
        if x < number-y-1:
            print(" ",end="")
        else:
            print("*",end = "")
    print()

for y in range(number):
    for _ in range(number-y-1):
        print(' ', end='')
    for x in range(y*2+1):
        print('*', end='')
    print()