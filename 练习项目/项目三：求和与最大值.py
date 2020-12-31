#实例三：求和与最大值
summ=0
for i in range(11):#1到10的和
    print(i)
    summ=summ+i
print("1到10的和：",summ)

summ=0
for i in range(0,11,2):#1到10的偶数和
    print(i)
    summ=summ+i
print("1到10的偶数和：",summ)

summ=0
for i in range(1,11,2):#1到10的奇数和
    print(i)
    summ=summ+i
print("1到10的奇数和：",summ)


a=[1,4,6,7,9,2,3,5,8]
maxx=a[0]#设maxx为第一个元素
for i in range(0,len(a)-1):#最大值
    if maxx<=a[i+1]:#用maxx与下一个元素相比较
     maxx=a[i+1]
print(maxx)
    
