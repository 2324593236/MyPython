##遍历目录
import os#调用os模块
path = r"E:\Python\Python学习\练习项目"#设置要遍历的目录路径
print("目录【",path,"】下有：")
for ljstr,mllist,wjlist in os.walk(path,topdown = True):#遍历返回值是一个元组
    for name in mllist:#遍历返回值中的目录列表
        print(os.path.join(ljstr,name),"\n")#路径名与目录名连接
    for name in wjlist:#遍历返回值中的文件列表
        print("\t\t",os.path.join(ljstr,name))#路径名与文件名连接
