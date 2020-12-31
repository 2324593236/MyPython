###输入三边长求三角形变长面积
a = float(input("请输入a边长："))
b = float(input("请输入b边长："))
c = float(input("请输入c边长："))
bc = a+b+c
if a+b>c and a+c>b and b+c>a:
    print("三角形的周长为:",bc)
    print("三角形的面积为:",bc/2*(bc/2-a)*(bc/2-b)*(bc/2-c)**0.5)
    