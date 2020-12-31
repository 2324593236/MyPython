#生成99个随机但不重复的整数
import random#调用随机数模块
list1 = []
while len(list1)<99:
    number = random.randint(1,99)
    if number not in list1:#过滤列表是是否存在该元素，不存在的话添加，存在的话舍去
        list1.append(number)
print(list1)
print(len(list1))#列表长度
list1.sort(key=None,reverse=False)#升序排序
print(list1)
