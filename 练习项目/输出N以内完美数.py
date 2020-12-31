#输出N以内的完美数
n = int(input("多少以内的完美数："))
for x in range(1,n):
    number = 0
    for y in range(1,n):
        if x % y == 0:
            number+=y
            if x==number:
                print(x)