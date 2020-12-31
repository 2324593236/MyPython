##变量交换
while True:
    value1 = input("请输入第1个变量：")
    value2 = input("请输入第1个变量：")
    print("第1个变量为：",value1,"第2个变量为：",value2)
    value3 = value1
    value1 = value2
    value2 = value3
    print("-----------------交换后-----------------")
    print("第2个变量为：",value1,"第2个变量为：",value2,"\n\n")
