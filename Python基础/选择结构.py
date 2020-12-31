#简单if判断
a=200
if a>100:
    print("买车")
else:
    print("买个der")
    
#elif多条件判断
b=200
if b>100:
    print("买，买大的，买两个")
elif b>50:
    print("买，买小的")
elif b>20:
    print("买，买二手的")

#嵌套if
c=int(input("你有多少钱："))
d=int(input("你借多少钱："))
if c>100:
    print("买，买大的")
    if d>50:
        print("买两个")
    elif d>30:
        print("全新的")
    else:
        print("二手的")
else:
    print("买个der")
