import random
##元组的创建与删除
tuple1 = (1,2,"a","A","倪","1",("zadj"),["adsf"])#直接定义一个元组
tuple2 = ()#定义一个空元组
tuple3 = tuple(range(1,20))#用range()函数创建一个元组
tuple4 = (3,)#定义一个元素的元组，元素末尾添加逗号
tuple5 = ()
tuple6 = (random.randint(0,100),)

del tuple2#用del语句删除元组

##元组的访问
print(tuple1)#用print()函数输出
print(tuple1[1])#通过元素索引访问
print(tuple1[2:6])#通过索引访问第2-5个元素

for item in tuple1:#用for循环遍历
    print(item)

for index,item in enumerate(tuple1):#用for循环和enumerate函数访问元组
    print("第",index+1,"项","为：",item)

##元组的修改
tuple1 = (1,999,"a","A","倪","1",("zadj"),["adsf"])#通过重新定义一个元组进行修改
print(tuple1)
tuple1 = tuple1 + tuple3#通过元组相加的方式进行添加修改
print(tuple1)

##元组推导式
#for i in range(10):#循环10次
#    tuple5 = tuple5 + (random.randint(0,100),)#添加元组0-100内的随机元素
#print(tuple5)

tuple5 = tuple(random.randint(0,100) for i in range(10))#循环10次添加元组0-100内的随机元素
print(tuple5)
