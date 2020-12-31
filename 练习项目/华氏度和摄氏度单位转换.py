##华氏温度与摄氏温度的换算
#公式：华氏度=32+摄氏度*18 单位：℉
#      摄氏度=华氏度/18-32 单位：℃
value1 = None
value2 = None
while True:
    try:
        pd = input("1 华氏度转换为摄氏度\n2 摄氏度转华氏度\n请输入换算方式( 1 或 2 )：")
        if pd == '1':
            value1 = int(input("请输入当前温度(华氏度)："))
            print("输入的温度为:",value1,"℉,转换为摄氏度为:",value1/18-32,"℃\n")
        elif pd == '2':
            value2 = int(input("请输入当前温度(摄氏度)："))
            print("输入的温度为:",value2,"℃,转换为摄氏度为:",value2*18+32,"℉\n")
        else:
            print("\n---------------输入错误，请重新输入---------------\n")
    except ValueError:
        print("\n-------------能不能认真点输入------------\n")
        
