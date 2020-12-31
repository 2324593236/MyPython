#集合的创建
set1 = {1,2,"hello","世界"}#直接定义一个集合
set2 = set()#定义一个空集合
list1 = [1,1,2,2]
set3 = set(list1)#变集合去重

#集合元素的添加，删除
set1.add("测试")#在集合一个元素"测试"
print(set1)

set1.remove("测试")#在集合中移除元素“测试”
print(set1)

set4 = set1.pop()#随机移除集合中一个元素并返回删除的元素
print(set1)#移除元素后的集合
print(set4)#移除元素返回的值

set5 = set1.clear()#清空集合内元素
print(set5)

#del set5#删除集合
#print(set5)

##集合的交集、差集、并集、对称差
print(set1-set3)#集合的差集
print(set1|set3)#集合的并集
print(set1&set3)#集合的交集
print(set1^set3)#集合的对称差
