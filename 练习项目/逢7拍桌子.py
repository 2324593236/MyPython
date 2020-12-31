# _*_ coding utf-8 _*_
# 开发团队：HS黄舍
# 开发人员：Administrator
# 开发项目：Python Study
# 开发时间：日期:2020/11/27 时间:19:48
# 文件名称：逢7拍桌子.py
# 开发工具：PyCharm
i = range(1,100)#建立1-99数字
count = 0
for x in i :
    if x%7 == 0:#遍历到7的倍数时
        print("啪")
        count +=1#拍桌子次数加一
        continue#跳出本次小循环，进入下一次循环
    elif str(x).startswith("7"):#遍历到开头是7的数时
        print("啪")
        count +=1
        continue
    elif str(x).endswith("7"):#遍历到结尾是7的数时
        print("啪")
        count +=1
        continue
    else:
        print(x)
        continue
print("拍桌子的次数为：",count)