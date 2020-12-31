# _*_ coding utf-8 _*_
# 开发团队：HS黄舍
# 开发人员：Administrator
# 开发项目：Python Study
# 开发时间：日期:2020/11/24 时间:12:46
# 文件名称：创建输出文本文件.py
# 开发工具：PyCharm
fp = open(r'E:\Python\Python学习\文本文件.txt','a+')#打开文本文件.txt，'a+'最佳形式
print("坚持就是胜利，用尽自己的每一分钟，谢谢！！！",file = fp)#写入文本。。。。到fp
fp.close()#关闭fp