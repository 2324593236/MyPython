import random
##列表的创建与删除
list1 = [1,"a","倪","1","A",["asdf"]]#直接定义一个列表
list2 = []#直接定义一个空列表
list3 = list(range(1,10,1))#用list()函数和range()函数创建一个列表
str1 = "A2s4D5f9g7E5B4a"
list4 = list(str1)#用list()函数转换字符串创建列表
list5 = []

del list2#删除列表list2

##列表的访问
print(list1[2])#用print()函数直接打印输出列表索引为2的元素
print(list1[1:6:2])#用print()函数访问索引值为1-4且步长为2的函数

##列表的遍历
for item in list1:#用for语句遍历列表
    print(item)

for index,item in enumerate(list1):#enumerate()获取索引值函数，index为索引值，item为项
    print(index+1,item)

##列表元素的添加、修改、删除
list1.append("item1")#用listname.append()方法在列表末尾添加元素
print(list1)

list1.insert(1,"item2")#用listname.insert(index,"item")方法在列表索引处添加元素
print(list1)

list1.extend(list4)#用oldlistname.extend(newlistname)方法将将新列表添加至旧列表中
print(list1)

list1[2] = "newstr"#直接访问元素索引进行赋值修改
print(list1)

del list1[2]#用del语句，访问元素索引删除
print(list1)

list1.remove("a")#用listname.remove(item)方法访问列表中元素的值进行删除
print(list1)

##列表的统计计算
print(list1.count("A"))#用listname.count(item)方法统计元素在列表中出现的次数
print(list1.index("A"))#用listname.index(item)方法统计元素在列表中的首次出现的索引值，
print(sum(list5,100))#用sum()函数统计列表中个元素的和加上100的和

##列表的排序
print(sorted(list4,key=None,reverse=False))#用sorted(listname,key,reverse)函数进行key=None区分大小写,reverse=False升序排序
print(sorted(list4,key=str.lower,reverse=True))#用sorted()listname,key,reverse)函数进行key=str.lower不区分大小写,reverse=True降序排序
list4.sort(key=None,reverse=False)#用listname.sort(key,reverse)方法进行key=None区分大小写,reverse=False升序排序
print(list4)
list4.sort(key=str.lower,reverse=True)#用listname.sort(key.reverse)方法进行key=str.lower不区分大小写,reverse=True降序排序
print(list4)

##列表推导式
#for item in range(10):#循环10次
#    list5.append(random.randint(0,100))#向列表中添加0-100内随机的整数
list5 = [random.randint(0,100) for i in range(10)]#循环10次向列表中添加0-100内随机的整数
print(list5)
list5 = [i*i for i in list5]#用列表中每个元素的二次方创建一个列表
print(list5)
list5 = [i*i for i in list5 if i < 4000]#用列表中每个小于4000的元素的二次方创建一个列表
print(list5)
list5 = [i for i in list5 if i%2==0]#查询列表中所有偶数
print(list5)
