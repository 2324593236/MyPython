#循环结构
list=[1,2,3,4]#列表
tuple=(1,2,3,4)#元组
dictionary={"name":"张三","age":99}#字典
col={"a","b","c","d"}#集合

#for循环
for i in range(10):#for循环：实质是对序列的遍历
    print("第",i+1,"次","hello world")
    print("测试")

for i in list:#遍历列表
    print(i)

for i in tuple:#遍历元组
    print(i)

for i in dictionary:#遍历字典
    print(i)#直接遍历字典只能输出字典中的键
    print(dictionary[i])#遍历字典中键的值

for i in col:#遍历集合
    print(i,)
print("\n")

#while循环
i=0
while i<=10:
    print(i)
    if i==5:
        print("休息")
    i=i+1
print("\n")

#嵌套循环
i=1
sum=0
while i<=10:
    print("第",i,"年")
    if i==5:
        print("今年不用给")
        #continue#continue结束本次循环，进入下一次循环
        #break#结束整个循环
    j=1
    while j<=12:
        sum=sum+1
        if j==6:
            j=j+1
            continue
        print("第",i,"年",j,"月支付",1,"已支付:",float(sum))
        j=j+1
    i=i+1
print("\n")

#无限循环
import time
i=1
while 1==1:
    print(i)
    i=i+1
    time.sleep(1)
