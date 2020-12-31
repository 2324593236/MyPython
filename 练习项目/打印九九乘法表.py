# _*_ coding utf-8 _*_
# 开发团队：HS黄舍
# 开发人员：Administrator
# 开发项目：Python Study
# 开发时间：日期:2020/11/27 时间:19:20
# 文件名称：打印九九乘法表.py
# 开发工具：PyCharm
for x in range(1,10):#循环次数
    for y in range(1,x+1):#输出列数
        if x == y:#当行数等于列数时
            print(x,"X",y,"=",x * y,"\n")#结尾换行
        else:#否则
            print(x, "X",y,"=",x * y,end = "\t")#结尾加空格