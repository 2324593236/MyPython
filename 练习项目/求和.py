##求和
import re#调用正则表达是模块
pattern1 = r"[' '|','|'，'|'']"#定义分隔符模板
pattern2 = r"."
number = 0
while True:
    try:
        list1 = input("请输入要求和的数用，间隔:")#输入要求和的数
        list1 = re.split(pattern1,list1)#用正则表达式过滤输入的数，并返回一个列表
        print("输入的数为：",list1)
        for i in list1:#遍历输入的数
            pd = i.find('.')#用find()函数判定输入的每个数是整型还是浮点型
            if i.find('.') == -1:#返回值为-1,表示没有小数点，是整型
                number += int(i)#将字符串整型化
            else:#返回值不是-1，表示有小数点，是浮点型
                number += float(i)#将字符串浮点型化
        print(number)
    except ValueError:
        print("------------请注意输入格式-------------\n\n")
