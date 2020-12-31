#项目一：快递价格计算器
#架构外层条件尽量要少，重量weight条件有两个，地区编号num条件有4个，所以外层架构用重量条件，可以尽可能的减少代码数量
while 1==1:
    print("欢迎来的快递价格计算器！")
    weight=int(input("请输入重量(kg)："))
    num=input("请输入收货的编号(01.其他 02.东三省/宁夏/青海/海南 03.新疆/西藏 04.港澳台/国外:")

    p=0
    if weight>=3:
        if num=="01":
            p=10+5*(weight-3)
        elif num=="02":
            p=12+5*(weight-3)
        elif num=="03":
            p=20+5*(weight-3)
        elif num=="04":
            p="error"
        else:
            print("输入错误！！！")
    elif weight<3 and weight>0:
        if num=="01":
            p=10
        elif num=="02":
            p=12
        elif num=="03":
            p=20
        elif num=="04":
            p="error"
            print("不接受寄件")
        else:
            print("输入错误！！！")
    else:
        p="error"
        print("输入错误！！！")

    print("此件包裹价格为:",p,"元")

