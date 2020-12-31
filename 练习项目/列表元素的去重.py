##删除列表中的重复项
import re#调用re正则表达式模块
pattern1 = r"[,|，]"#定义分隔符模板
while True:
    list1 = input("请输入要加入列表的值，用逗号分隔：")#输入字符串
    list1 = re.split(pattern1,list1)#用正则表达式分隔字符串，返回值是列表
    print("输入的列表为：",list1)#输出过滤处理后的字符串
    list2 = list(set(list1))#用set()函数过滤重复项,返回值元组，用list()函数将元组转换为列表
    print("去重后的列表为：",list2,"\n\n")#输出处理后的列表
