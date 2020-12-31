###目录
import os#调用os模块全部函数,os模块是操作系统功能和文件系统相关的模块
import shutil#调用shutil模块，可删除非空目录
##os.getcwd()#返回当前工作目录
##os.listdir(path)#返回指定路径下的文件和目录信息
##os.makedir(path[,mode])#创建目录
##os.makedirs(path1/path2...[.mode])#创建多级目录
##os.rmdir(path)#删除目录
##os.removedirs(path1/path2..)#删除多级目录
##os.chdir(path)#把path设置为当前工作目录
##os.walk(top[,topdown[,onerror]])#遍历目录树，该方法返回一个元组，包括所有的路径名、所有目录列表和文件列表3个元素
##os.path.abspath(path)#用于获取文件或目录的绝对路径
##os.path.exists(path)#用于判断目录或者文件是否存在
##os.path.join(path.name)#将目录与目录或者文件名拼接起来
##os.path.splitext()#分离文件名与扩展名
##os.path.basename(path)#从一个目录中提取文件名
##os.path.dirname(path)#从一个路径中提取文件路径，不包括文件名
##os.path.isdir(path)#用于判断是否为路径

##创建目录1
def mkdir(path):#创建一个递归函数用于创建目录
    if not os.path.isdir(path):#判断是否为目录
        mkdir(os.path.split(path)[0])#传递路径，分隔路径名从0开始
    else:#如果存在的话
        print("目录已存在")
        return#返回
    os.mkdir(path)
mkdir(r"E:\Python\Python学习\练习项目\测试目录(None)")

##创建目录2
if not os.path.exists(r"E:\Python\Python学习\练习项目\测试目录(None)"):#判断要创建的目录是否已经存在
    os.mkdir(r"E:\Python\Python学习\练习项目\测试目录(None)")#如果不存在的话，创建目录
else:
    print("目录已存在")

##创建多级目录3
try:
    os.makedirs(r"E:\Python\Python学习\练习项目\测试目录(None)")#用os.makedirs函数直接创建多级目录
except FileExistsError:
    print("目录已存在")

##删除目录(空目录)
if os.path.exists(r"E:\Python\Python学习\练习项目\测试目录(None)"):
    os.rmdir(r"E:\Python\Python学习\练习项目\测试目录(None)")#用os.rmdir函数，可删除空目录
else:
    print("目录不存在")

##删除目录(非空目录)
if os.path.exists(r"E:\Python\Python学习\练习项目\测试目录(None)"):
    shutil.rmtree(r"E:\Python\Python学习\练习项目\测试目录(None)")#用shutil.rmtree函数，可删除非空目录
else:
    print("目录不存在")
    
##判断目录或文件是否存在
print(os.path.exists(r"E:\Python"))#用os.path.exists()判断目录是否存在
print(os.path.exists(r"E:\Python\123"))

##遍历目录
#os.walk(top[,topdown][,onerror][,followlinks])#遍历目录函数，top为要遍历的目录，topdown为True自上而下,为False自下而上，onerror为错误处理方式，followlinks为软连接指向的目录
#返回值（dirpath路径字符串,dirnames子目录列表,filenames文件列表）
value1 = os.walk(r"E:\Python\Python学习\练习项目")#遍历目录
for i in value1 :
    print(i,"\n")

##目录的重命名
#os.rename(oldname,newname)#os.rename()重命名函数,oldname为被重命名的目录路径或文件名，newname为命名后的目录路径或文件名
os.makedirs(r"E:\Python\Python学习\练习项目\测试目录(None)")#用os.makedirs函数直接创建多级目录
os.rename(r"E:\Python\Python学习\练习项目\测试目录(None)",r"E:\Python\Python学习\练习项目\测试目录1(None)")#用os.rename()函数修改路径目录名


