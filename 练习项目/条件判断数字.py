# _*_ coding utf-8 _*_
# 开发团队：HS黄舍
# 开发人员：Administrator
# 开发项目：Python Study
# 开发时间：日期:2020/11/27 时间:18:36
# 文件名称：条件判断数字.py
# 开发工具：PyCharm
print('今有物，不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？')
#number = int(input('请输入为何数：'))
for number in range(0,999999):
    if number%3 == 2 and number%5 == 3 and number%7 == 2:
        print(number,"符合条件")

