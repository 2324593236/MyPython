#输出N以内的素数
n = int(input("多少以内的素数："))
if n:
    for i in range(n):
        if i ==2 or i==3:
            print(i)
        elif i!=0 and i!=1:
            if i%2!=0 and i%3!=0:
                print(i)