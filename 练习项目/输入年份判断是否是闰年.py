###输入年份判断是否是闰年
years = input("输入年份\n")
try:
    if years or years >= 0 :
        if int(years) % 4 == 0:
            print(years,"是闰年")
        else:
            print(years,"不是闰年")
except ValueError:
    print("请正确输入")