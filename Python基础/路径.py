###路径
import os
#相对路径
print(os.getcwd())
with open("素材\测试(None).txt") as file:#通过相对路径打开文件
    print(file.read())

#绝对路径
print(os.path.abspath(r"素材\测试(None).txt"))#通过相对路径获取绝对路径

#拼接路径
print(os.path.join(r"E:\Python\Python学习",r"素材\测试(None).txt"))
