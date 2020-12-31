import random
# _*_ coding utf-8 _*_
# 开发团队：HS黄舍
# 开发人员：Administrator
# 开发项目：Python Study
# 开发时间：日期:2020/11/27 时间:20:44
# 文件名称：字典的创建和删除.py
# 开发工具：PyCharm
a = ["姓名","bh","内容"]#列表
b = ["倪","99","加油"]
c = ("称呼","BH","简介")
d = ("倪","88","努力")
##字典的创建
dictionary1 = dict(zip(a,b))#dict(zip())两个函数结合使用将才列表a，b转换为字典
print(dictionary1)

dictionary2 = dict(zip(c,d))#dict(zip())两个函数结合使用将才元组c，d转换为字典
print(dictionary2)

dictionary3 = {c:b}#用｛元组:列表｝创建键为c元组，值为b列表的字典，列表不能为键
print(dictionary3)

dictionary4 = {}#用｛｝创建空字典
print(dictionary4)

dictionary5 = dict()#用dict()方法创建空字典
print(dictionary5)

dictionary6 = dict(称呼1 = '倪',称呼2 = '倪',称呼3 = '倪')#用dict()方法直接输入元组创建字典
print(dictionary6)

dictionary7 = dict.fromkeys(a)#以列表a为键，值为空创建字典
print(dictionary7)

#del dictionaryname#删除字典

##字典的访问
print(dictionary1["姓名"])#访问字典dictionary1中的“姓名”键的值
print(dictionary1["xm"] if "xm" in dictionary1 else "没有")#访问字典中"xm"键的值，如果"xm"键不存在，返回“没有”
print(dictionary1.get("姓名"))#用get方法访问字典的“姓名”键的值，如果不存在返回“None”
print(dictionary1.get("xm","没有"))#用get方法访问字典的“xm”键的值，如果不存在返回“没有”

##字典的遍历
print(dictionary1.items())#用dictionaryname.items()方法遍历字典

for key,value in dictionary1:#用x为键，y为值，遍历字典
    print("键是：",key,"值是：",value)

for key in dictionary1.keys():#用dictionaryname.keys()方法遍历字典的键
    print(key)

for value in dictionary1.values():#用dictionaty.vales()方法遍历字典的值
    print(value)

##添加修改删除字典元素
dictionary1["keyname"] = "value"#添加字典元素
print(dictionary1)
dictionary1["keyname"] = "newvalue"#如果添加的字典元素键的值已经存在，即为修改
print(dictionary1)
del dictionary1["keyname"]#删除字典的元素
print(dictionary1)

##字典推导式
randomdict = {i:random.randint(1,100) for i in range(1,5)}#创建一个键为i，值为1-100随机数的字典
print(randomdict)