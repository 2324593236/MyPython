##判断一个数是否为素数
while True:
    try:
        number = int(input("请输入你要判断的数："))
        if number == 2 or number % 2 != 0 or number %3 != 0:
            print(number,"是素数---------------\n")
        else:
            print(number,"不是素数---------------\n")
    except ValueError:
        print("不是整数或数字无法判断-------------")
          
        

